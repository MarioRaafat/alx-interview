def sieve_of_eratosthenes(n):
    """Helper function to generate prime numbers up to n using Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False
    return primes

def isWinner(x, nums):
    if not nums or x < 0:
        return None

    MariaRounds = BenRounds = 0
    for num in nums:
        if num < 2:
            BenRounds += 1
            continue

        prime_nums = sieve_of_eratosthenes(num)
        prime_count = sum(prime_nums)
        print("prime_count", prime_count)
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