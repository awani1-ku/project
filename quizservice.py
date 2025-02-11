
from flask import Flask, request, jsonify
import requests
# Quiz Conducting Service (Microservice 2)
quiz_service = Flask(__name__)

@quiz_service.route("/quiz/submit", methods=["POST"])
def submit_quiz():
    submission = request.json
    questions = requests.get("http://127.0.0.1:8003/questions").json()
    score = sum(1 for q in questions if submission.get(str(q["id"])) == q["answer"])
    return jsonify({"score": score})

if __name__=="__main__":
    quiz_service.run(port=8004)