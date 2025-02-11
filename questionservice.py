from flask import Flask, request, jsonify
import requests

# Question Paper Service (Microservice 1)
question_service = Flask(__name__)

@question_service.route("/questions", methods=["GET"])
def get_questions():
    questions = [
        {"id": 1, "question": "What is Python?", "answer": "Programming Language"},
        {"id": 2, "question": "What is Flask?", "answer": "Web Framework"}
    ]
    return jsonify(questions)
    

if __name__=="__main__":
    question_service.run(host="0.0.0.0", port=8003)