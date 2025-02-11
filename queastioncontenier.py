from flask import Flask, request, render_template

app = Flask(__name__)

# Store questions in a simple list (temporary storage)
questions = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            questions.append(question)  # Add question to the list
    return render_template("index.html", questions=questions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
