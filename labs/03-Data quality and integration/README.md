# Lab 03 — Data quality and integration

We use a short heart-rate recording to find duplicates and missing readings. We then compare the average with the number of readings behind it.

## Before the lab

Read the notebook introduction and data description. The recording contains one heart-rate reading per second, so a complete minute contains 60 readings.

Write a short prediction: **Can a plausible average heart rate hide missing or duplicated readings? What would you check alongside the average?** Bring your answer to the lab; no separate submission is required.

## During the lab

1. Run the guided notebook and inspect the received readings.
2. Compare the average and reading count for each minute.
3. Remove repeated timestamps and check the counts again.
4. Explain why removing duplicates does not recover missing observations.
5. Compare the evidence with your initial prediction and discuss it with the instructor.

## After the lab

Use the separate optional Data quality exercise to compare completeness thresholds of 54 and 60 readings per minute. Save your table and explanation in your notebook. Bring questions to the next lab or post them in the course discussion forum when available.

**Self-check:** after duplicate removal, the three minutes contain 60, 45 and 60 readings. Explain why the middle minute has 75% coverage and why its average alone is insufficient to judge data completeness.

## Materials

- [Notebook](03_data_quality.ipynb)
- [Optional exercise](exercise-03-data-quality.md)
- [Data sources and preprocessing](data/README.md)
- [Docker setup](../../docs/container-release.md)

Start the environment from the repository root with
`docker compose -f compose.release.yaml up -d`. Use
`docker compose -f compose.release.yaml logs lab` to find the Jupyter login URL,
then open the notebook in this folder and run the cells in order.

The notebook saves `outputs/comparison.png` and `outputs/comparison.csv`.
