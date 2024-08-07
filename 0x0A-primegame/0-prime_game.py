#!/usr/bin/python3
"""Prime Game Solution
"""


def sieve_of_eratosthenes(max_num):
    """Generate a list of primes up to max_num using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for multiple in range(p * p, max_num + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


def play_game(n, primes):
    """Simulate the game for a given n using the list of primes and\
       return the winner."""
    remaining = set(range(1, n + 1))
    current_player = 'Maria'

    while True:
        prime_found = False
        for prime in primes:
            if prime in remaining:
                prime_found = True
                to_remove = set(range(prime, n + 1, prime))
                remaining -= to_remove
                break

        if not prime_found:
            return 'Ben' if current_player == 'Maria' else 'Maria'

        current_player = 'Ben' if current_player == 'Maria' else 'Maria'


def isWinner(x, nums):
    """Determine the player who won the most rounds."""
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        winner = play_game(num, primes)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
