"""Finite actual-circle Bose counting certificate; no asymptotic approximation.

The analytic Green blocks and receiver scope are proved in
the finite-band counting appendix of the accompanying final manuscript.
Only a specified finite detection band is measured; omitted modes are not
assigned zero occupation. Arithmetic uses Arb.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def rat(value):
    value = Fraction(str(value))
    return arb(value.numerator) / value.denominator


def positive(x, label):
    if not x > 0:
        raise ArithmeticError("Unproved strict positive bound: " + label)


def run(precision):
    ctx.prec = precision
    pi = arb.pi()
    inner, outer, base = rat("99/200"), rat("101/200"), rat("1/2")
    beta, eta, angle = rat("1/20"), rat("7/10"), rat("1/10")
    tilt_null, tilt_signal, dark = rat("3/2"), rat(1), rat("1/10")
    null_logmgf, signal_loglaplace = rat(0), rat(0)
    null_mean_upper, signal_mean_lower = rat(0), rat(0)
    signal_band_number, reference_band_number = rat(0), rat(0)
    signal_band_energy, reference_band_energy = rat(0), rat(0)
    sin2, sin_square = (2 * angle).sin(), angle.sin() ** 2
    for n in range(50, 501):
        # Pushforward masses 1/2 and 1/2, normalized angular measure dtheta/2pi.
        factor = 1 / (8 * pi * n)
        k11 = factor * (1 - inner ** (2 * n))
        k22 = factor * (1 - outer ** (2 * n))
        k12 = factor * ((inner / outer) ** n - (inner * outer) ** n)
        diagonal_difference = k11 - k22
        # Multiplication remains valid when this tiny difference straddles zero;
        # this runtime's generic real-power operation can return NaN there.
        discriminant = (diagonal_difference * diagonal_difference
                        + 4 * k12 * k12).sqrt()
        small = (k11 + k22 - discriminant) / 2
        large = (k11 + k22 + discriminant) / 2
        positive(small, f"positive actual Green block, n={n}")
        positive(discriminant, f"distinct eigenvalues, n={n}")
        ns = 1 / ((beta / small.sqrt()).exp() - 1)
        nl = 1 / ((beta / large.sqrt()).exp() - 1)
        slope = (nl - ns) / discriminant
        positive(slope, f"increasing Bose function, n={n}")
        positive(k12, f"positive cross block, n={n}")
        # For EVERY angle theta_n in [-angle,angle], possibly mode dependent:
        # q_theta' N q_theta >= (nl+ns)/2 - slope*k12
        #                            - |slope*(k11-k22)| sin(2 angle)/2.
        signal_lower = eta * ((nl + ns) / 2 - slope * k12
                              - abs(slope * (k11 - k22)) * sin2 / 2)
        positive(signal_lower, f"positive signal occupation, n={n}")
        kbase = (1 - base ** (2 * n)) / (4 * pi * n)
        nbase = 1 / ((beta / kbase.sqrt()).exp() - 1)
        reference_upper = eta * sin_square * nbase
        denom_null = 1 - reference_upper * (tilt_null.exp() - 1)
        positive(denom_null, f"finite null count mgf, n={n}")
        null_logmgf -= 2 * denom_null.log()
        signal_loglaplace -= 2 * (1 + signal_lower *
                                 (1 - (-tilt_signal).exp())).log()
        null_mean_upper += 2 * reference_upper
        signal_mean_lower += 2 * signal_lower
        # Both angular signs are included. These are prepared-band costs,
        # before detector loss, not claims about total full-ensemble cost.
        signal_band_number += 2 * (ns + nl)
        reference_band_number += 2 * nbase
        signal_band_energy += 2 * (ns / small.sqrt() + nl / large.sqrt())
        reference_band_energy += 2 * nbase / kbase.sqrt()
    # Declare split geometry iff total recorded count >=5.
    # Independent Poisson dark mean in [0,.1]: worst case .1 under null;
    # dropping dark counts under signal only increases false negatives.
    false_positive = (-5 * tilt_null + null_logmgf
                      + dark * (tilt_null.exp() - 1)).exp()
    false_negative = (4 * tilt_signal + signal_loglaplace).exp()
    error = (false_positive + false_negative) / 2
    positive(rat("57/10000") - false_positive, "false positive < .0057")
    positive(rat("72/100000") - false_negative, "false negative < .00072")
    positive(rat("32/10000") - error, "equal-prior error < .0032")
    return {
        "precision_bits": precision,
        "false_positive_upper_ball": str(false_positive),
        "false_negative_upper_ball": str(false_negative),
        "equal_prior_error_upper_ball": str(error),
        "null_mean_upper_without_dark_ball": str(null_mean_upper),
        "signal_mean_lower_without_dark_ball": str(signal_mean_lower),
        "prepared_signal_band_mean_quanta_ball": str(signal_band_number),
        "prepared_reference_band_mean_quanta_ball": str(reference_band_number),
        "prepared_signal_band_excitation_energy_ball": str(signal_band_energy),
        "prepared_reference_band_excitation_energy_ball": str(reference_band_energy),
        "assertions_passed": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("circular_count_certificate_256.json"))
    args = parser.parse_args()
    result = {
        "status": "validated finite-band common-Fock discrimination, not a device",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters": {
            "carrier": "unit Euclidean disk, Dirichlet boundary",
            "circle_radii": ["99/200", "101/200"],
            "layer_masses": ["1/2", "1/2"],
            "reference_radius": "1/2", "reference_mass": "1",
            "gamma": "1/2", "epsilon": "1/100", "tau": "1/2",
            "beta": "1/20", "efficiency": "7/10",
            "per_angular_mode_sorter_angle_range_radians": ["-1/10", "1/10"],
            "independent_Poisson_dark_mean_range": ["0", "1/10"],
            "angular_indices": "50<=|n|<=500",
            "detected_modes": 902, "prepared_band_modes": 1804,
            "decision_threshold": 5,
            "null_Chernoff_tilt": "3/2", "signal_Laplace_tilt": "1",
        },
        "certificate": run(args.precision),
        "scope": [
            "Exact actual-circle Green blocks; no Weyl or collision approximation.",
            "Constant sorter errors confined to each selected angular two-layer block.",
            "Ideal rejection of unmeasured angular modes; no stopband leakage certified.",
            "Full number-conserving Bose state or exactly its measured-band marginal.",
            "All signals cost many prepared quanta; no per-phonon or quantum advantage.",
            "No claim that the aligned Fock model is an unmodified mechanical membrane.",
        ],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
