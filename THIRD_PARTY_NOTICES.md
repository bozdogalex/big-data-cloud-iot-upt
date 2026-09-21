# Third-party materials

## BIDMC physiological measurements

The source recording and teaching excerpts in `labs/03-Data quality and integration/data/`
come from the BIDMC PPG and Respiration Dataset v1.0.0 on PhysioNet.
The data use the **Open Data Commons Attribution License v1.0**.
The original licence is preserved in that directory as `LICENSE.txt`.
The accompanying `README.md` records attribution, source URLs and the deliberate
teaching transformations. Data-derived notebook outputs remain subject to the
source data's applicable attribution requirements.

## Container and dependencies

The Python/Debian base image and installed Python packages retain their own
licences. The project's MIT and CC BY 4.0 grants cover only original project
materials; they do not relicense bundled third-party software or data.
The base image digest is in `Dockerfile`; Python versions are recorded in
`requirements-lock.txt`. Installed package metadata and system copyright
notices remain available inside the image.
