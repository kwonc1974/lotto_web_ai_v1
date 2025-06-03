import random

# 최근 5주간 자주 등장한 번호 (예시)
HOT_NUMBERS = [3, 7, 11, 23, 28, 35, 42, 44]
# 잘 안 나오는 번호 (예시)
COLD_NUMBERS = [1, 2, 4, 6, 14, 17, 31, 39]

def generate_ai_lotto():
    selected = set()

    weighted_numbers = []
    for n in range(1, 46):
        score = 1
        if n in HOT_NUMBERS:
            score += 5
        if n in COLD_NUMBERS:
            score -= 1
        weighted_numbers.extend([n] * score)

    while len(selected) < 6:
        pick = random.choice(weighted_numbers)
        if pick not in selected:
            selected.add(pick)

    # 구간 안배: 10단위 구간 최소 3개 포함되게 조정
    while True:
        sections = {n // 10 for n in selected}
        if len(sections) >= 3:
            break
        selected = set(random.sample(weighted_numbers, 6))

    return sorted(selected)
