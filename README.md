# project35 — Variant 35: Two Random Number Generators

Endterm cross-cutting task: compare generation speed of an array of size 1e6
using the legacy `np.random` interface vs `np.random.default_rng()`.

Topic source: https://github.com/baktybektursunkulov/ProgrammingTechnologies/blob/master/ENDTERM_TOPICS.md

## Weeks

| Week | File | What it produces |
| --- | --- | --- |
| 9  | `week9.py`  | Single timing of `np.random.rand(10**6)` |
| 10 | `week10.py` | Single timing of `default_rng().random(10**6)` |
| 11 | `week11.py` | Two-row table → `outputs/comparison.csv` |
| 12 | `week12.py` | 5 repeats per method, mean → versioned `outputs/results.json` |
| 13 | `week13.py` | Bar chart of means → `outputs/comparison.png` |
| 14 | `week14.py` | Flask `GET /timings` → JSON of averaged times |

Weeks 13 and 14 read the same `outputs/results.json` produced by week 12, so
the chart and the API stay in sync. Re-running week 12 bumps the data; bumping
`Week12.VERSION` flags it as a new version.

## Run

```bash
pip install -r requirements.txt
python main.py            # weeks 9–13
python week14.py          # week 14: serves http://127.0.0.1:5000/timings
```
