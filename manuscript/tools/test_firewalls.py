#!/usr/bin/env python3
"""Negative and positive regression tests for the firewalls: every red-team sentence found by
the conformance reviews must be caught, and every compliant sentence from the manuscript must pass.
Also covers the numeric-literal (C3) and vocabulary (C6) scanners of check.py.
Run by `make check` before check.py."""
import sys
import unittest

import check
import firewalls as fw


def flags(text):
    return [v[1][:3] for v in fw.semantic(text, "t")]


class Semantic(unittest.TestCase):
    def test_numerical_delta(self):
        for bad in [r"We find $\delta = 0.3$ for this model.",
                    r"Here $N_0(t) = 12$ suffices.",
                    r"The window is $\delta \approx 1$.",
                    r"One can take $\delta < 0.2$.",
                    r"$\delta \lesssim 0.3$ in practice.",
                    r"$N_{0} = 12$ is enough.",
                    r"We have $0.2 > \delta$ here.",
                    r"a threshold of about $40$ suffices for $N_0$"]:
            self.assertIn("(b)", flags(bad), bad)
        for ok in [r"Put $\delta = \min(1, |c_7|/(2\Lambda))$.",
                   r"$\exists\, \delta > 0$ such that $N_0(t) < \infty$.",
                   r"There exists $\delta \in (0, 1]$ such that the sign is fixed.",
                   r"$N_0(t) = \lfloor \Theta(t)/|K(t)| \rfloor + 1$, a finite integer."]:
            self.assertEqual([f for f in flags(ok) if f == "(b)"], [], ok)

    def test_uniform_threshold(self):
        for bad in [r"The threshold $N_0$ is uniform in $t$.",
                    r"A single threshold works for all $t$.",
                    r"The threshold $N_0(t)$ does not depend on $t$."]:
            self.assertIn("(c)", flags(bad), bad)
        for ok in [r"$N_0(t)$ is not claimed to be uniform in $t$.",
                   r"no uniform $N_0$ over the interval is claimed",
                   r"It is not a uniform statement over an interval, and neither $\delta$ nor $N_0(t)$ is computed."]:
            self.assertEqual([f for f in flags(ok) if f == "(c)"], [], ok)

    def test_tstar_inside_window(self):
        for bad in [r"The time $t_\star = 0.5$ lies in $(0, \delta)$.",
                    r"Since $t_\star \in (0, \delta)$, the theorem applies.",
                    r"$t_\star = 0.5$ lies inside $(0, \delta)$, so no further check is needed.",
                    r"At $t = 0.5$ the window covers the computation and Theorem 1 applies.",
                    r"Proposition 1(a) predicts the value at $t_\star = 0.5$."]:
            self.assertIn("(d)", flags(bad), bad)
        for ok in [r"$t_\star = 0.5$ is not claimed to lie inside $(0, \delta)$.",
                   r"No statement that any particular numerical time, including $t_\star = 0.5$ used in Section 6, lies inside $(0, \delta)$.",
                   r"The times $t_\star = 0.5$ and $0.25$ were fixed in advance; none of the times is claimed to lie inside the theorem's window $(0, \delta)$.",
                   r"none of them is claimed to lie inside the theorem's window $(0, \delta)$",
                   r"the expansion holds at every fixed $t \in [0, 2\pi]$ and not only in the theorem's window"]:
            self.assertEqual([f for f in flags(ok) if f == "(d)"], [], ok)

    def test_reservoir_not_H(self):
        for bad in [r"In the reservoir limit the environment becomes a member of $\mathcal{H}$.",
                    r"The limit is the harmonic bath.",
                    r"In the reservoir limit the environment becomes a harmonic bath, with no anharmonic correction.",
                    r"As $N_B \to \infty$ the bath is effectively a harmonic one, and not weakly so."]:
            self.assertIn("(e)", flags(bad), bad)
        for ok in [r"The limit is not a statement that the environment enters $\mathcal{H}$.",
                   r"| model $\mathcal{D}$ in the reservoir limit | centred laws converge to one common Gaussian law ($\mathcal{E}_1$-type, finite-dimensional; not $\mathcal{H}$) |",
                   r"Whether that limit admits an effective harmonic-bath description is not addressed here; it connects to the influence-functional literature [2] [3].",
                   r"Nor is it a statement that the environment enters the harmonic class $\mathcal{H}$: no harmonic-bath realisation of it is constructed.",
                   r"The finite model remains anharmonic while its laws approach the common Gaussian limit.",
                   r"The finite-$N_B$ model remains anharmonic for every $N_B$; its centred force laws approach the common Gaussian limit."]:
            self.assertEqual([f for f in flags(ok) if f == "(e)"], [], ok)

    def test_effective_harmonic(self):
        for bad in [r"We show the reservoir is an effective harmonic bath.",
                    r"This quantifies why effective-harmonic descriptions are hard to escape.",
                    r"We prove the harmonic mapping of the limit, which is not difficult, citing [2]."]:
            self.assertIn("(f)", flags(bad), bad)
        for ok in [r"Whether it admits an effective harmonic-bath description is not addressed here [2].",
                   r"Whether that limit admits an effective harmonic-bath description is not addressed here; it connects to the influence-functional literature [2] [3]."]:
            self.assertEqual([f for f in flags(ok) if f == "(f)"], [], ok)


