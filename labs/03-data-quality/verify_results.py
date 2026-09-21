"""Check the teaching outcomes after executing the notebook."""
import hashlib
import json
from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parent
for filename, digest in json.loads((base / 'data/SHA256SUMS.json').read_text()).items():
    assert hashlib.sha256((base / 'data' / filename).read_bytes()).hexdigest() == digest
result = pd.read_csv(base / 'outputs/comparison.csv', index_col='minute')
assert result['received_rows'].tolist() == [70, 45, 60]
assert result['available_readings'].tolist() == [60, 45, 60]
assert result['coverage_percent'].tolist() == [100, 75, 100]
assert abs(result.loc[1, 'cleaned_mean_bpm'] - result.loc[1, 'reference_mean_bpm']) < 1e-9
assert abs(result.loc[3, 'cleaned_mean_bpm'] - result.loc[3, 'reference_mean_bpm']) < 1e-9
assert (base / 'outputs/comparison.png').stat().st_size > 1000
print('Verified data checksums, duplicate removal, missing coverage, reference agreement and figure output.')
