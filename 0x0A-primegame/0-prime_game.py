#!/usr/bin/python3
"""
This module returns the winner of a PrimeNumber game.
"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_round(n):
    """Play a single round of the game.
    Returns True if Maria wins, False if Ben wins.
    """
    # Create a set of available numbers
    available = set(range(1, n + 1))

    # Track current player (True for Maria, False for Ben)
    maria_turn = True

    while True:
        # Find available primes
        primes = [p for p in available if is_prime(p)]

        # If no primes available, current player loses
        if not primes:
            return not maria_turn

        # Choose the smallest prime
        prime = min(primes)

        # Remove the prime and its multiples
        available = {num for num in available if num % prime != 0}

        # Switch turns
        maria_turn = not maria_turn


def isWinner(x, nums):
    """Determine the overall winner across x rounds."""
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
