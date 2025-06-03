from flask import Flask, render_template, request
import subprocess
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    game_count = 1
    numbers = []

    if request.method == "POST":
        game_count = int(request.form.get("game_count", 1))
        action = request.form.get("action")

        if action == "generate":
            # AI 통합 추천: 하이브리드 + 스마트 중 랜덤 선택
            for _ in range(game_count):
                choice = random.choice(["hybrid_generator.py", "smart_generator.py"])
                output = subprocess.check_output(["python", choice], text=True)
                line = output.strip().split(":")[-1]
                nums = list(map(int, line.strip().split()))
                numbers.append(nums)

    return render_template("index.html", numbers=numbers, game_count=game_count)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)








