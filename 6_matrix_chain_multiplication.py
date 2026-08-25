import sys

def matrix_chain_order(p):
    """
    p: list of dimensions where matrix i has dimensions p[i-1] x p[i]
    Returns: minimum number of scalar multiplications, and the DP tables
    """
    n = len(p) - 1  # number of matrices
    
    # dp[i][j] = minimum multiplications to compute product of matrices i..j
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # s[i][j] = index k where optimal split occurs
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # chain_len is the length of the chain being solved
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    
    return dp[1][n], dp, s


def print_optimal_parens(s, i, j):
    """Recursively builds the optimal parenthesization as a string"""
    if i == j:
        return f"M{i}"
    else:
        k = s[i][j]
        left = print_optimal_parens(s, i, k)
        right = print_optimal_parens(s, k + 1, j)
        return f"({left} x {right})"


def main():
    # Example: dimensions of matrices
    # p = [10, 30, 5, 60] means:
    # M1 = 10x30, M2 = 30x5, M3 = 5x60
    p = [10, 30, 5, 60]

    print("Matrix dimensions (p):", p)
    n = len(p) - 1
    for i in range(1, n + 1):
        print(f"M{i}: {p[i-1]} x {p[i]}")

    min_cost, dp, s = matrix_chain_order(p)

    print("\nMinimum number of multiplications:", min_cost)
    print("Optimal Parenthesization:", print_optimal_parens(s, 1, n))

    print("\nDP Table (dp[i][j] = min cost to multiply chain i..j):")
    for row in dp[1:]:
        print(row[1:])


if __name__ == "__main__":
    main()