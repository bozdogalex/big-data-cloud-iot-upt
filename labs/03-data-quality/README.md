# Lab 03 — Data quality

Open `03_data_quality.ipynb` and run the cells in order. We use a short heart-rate recording with deliberately repeated and missing messages. The data is included, so you do not need to download anything or use a cloud account.

The optional exercise compares two thresholds for flagging incomplete minutes. Save your results and explain what the check tells you.

From the repository root, run `docker compose -f compose.release.yaml up -d`, then `docker compose -f compose.release.yaml logs lab` to find the Jupyter login URL. Open it and navigate to `labs/03-data-quality/03_data_quality.ipynb`.

The notebook saves `outputs/comparison.png` and `outputs/comparison.csv`. See `data/README.md` for source attribution and modifications.
