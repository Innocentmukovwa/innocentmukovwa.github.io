from flask import Flask, render_template, request, redirect, make_response
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    resp = make_response(render_template("index.html"))
    resp.set_cookie('username', 'email=username')
    return resp


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
            database.write(f"\n{email},{subject},{message}")
            print("Write success!")
    except Exception as e:
        print(f"Error writing to file: {e}")


def write_to_csv(data):
    try:
        with open('database.csv', mode='a',  newline='', encoding='utf-8') as database2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(
                database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            csv_writer.writerow([email, subject, message])
            print("Write success!")
    except Exception as e:
        print(f"Error writing to file: {e}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou")
        except Exception as e:
            print(f"something went wrong{e}")
    else:
        return "something went wrong! Try again."
