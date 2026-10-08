# Transverse information beyond thermal scalar limits in colliding layers

R. Arun Chandru · 8 October 2026

## Extended abstract

Imagine several closely spaced layers carrying the mass of a vibrating or encoded wave system. At long wavelengths they can look like one layer. At wavelengths comparable with their separation, however, their relative motions remain distinct. A thermal state spreads its population over many wavelengths, so whether it resolves the layers depends on how the temperature changes as the layers approach each other.

This paper calculates that joint limit for actual curved layers in a planar Dirichlet carrier. It does not replace the geometry by two guessed oscillator modes. A positive matrix-valued function determines the contribution of every relevant wavelength, and the proof controls the remaining low- and high-frequency tails. It yields the partition function, the full normalized one-excitation state, and the response of a measurement that coherently compares layer amplitudes.

The principal information result is a separation between selected thermal summaries and distinguishability. After first taking the joint geometric limit, and then a high-temperature limit of its coefficients, the one-excitation entropy differences from the collapsed reference vanish. Dimensionless energy statistics and ordinary smooth spatial expectations agree as well. Nevertheless, for M equally weighted layers, the trace distance tends to 1−1/M. A single controlled excitation can then be classified with limiting equal-prior error 1/(2M). M is fixed before either limit. This does not say that the two spectra or all measurements are equal at a finite temperature and separation.

The geometric crossover has further structure. Its eigenvalue count is strictly below the collapsed count at every finite scaled energy. This uses a classical sharp one-dimensional spectral inequality after a new actual-geometry transfer; the old inequality itself is not claimed as new. At the other thermal endpoint, the transverse signal usually decays algebraically even though excited spectral branches are exponentially suppressed. The surviving signal comes from rotation of the lowest branch relative to the fixed layer-comparison measurement. Two equally weighted layers are the exceptional nontrivial profile with no such rotation term.

Preparation changes the meaning of the information result. Deliberately preparing one excitation can avoid the exponentially rare event of finding exactly one excitation in a large equilibrium Bose sample. The paper gives a finite common encoding and pays for truncation, filtering acceptance, optical elements, bandwidth, timing and source failures. Alternatively, one can use an entire number-conserving Bose ensemble. Such a sample contains many quanta: in the frequency case the mean number grows as the inverse layer separation and the excitation energy grows as its inverse three-halves power. It is not a free single-photon improvement.

A calibrated total-count threshold tolerates sufficiently small fixed sorting errors. The most highly occupied low-frequency modes limit its concentration. A common filter constructed from the two candidate operators removes these modes while preserving a macroscopic transverse signal. With a stated positive mean margin, its error bound interpolates explicitly with stopband leakage. For the frequency exponent, leakage amplitude of order the fourth root of the separation is sufficient to retain the stronger exponential rate.

Finally, two exact concentric-circle Green matrices provide a finite example. At the displayed parameters, the specified receiver has rigorously bounded equal-prior error below 0.0032, with 70% collection efficiency, separate real sorting errors of up to 0.1 radians in each selected angular sector, and independent Poisson dark counts of mean at most 0.1 per gate. The source band contains 1804 modes and has different mean populations under the two hypotheses, approximately 61.7931 and 81.3157. Thus the example certifies its discrimination result, not matched brightness or the asymptotic entropy agreement at that finite point. Ball-arithmetic certificates and a portable verifier are included.

## Files

- `r_arun_chandru_transverse_information_in_colliding_layers.tex`: complete standalone LaTeX source, with embedded bibliography and all appendices.
- `r_arun_chandru_transverse_information_in_colliding_layers.pdf`: the article, produced after scientific content freeze.
- `verification/verify_circular_counts.py`: portable validated-arithmetic calculation of the finite circular bounds.
- `verification/requirements.txt`: the pinned Python dependency.
- `verification/circular_count_certificate_256.json` and `verification/circular_count_certificate_1152.json`: two precision replays of the same finite expressions.
- `verification/README.md`: exact commands, provenance, and numerical scope.
- `README.md`: this document.


## Compilation

A standard TeX Live or MiKTeX installation with REVTeX 4.2, the AMS packages, `booktabs`, `graphicx`, and `hyperref` is sufficient. The bibliography is embedded and no external figures are needed.

```text
pdflatex r_arun_chandru_transverse_information_in_colliding_layers.tex
pdflatex r_arun_chandru_transverse_information_in_colliding_layers.tex
```

A third run may be useful after reference changes. Alternatively:

```text
tectonic r_arun_chandru_transverse_information_in_colliding_layers.tex
```

Conditional tiny-font fallbacks support an incomplete offline font cache without changing the ordinary definitions on a complete installation. The delivered build uses local Tectonic 0.17.0. The `pdflatex` commands describe the standard alternative, not a separately tested local build.

## Reproducing the finite certificate

Use Python 3.12 and a virtual environment, then from the package folder run:

```text
python -m pip install -r verification/requirements.txt
python verification/verify_circular_counts.py
python verification/verify_circular_counts.py --precision 1152 --output verification/circular_count_certificate_1152.json
```

The verifier constructs rational inputs exactly and evaluates the finite expressions using Arb ball arithmetic through `python-flint`. It checks the required positivity conditions and strict rational upper bounds. Higher precision checks the same expressions, not a different numerical solver.

