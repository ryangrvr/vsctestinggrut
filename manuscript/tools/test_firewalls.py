#!/usr/bin/env python3
"""Negative tests for the semantic firewalls: each violating snippet must be caught,
each compliant snippet must pass. Run by `make check` before check.py."""
import sys
import unittest

import firewalls as fw


def flags(text):
    return [v[1][:3] for v in fw.semantic(text, "t")]


class Semantic(unittest.TestCase):
    def test_numerical_delta(self):
        self.assertIn("(b)", flags(r"We find $\delta = 0.3$ for this model."))
        self.assertIn("(b)", flags(r"Here $N_0(t) = 12$ suffices."))
        self.assertIn("(b)", flags(r"The window is $\delta \approx 1$."))
        self.assertEqual(flags(r"Put $\delta = \min(1, |c_7|/(2\Lambda))$."), [])
        self.assertEqual(flags(r"$\exists\, \delta > 0$ such that $N_0(t) < \infty$."), [])
        self.assertIn("(b)", flags(r"One can take $\delta < 0.2$."))

    def test_uniform_threshold(self):
        self.assertIn("(c)", flags(r"The threshold $N_0$ is uniform in $t$."))
        self.assertEqual(flags(r"$N_0(t)$ is not claimed to be uniform in $t$."), [])

    def test_tstar_inside_window(self):
        self.assertIn("(d)", flags(r"The time $t_\star = 0.5$ lies in $(0, \delta)$."))
        self.assertIn("(d)", flags(r"Since $t_\star \in (0, \delta)$, the theorem applies."))
        self.assertEqual(flags(r"$t_\star = 0.5$ is not claimed to lie inside $(0, \delta)$."), [])

    def test_reservoir_not_H(self):
        self.assertIn("(e)", flags(r"In the reservoir limit the environment becomes a member of $\mathcal{H}$."))
        self.assertIn("(e)", flags(r"The limit is the harmonic bath."))
        self.assertEqual(flags(r"The limit is not a statement that the environment enters $\mathcal{H}$."), [])
        self.assertEqual(flags(r"The finite model remains anharmonic while its laws approach the common Gaussian limit."), [])

    def test_effective_harmonic(self):
        self.assertIn("(f)", flags(r"We show the reservoir is an effective harmonic bath."))
        self.assertIn("(f)", flags(r"This quantifies why effective-harmonic descriptions are hard to escape."))
        self.assertEqual(flags(r"Whether it admits an effective harmonic-bath description is not addressed here [2]."), [])


class Quantifiers(unittest.TestCase):
    GOOD = " ".join(fw.QUANTIFIER_CHAIN)

    def test_good_chain(self):
        self.assertEqual(fw.quantifiers(self.GOOD, self.GOOD + " x " + self.GOOD, self.GOOD), [])

    def test_swapped_quantifiers(self):
        bad = self.GOOD.replace(r"for each fixed $t \in (0, \delta)$", r"for all $t \in (0, \delta)$")
        self.assertTrue(any("(a)" in v[1] for v in fw.quantifiers(bad, bad + bad, bad)))

    def test_missing_nonuniform_clause(self):
        bad = self.GOOD.replace(r"$N_0(t)$ is not claimed to be uniform in $t$", "")
        self.assertTrue(any("missing" in v[1] for v in fw.quantifiers(bad, bad + bad, bad)))

    def test_statement_absent_from_section_4(self):
        self.assertTrue(any("both" in v[1] for v in fw.quantifiers(self.GOOD, self.GOOD, self.GOOD)))


if __name__ == "__main__":
    r = unittest.main(exit=False, verbosity=1).result
    sys.exit(0 if r.wasSuccessful() else 1)
