"""Stage-3 evaluation kit, item (a): L0 normalizer and price coder (charter §4.1-§4.4, App. B).

Charter: PROGRAM/STAGE3/STAGE3_CHARTER.md (CR-1 re-freeze 0b414e6). This module prices
expressions; it contains no candidate law and evaluates none.

Expression format: nested tuples in prefix (Polish) form, e.g.
    ('forall', 'x', ('->', ('in', 'x', 'V'), ('=', ('apply', 'f', 'x'), 'x')))
Leaves are variable names (str), or literals: ('nat', n), ('rat', n, d), ('real', mantissa_bits, exponent).
"""
from math import floor, log2, ceil, comb

# ---- Appendix B.1: the 64-token alphabet (60 usable + 4 reserved) -------------------
LOGIC = ['not', 'and', 'or', '->', '<->', 'forall', 'exists', '=', '!=', 'top', 'bot', 'ite']
SETS = ['in', 'subseteq', 'emptyset', 'singleton', 'pair', 'times', 'powerset', 'card',
        'union', 'inter', 'minus', 'range']
MAPS = ['lambda', 'apply', 'compose', 'id', 'image', 'preimage', 'inverse', 'restrict']
ARITH = ['0', '1', 'succ', '+', '-', '*', '/', '<=', '<', 'sum_finite']
COND = ['kernel', 'cond_prob', 'E', 'tensor', 'marginal', 'do', 'law', 'support']
PROC = ['sequential', 'parallel', 'contract', 'wire']
STRUCT = ['def', 'var', 'nat', 'rat', 'real', 'end']
RESERVED = ['reserved1', 'reserved2', 'reserved3', 'reserved4']
ALPHABET = LOGIC + SETS + MAPS + ARITH + COND + PROC + STRUCT + RESERVED
assert len(ALPHABET) == 64 and len(set(ALPHABET)) == 64
BITS_PER_TOKEN = 6  # log2(64)
USABLE = set(ALPHABET) - set(RESERVED)

ARITY = {'not': 1, 'and': 2, 'or': 2, '->': 2, '<->': 2, 'forall': 2, 'exists': 2,
         '=': 2, '!=': 2, 'top': 0, 'bot': 0, 'ite': 3}


def elias_delta_len(n):
    """Length in bits of the Elias-delta code of a positive integer n."""
    if n < 1:
        raise ValueError('Elias-delta needs n >= 1')
    L = floor(log2(n)) + 1
    return (L - 1) + 2 * floor(log2(L)) + 1


def ell(n):
    """Charter §4.1: l(n) := Elias-delta length of n + 1 (n a natural number)."""
    return elias_delta_len(n + 1)


def literal_bits(lit, p):
    kind = lit[0]
    if kind == 'nat':
        return ell(lit[1])
    if kind == 'rat':
        return ell(abs(lit[1])) + ell(lit[2]) + 1
    if kind == 'real':  # ('real', exponent): mantissa at precision p, exponent, sign
        return p + ell(abs(lit[1])) + 1
    raise ValueError(lit)


def is_literal(x):
    return isinstance(x, tuple) and x and x[0] in ('nat', 'rat', 'real')


def tokens_and_vars(expr, out_tokens, var_occ, literals):
    if is_literal(expr):
        out_tokens.append(expr[0])  # the literal-kind token itself costs 6 bits
        literals.append(expr)
        return
    if isinstance(expr, str):
        if expr in USABLE:
            out_tokens.append(expr)
        elif expr in RESERVED:
            raise ValueError('reserved token used by a card: ' + expr)
        else:
            out_tokens.append('var')
            var_occ.append(expr)
        return
    head, *args = expr
    if head in RESERVED:
        raise ValueError('reserved token used by a card: ' + head)
    if head not in USABLE:
        raise ValueError('unknown token: ' + str(head))
    out_tokens.append(head)
    for a in args:
        tokens_and_vars(a, out_tokens, var_occ, literals)


def L_stmt(expr, p=10):
    """Charter §4.1: 6·#tokens + Σ_var-occurrences ceil(log2(v+1)) + Σ_literals l(lit)."""
    toks, occ, lits = [], [], []
    tokens_and_vars(expr, toks, occ, lits)
    v = len(set(occ))
    var_bits = len(occ) * ceil(log2(v + 1)) if occ else 0
    return BITS_PER_TOKEN * len(toks) + var_bits + sum(literal_bits(l, p) for l in lits)


