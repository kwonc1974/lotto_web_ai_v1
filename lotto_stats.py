import requests
from bs4 import BeautifulSoup
from collections import Counter

def get_lotto_numbers(draw_no):
    url = f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={draw_no}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    win_numbers = soup.select_one(".nums").text.strip().split("\n")
    numbers = [int(num.strip()) for num in win_numbers if num.strip().isdigit()]
    return numbers[:6]

def get_recent_top_numbers(n=5):
    latest = 1120  # 최근 회차로 임시 지정 (자동화 예정)
    all_numbers = []

    for i in range(latest, latest - n, -1):
        nums = get_lotto_numbers(i)
        all_numbers.extend(nums)

    count = Counter(all_numbers)
    top = count.most_common()
    return top

if __name__ == "__main__":
    stats = get_recent_top_numbers()
    print("📊 최근 5주간 번호 등장 순위:")
    for num, cnt in stats:
        print(f"{num}번: {cnt}회")
