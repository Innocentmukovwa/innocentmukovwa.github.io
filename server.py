from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/about_me")
def about():
    return render_template("about.html")


@app.route("/works")
def my_work():
    return render_template("works.html")


@app.route("/contacts")
def contctsa():
    return render_template("contact.html")


@app.route("/components")
def compontne():
    return render_template("components.html")


@app.route("/thankyou")
def thank():
    return render_template("thankyou.html")


def write_to_file(data):
    try:
        with open('database.txt', mode='a') as database:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            database.write(f'\n{email},{subject},{message}')
            print("Write success!")
    except Exception as e:
        print(f"Error writing to file: {e}")

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        print()
        return redirect("/thankyou")
    else:
        return "something went wrong"
