from flask import Flask, render_template, request
import smtplib


# MY_MAIL = "saifiaryan208@gmail.com"
# MY_PASSWORD = "jtqhsdbswtmzoohz"

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index_page():
    if request.method == "POST":
        name = request.form['visitingPerson']
        send_mail(name)
        return render_template("home.html")
    return render_template("index.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/resume")
def resume_page():
    return render_template("resume.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == "POST":
        name = request.form['Username']
        mail = request.form['Email']
        subject = request.form['Subject']
        message = request.form['Message']
        send_mail(name, mail, subject, message)
    return render_template("contact.html")

def send_mail(*args):
    count = 0
    for item in args:
        with open("data.txt", mode="a") as file:
            if len(args) == 1:
                file.write(f"Subject:Hello, this mail is sent by your portfolio for track of Visitor.\n\nName: {args[0]}")
            else:
                count += 1
                if count == 3:
                    file.write(f"Name: {args[0]}\nEmail: {args[1]}\nSubject: {args[2]}\nMessage: {args[3]}")
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=MY_MAIL, password=MY_PASSWORD)
        #     if len(args) == 1:
        #         connection.sendmail(
        #             from_addr=MY_MAIL,
        #             to_addrs="phadse04@gmail.com",
        #             msg=f"Subject:Hello, this mail is sent by your portfolio for track of Visitor.\n\nName: {args[0]}")
        #     else:
        #         count += 1
        #         if count == 3:
        #             connection.sendmail(
        #                 from_addr=MY_MAIL,
        #                 to_addrs="phadse04@gmail.com",
        #                 msg=f"Subject:Hello, this mail is sent by your Portfolio.\n\nThere is a message from a user visited your portfolio.\n\n"
        #                     f"Name: {args[0]}\nEmail: {args[1]}\nSubject: {args[2]}\nMessage: {args[3]}")

if __name__ == "__main__":
    app.run(debug=True)