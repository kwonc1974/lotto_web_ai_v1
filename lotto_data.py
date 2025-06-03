# lotto_data.py

import requests
from bs4 import BeautifulSoup

def get_recent_lotto_numbers(weeks=5):
    result = []
    for i in range(weeks):
        draw_no = get_latest_draw_no() - i
        url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={draw_no}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        numbers = soup.select(".win span.ball_645")
        nums = [int(n.text) for n in numbers[:6]]
        result.append(nums)
    return result

def get_latest_draw_no():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    draw_text = soup.select_one(".win_result h4 strong").text.strip()
    return int(draw_text.replace("제 ", "").replace("회", ""))

if __name__ == "__main__":
    data = get_recent_lotto_numbers()
    for week in data:
        print(week)
