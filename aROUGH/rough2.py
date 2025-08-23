def naive_poly_mult(P, Q):
    n = max(len(P), len(Q))

    # Base case: single coefficient
    if n == 1:
        return [P[0] * Q[0]]

    # Pad both polynomials to length n (power of 2 helps)
    while len(P) < n:
        P.append(0)
    while len(Q) < n:
        Q.append(0)

    m = n // 2

    # Split
    P_low, P_high = P[:m], P[m:]
    Q_low, Q_high = Q[:m], Q[m:]

    # Recursive multiplications
    L = naive_poly_mult(P_low, Q_low)
    H = naive_poly_mult(P_high, Q_high)
    M1 = naive_poly_mult(P_low, Q_high)
    M2 = naive_poly_mult(P_high, Q_low)

    # Allocate result (size 2n-1)
    result = [0] * (2 * n - 1)

    # Add L
    for i in range(len(L)):
        result[i] += L[i]

    # Add M1+M2 shifted by m
    for i in range(len(M1)):
        result[i + m] += M1[i]
    for i in range(len(M2)):
        result[i + m] += M2[i]

    # Add H shifted by 2m
    for i in range(len(H)):
        result[i + 2*m] += H[i]

    return result
