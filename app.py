from flask import Flask, render_template, request

app = Flask(__name__)

# 등급 계산 함수
def c_grade(rank, total):
    percentage = (rank / total) * 100

    if percentage <= 4.0:
        return 1
    elif percentage <= 11.0:
        return 2
    elif percentage <= 23.0:
        return 3
    elif percentage <= 40.0:
        return 4
    elif percentage <= 60.0:
        return 5
    elif percentage <= 77.0:
        return 6
    elif percentage <= 89.0:
        return 7
    elif percentage <= 96.0:
        return 8
    else:
        return 9

# 기본 페이지
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 폼 데이터 받기
        subject = request.form.get("subject")
        total = int(request.form.get("total"))
        rank = int(request.form.get("rank"))

        # 등급 계산
        grade = c_grade(rank, total)

        # 결과 반환
        return render_template("index.html", grade=grade, subject=subject, total=total, rank=rank)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
