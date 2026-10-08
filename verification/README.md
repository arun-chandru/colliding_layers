# Finite-band circular Bose-count verification

This script reproduces the Arb interval-arithmetic certificate in the
finite-band counting appendix of the accompanying manuscript
`r_arun_chandru_transverse_information_in_colliding_layers.tex`.
It checks the stated finite set of angular modes and the declared sorter,
loss, and dark-count bounds.

Use Python 3.12 and install the pinned dependency from this directory:

```console
python -m pip install -r requirements.txt
python verify_circular_counts.py
python verify_circular_counts.py --precision 1152 --output circular_count_certificate_1152.json
```

The first command after installation writes `circular_count_certificate_256.json`
beside the script, independent of the working directory. An explicit `--output`
path is interpreted relative to the working directory. The two included JSON
files were freshly generated using Python 3.12.10 and python-flint 0.9.0.
Every strict inequality assertion passed at both precisions.

The error bounds are false positive below 0.0057, false negative below 0.00072,
and equal-prior error below 0.0032. The certificate also reports measured
occupation bounds and prepared-band quanta and excitation-energy costs.
The exact parameters and model limitations are recorded in each JSON file.

## Provenance and integrity

The audited original was `SGT_CIRCULAR_COUNT_CHECK.py`, source SHA-256
`fc6ebb811aee50ebb9621e43a9a8ec68f2548464fc8620bec09f1d105de7c486`.
The public script removes only the original private `ROOT`/`sys.path`
dependency injection, updates this manuscript reference in the docstring,
and changes the default output filename. Its `rat`, `positive`, and `run`
function syntax trees are exactly unchanged. Parameter and scope payloads
are unchanged.

| Included file | SHA-256 |
| --- | --- |
| `verify_circular_counts.py` | `ca177eaed233a1460c24e4a9ce2f3f8a64f3e619045301ac6f74aff3f1545ad3` |
| `circular_count_certificate_256.json` | `e4aed64286ee1605f08b3119db04de352d1289f93590fac6d35b302d41a9cc37` |
| `circular_count_certificate_1152.json` | `3731cffd810a025673b98ebe6325597398e3191c5e632d26109c5c00555b55f4` |

The original 256-bit certificate SHA-256 was
`d52d9a3f0342e3670cc8aafa68e59f67bee57aabe089711e25f70918affc381d`.
The original independent 1152-bit recheck SHA-256 was
`bf0dc37f62cd641577977e36db3518e8cffaab4d16b5d4a8a435ab2e7a4f65d9`.
The freshly generated JSON payloads match those originals exactly after
excluding the top-level `source_sha256`, which correctly records the public
script hash. There are no numerical or interval-radius differences.

To verify the included hashes, use `sha256sum` on Unix-like systems or
`Get-FileHash -Algorithm SHA256` in PowerShell. A different library release
may print different interval enclosures; the pinned release reproduces the
included outputs.
