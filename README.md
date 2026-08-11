# DAA Lab — Design and Analysis of Algorithms

Lab programs implemented in Python.

## Contents

| # | Program | Folder | Technique |
|---|---------|--------|-----------|
| 4 | Factorial (Iterative vs Recursive) with time analysis | `4_Factorial/` | Iteration & Recursion |
| 5 | 0/1 Knapsack Problem | `5_Knapsack/` | Dynamic Programming |
| 6 | Chain Matrix Multiplication | `6_MatrixChainMultiplication/` | Dynamic Programming |
| 7 | Making a Change Problem (Coin Change) | `7_CoinChange/` | Dynamic Programming |

## How to Run

Each program is standalone. Run with Python 3:

```bash
python3 4_Factorial/factorial.py
python3 5_Knapsack/knapsack.py
python3 6_MatrixChainMultiplication/matrix_chain_multiplication.py
python3 7_CoinChange/coin_change.py
```

Each script prompts for input on the console.

## Complexity Summary

| Program | Time Complexity | Space Complexity |
|---|---|---|
| Factorial (Iterative) | O(n) | O(1) |
| Factorial (Recursive) | O(n) | O(n) — call stack |
| 0/1 Knapsack | O(n·W) | O(n·W) |
| Matrix Chain Multiplication | O(n³) | O(n²) |
| Coin Change | O(n·amount) | O(amount) |

## Sample Inputs

**Program 4 — Factorial**
```
Enter a number: 10
```

**Program 5 — Knapsack**
```
Number of items: 4
Weights: 1 3 4 5
Values:  1 4 5 7
Capacity: 7
```

**Program 6 — Matrix Chain Multiplication**
```
Number of matrices: 6
Dimensions: 30 35 15 5 10 20 25
```

**Program 7 — Coin Change**
```
Coins: 1 2 5
Amount: 11
```

## Author

DAA Lab Submission