class Quantifiers(unittest.TestCase):
    STMT = ("**Theorem.** Preamble text here. " + " middle ".join(fw.QUANTIFIER_CHAIN) + " tail.")

    def check(self, full, s1=None):
        return fw.quantifiers(self.STMT, full, self.STMT if s1 is None else s1)

    def test_good(self):
        self.assertEqual(self.check(self.STMT + " x " + self.STMT), [])

    def test_swapped_quantifiers(self):
        bad = self.STMT.replace(r"for each fixed $t \in (0, \delta)$", r"for all $t$ at once")
        self.assertTrue(any("(a)" in v[1] for v in fw.quantifiers(bad, bad + bad, bad)))

    def test_missing_nonuniform_clause(self):
        bad = self.STMT.replace(r"$N_0(t)$ is not claimed to be uniform in $t$", "")
        self.assertTrue(any("missing" in v[1] for v in fw.quantifiers(bad, bad + bad, bad)))

    def test_statement_absent_from_section_4(self):
        self.assertTrue(any("S1" not in v[0] for v in self.check(self.STMT)))

    def test_tamper_after_first_200_chars(self):
        tampered = self.STMT.replace(r"$N_0(t)$ is not claimed to be uniform in $t$",
                                     r"$N_0$ is uniform in $t$")
        self.assertTrue(any("(a)" in v[1] for v in self.check(self.STMT + " x " + tampered)))


class Scanners(unittest.TestCase):
    def test_numeric_literals(self):
        self.assertTrue(check.numeric_scan("t.md", "the variance is 0.4679 here"))
        self.assertTrue(check.numeric_scan("t.md", "a constant 28 appears"))
        self.assertTrue(check.numeric_scan("t.md", "differ by three orders of magnitude"))
        self.assertTrue(check.numeric_scan("t.md", "to seven significant figures"))
        self.assertFalse(check.numeric_scan("t.md", "at $t_\\star = 0.5$ with $\\beta = 1$"))
        self.assertFalse(check.numeric_scan("t.md", "value ${{num.global_p}}$ and $N_B \\in \\{4, 8, 16, 32, 64, 128\\}$"))

    def test_vocab(self):
        self.assertTrue(check.vocab_scan("t", "the GRUT program"))
        self.assertTrue(check.vocab_scan("t", "two GRUTs walk in"))
        self.assertTrue(check.vocab_scan("t", "several charters were frozen"))
        self.assertTrue(check.vocab_scan("t", "the owner's ruling"))
        self.assertTrue(check.vocab_scan("t", "ontological commitments"))
        self.assertFalse(check.vocab_scan("t", "aggregate data on the frontier"))
        self.assertFalse(check.vocab_scan("t", "the gatekeeper problem"))  # 'gate' only as a word


if __name__ == "__main__":
    r = unittest.main(exit=False, verbosity=1).result
    sys.exit(0 if r.wasSuccessful() else 1)
