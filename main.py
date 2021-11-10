from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        name = request.form.get("your-name")
        return f"Hello {name}!"


print("It works!")


# This is just a regular way to run a Python file safely.
if __name__ == '__main__':
    app.run()
