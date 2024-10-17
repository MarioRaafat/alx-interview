#!/usr/bin/python3

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if not nums or x < 0:
        return None

    MariaRounds = BenRounds = 0
    for num in nums:
        if num < 2:
            BenRounds += 1
            continue

        primes = [True] * (num + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(num**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, num + 1, i):
                    primes[multiple] = False
        prime_count = sum(primes)
        if prime_count % 2 == 0:
            BenRounds += 1
        else:
            MariaRounds += 1

    if MariaRounds > BenRounds:
        return "Maria"
    elif MariaRounds < BenRounds:
        return "Ben"
    else:
        return None
