# 💓 HeartCheck

A Python desktop app that guides you through the Ruffier-Dickson fitness test and calculates your cardiovascular health score.

## Features

- Step-by-step guided test flow with instructions
- Built-in stopwatch for timing pulse measurements
- Squat counter for the exercise phase
- Calculates the **Ruffier Index**: `(P1 + P2 + P3 − 200) / 10`
- Age-adjusted fitness rating (5 levels: Excellent → Poor)
- Input validation with descriptive error messages
- Clean dark-themed UI built with `tkinter`

## Test Protocol

The app follows the standard Ruffier-Dickson test:

```
1. Sit quietly → measure resting pulse for 15 seconds (P1)
2. Perform 30 squats in 45 seconds
3. Immediately after → measure pulse for 15 seconds (P2)
4. Wait 45 seconds → measure pulse again for 15 seconds (P3)
```

## Fitness Ratings

| Ruffier Index | Rating        |
|---------------|---------------|
| < 3           | Excellent      |
| 3 – 5.9       | Good           |
| 6 – 9.9       | Average        |
| 10 – 14.9     | Below Average  |
| ≥ 15          | Poor           |

*Thresholds are adjusted based on age group (<30, 30–49, 50+).*

## Usage

1. Clone the repo:

```bash
git clone https://github.com/pregiorg/Heart_Check.git
cd heartcheck
```

2. Run the app:

```bash
python heartcheck.py
```

## Requirements

- Python 3.x
- No external libraries — uses `tkinter` from the standard library

## Screenshots

*Coming soon*

## What I Learned

- Building multi-screen GUI apps with `tkinter`
- Managing widget lifecycle with `winfo_children()` and `.destroy()`
- Implementing a stopwatch using `root.after()` and cancellable callbacks
- Organising a class-based tkinter app with clear state management
- Input validation and user-friendly error handling with `messagebox`

## License

MIT
