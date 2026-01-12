from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "Only_For_VidhyaSetu_2025"


# -------------------- BASIC PAGES --------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


# -------------------- AUTHENTICATION --------------------

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login_done", methods=["POST"])
def login_done():
    return redirect(url_for("chat_bot"))


@app.route("/register_done", methods=["POST"])
def register_done():
    mobile = request.form.get("mobile")
    pin = request.form.get("pin")

    # Temporary validation (can replace with DB + Agentic AI later)
    if mobile and pin:
        return redirect(url_for("index"))

    return redirect(url_for("login"))

@app.route("/forget_pwd")
def forget_pwd():
    return render_template("forget_pwd.html")


# -------------------- SECURITY SETUP FLOW --------------------

@app.route("/security_setup_1")
def security_setup_1():
    return render_template("security_setup_1.html")


@app.route("/security_setup_2")
def security_setup_2():
    return render_template("security_setup_2.html")


@app.route("/security_setup_3")
def security_setup_3():
    return render_template("security_setup_3.html")


# -------------------- FEATURES --------------------

@app.route("/chat_bot")
def chat_bot():
    return render_template("chat_bot.html")


@app.route("/legal_law")
def legal_law():
    return render_template("legal_law.html")


# -------------------- FORM ACTION ROUTES --------------------

@app.route("/signup_done", methods=["POST"])
def signup_done():
    return redirect(url_for("security_setup_1"))




# -------------------- RUN APP --------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)
