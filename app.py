from flask import Flask, render_template, request
import random
import subprocess

app = Flask(__name__)

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    game_count = 1
    if request.method == "POST":
        action = request.form.get("action")
        game_count = int(request.form.get("count", 1))
        
        if action == "generate":
            # AI 통합 추천: 하이브리드 + 스마트 중 랜덤 선택
            for _ in range(game_count):
                choice = random.choice(["hybrid_generator.py", "smart_generator.py"])
                output = subprocess.check_output(["python", choice], text=True)
                line = output.strip().split(":")[-1]
                result.append(line)

        elif action == "clear":
            result = []

    return render_template("index.html", result=result, game_count=game_count)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)








