from lotto_data import get_recent_lotto_numbers
import random

def generate_hybrid_numbers():
    recent = get_recent_lotto_numbers()
    recent_flat = sorted(set(num for sub in recent for num in sub))
    numbers = []

    while len(numbers) < 6:
        if random.random() < 0.5:
            num = random.choice(recent_flat)
        else:
            num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    numbers.sort()
    return numbers

if __name__ == "__main__":
    print(generate_hybrid_numbers())


