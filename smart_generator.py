import random
from lotto_data import get_recent_lotto_numbers

def get_smart_numbers():
    # 최근 5주간 번호 가져오기
    recent_numbers = get_recent_lotto_numbers()

    # 출현 횟수 세기
    number_counts = {}
    for round_nums in recent_numbers:
        for num in round_nums:
            number_counts[num] = number_counts.get(num, 0) + 1

    # 가장 자주 나온 상위 20개 숫자 추리기
    sorted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)
    top_20 = [num for num, count in sorted_numbers[:20]]

    # top_20에서 4개, 나머지(1~45 중 top_20 제외)에서 2개 선택 (하이브리드 방식)
    others = [num for num in range(1, 46) if num not in top_20]

    result = random.sample(top_20, 4) + random.sample(others, 2)
    return sorted(result)

if __name__ == "__main__":
    print(get_smart_numbers())