# ---- Normalizer: prenex negation normal form (charter §4.1) --------------------------
def _nnf(e, neg=False):
    if isinstance(e, str) or is_literal(e):
        return ('not', e) if neg else e
    h = e[0]
    if h == 'not':
        return _nnf(e[1], not neg)
    if h == '->':
        return _nnf(('or', ('not', e[1]), e[2]), neg)
    if h == '<->':
        a, b = e[1], e[2]
        return _nnf(('and', ('->', a, b), ('->', b, a)), neg)
    if h in ('and', 'or'):
        hh = h if not neg else ('or' if h == 'and' else 'and')
        return (hh, _nnf(e[1], neg), _nnf(e[2], neg))
    if h in ('forall', 'exists'):
        hh = h if not neg else ('exists' if h == 'forall' else 'forall')
        return (hh, e[1], _nnf(e[2], neg))
    if h == 'top':
        return ('bot',) if neg else e
    if h == 'bot':
        return ('top',) if neg else e
    return ('not', e) if neg else e  # atoms


def _rename(e, old, new):
    if isinstance(e, str):
        return new if e == old else e
    if is_literal(e):
        return e
    if e[0] in ('forall', 'exists') and e[1] == old:
        return e
    return tuple([e[0]] + [_rename(a, old, new) for a in e[1:]])


def _prenex(e, counter):
    if isinstance(e, str) or is_literal(e) or e[0] not in ('and', 'or', 'forall', 'exists'):
        return [], e
    if e[0] in ('forall', 'exists'):
        fresh = 'q%d' % counter[0]
        counter[0] += 1
        q, m = _prenex(_rename(e[2], e[1], fresh), counter)
        return [(e[0], fresh)] + q, m
    q1, m1 = _prenex(e[1], counter)
    q2, m2 = _prenex(e[2], counter)
    return q1 + q2, (e[0], m1, m2)


def normalize(expr):
    """Prenex negation normal form with explicit quantifiers and no Skolem symbols.
    Bound variables are renamed apart (q0, q1, ...) in order of appearance."""
    q, matrix = _prenex(_nnf(expr), [0])
    out = matrix
    for kind, v in reversed(q):
        out = (kind, v, out)
    return out


# ---- Price coder: §4.2 items and §4.3-§4.4 verdicts ----------------------------------
def ip4_selection(L, family_size):
    return max(L, log2(family_size)) if family_size and family_size > 1 else L


def ip5_constant(literal_len, R_over_window=None, exact_expr_len=None):
    """IP-5: max(literal length at p, log2(R/passing window)); zero-width windows are
    priced at L_stmt of the expression stating the value (CR-1, finding 16)."""
    if exact_expr_len is not None:
        return max(literal_len, exact_expr_len)
    return max(literal_len, log2(R_over_window)) if R_over_window else literal_len


def ip12_tax(n_drafts):
    return log2(1 + n_drafts)


def ip13_domain(L_pred, N_AI3, N_total, k_ex):
    """IP-13 (CR-1 wording): max(L_stmt(pred), log2 C(N_AI3, ceil(N_AI3*k_ex/N)))."""
    k = ceil(N_AI3 * k_ex / N_total) if N_total else 0
    return max(L_pred, log2(comb(N_AI3, k))) if k > 0 else L_pred


VOCAB_ITEM_BITS = 4  # IP-6: ceil(log2 16) per canonical VB item


def price(ledger):
    """ledger: list of dicts {'item', 'class', 'bits'}; returns total Price."""
    return sum(r['bits'] for r in ledger)


def compression_verdict(b_J, D_sel, price_by_p, p_star=10):
    """§4.3-§4.4: ΔL0 = b_J − Price; ΔL = b_J + D_sel − Price (b_J uses p★ at every p).
    price_by_p: {6: P6, 10: P10, 16: P16}."""
    dL0 = {p: b_J - P for p, P in price_by_p.items()}
    dL = {p: b_J + D_sel - P for p, P in price_by_p.items()}
    if dL[10] <= 0:
        verdict = 'LOOKUP'
    elif dL0[10] >= p_star and dL0[16] > 0:
        verdict = 'COMPRESSIVE'
    else:
        verdict = 'NON-COMPRESSIVE'
    return {'dL0': dL0, 'dL': dL, 'verdict': verdict}


def coupling_credit(c_inst, c_J, c_lock, N_fib, c_fam=None, kappa=None, p_star=10):
    """§2.5: b_J = min{ N_fib · min_ι [p★·min(c_ι, c_J, c_lock) + κ-terms], p★·c_fam + κ_fam }.
    c_inst: list of per-instance codimensions over I_K (minimum taken over all of I_K)."""
    k_inst, k_J, k_lock, k_fam = (kappa or ([0] * len(c_inst), 0, 0, 0))
    per = min(p_star * min(ci, c_J, c_lock) + min(ki, k_J, k_lock)
              for ci, ki in zip(c_inst, k_inst))
    b = N_fib * per
    if c_fam is not None:
        b = min(b, p_star * c_fam + k_fam)
    return b
