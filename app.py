from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(f"Name: {name} Email: {email}, Message: {message}")

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
