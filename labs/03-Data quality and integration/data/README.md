# Heart-rate data provenance

The source file is the unmodified `bidmc_01_Numerics.csv` from the **BIDMC PPG and Respiration Dataset v1.0.0**, by Marco Pimentel, Alistair Johnson, Peter Charlton and David Clifton.

- Dataset: https://physionet.org/content/bidmc/1.0.0/
- Source file: https://physionet.org/files/bidmc/1.0.0/bidmc_csv/bidmc_01_Numerics.csv
- DOI: https://doi.org/10.13026/C2208R
- Downloaded: 15 September 2026.
- The dataset page specifies Open Data Commons Attribution License v1.0: https://opendatacommons.org/licenses/by/1-0/
- The source distribution's licence notice is preserved in `LICENSE.txt`.

This teaching excerpt contains information from BIDMC, made available under the Open Data Commons Attribution License. Dataset rights remain with the original providers; this notice does not license unrelated repository code.

## Teaching transformations

`reference.csv` retains elapsed seconds 0–179 and the HR column, renamed `elapsed_seconds` and `heart_rate_bpm`. The monitor-derived HR measurements are sampled once per second. No calendar timestamp is invented.

`received.csv` removes seconds 75–89 and repeats seconds 20–29 once. These changes simulate ingestion defects; they are not defects attributed to the source dataset. There are 175 received rows, 165 unique timestamps and 15 absent timestamps. Missing observations are left missing rather than interpolated.

Regenerate these files using `python scripts/build_materials.py` from the repository root. `SHA256SUMS.json` records checksums of the source and derived CSVs. The unmodified excerpt is an experimental reference, not clinical ground truth.

## Citations

Pimentel et al. *Towards a Robust Estimation of Respiratory Rate from Pulse Oximeters*. IEEE Transactions on Biomedical Engineering, 64(8), 1914–1923. DOI: https://doi.org/10.1109/TBME.2016.2613124

Pollard et al. (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: https://doi.org/10.1038/s44360-026-00096-z
