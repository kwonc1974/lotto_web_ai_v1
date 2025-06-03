import random
from lotto_data import get_recent_lotto_numbers

def ai_recommend_numbers():
    recent_numbers = get_recent_lotto_numbers(5)

    # 자주 나온 번호 뽑기
    flat_list = [num for draw in recent_numbers for num in draw]
    frequency = {}
    for num in flat_list:
        frequency[num] = frequency.get(num, 0) + 1
    popular_numbers = sorted(frequency, key=frequency.get, reverse=True)[:15]

    # 랜덤 번호 뽑기
    random_pool = list(set(range(1, 46)) - set(popular_numbers))
    random_numbers = random.sample(random_pool, 15)

    # 두 개를 섞은 뒤 6개 추출
    hybrid_pool = list(set(popular_numbers + random_numbers))
    final_numbers = random.sample(hybrid_pool, 6)
    return sorted(final_numbers)

# 테스트용 출력
if __name__ == "__main__":
    for _ in range(3):  # 예시로 3게임 출력
        print(ai_recommend_numbers())
