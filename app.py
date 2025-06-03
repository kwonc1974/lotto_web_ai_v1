from flask import Flask, render_template, request
import subprocess
import random

app = Flask(__name__)

def run_generator(script, game_count):
    results = []
    for _ in range(game_count):
        output = subprocess.check_output(["python", script], text=True)
        numbers_line = output.strip().split(":")[-1]
        numbers = numbers_line.strip("[] \n").split(", ")
        numbers = [int(n) for n in numbers if n.isdigit()]
        results.append(numbers)
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    numbers_list = []
    game_count = 1

    if request.method == "POST":
        try:
            game_count = int(request.form.get("game_count", 1))
        except:
            game_count = 1

        action = request.form.get("action")

        if action == "generate":
            # AI 통합 추천: 하이브리드 + 스마트 중 랜덤 선택
            for _ in range(game_count):
                choice = random.choice(["hybrid_generator.py", "smart_generator.py"])
                output = subprocess.check_output(["python", choice], text=True)
                line = output.strip().split(":")[-1]
                nums = line.strip("[] \n").split(", ")
                nums = [int(n) for n in nums if n.isdigit()]
                numbers_list.append(nums)

        elif action == "reset":
            numbers_list = []

    return render_template("index.html", numbers_list=numbers_list, game_count=game_count)

if __name__ == "__main__":
    app.run(debug=True)







