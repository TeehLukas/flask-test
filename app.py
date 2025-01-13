from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

def bye():
    print("Bye!")


if __name__ == '__main__':
    app.run(debug=True)



