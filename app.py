import bcrypt
from flask import Flask, make_response, render_template, session, request, redirect
from data import users

app = Flask(__name__)
app.secret_key = "moj sekretny klucz"

@app.route('/')
def index():

    ile_razy = session.get('ktory_raz_jestem', default=1)
    session['ktory_raz_jestem'] = ile_razy + 1

    response = make_response(render_template("index.html", visits = ile_razy))
    response.set_cookie('kamil_ciasteczko', value="bylem tutaj, Tony Halik")

    return response

def check_credentials(login, password):
    INVALID = -1
    hash_in_hex = users.get(login, INVALID)
    if hash_in_hex == INVALID:
        return False
    hash_in_bytes = bytes.fromhex(hash_in_hex)

    return bcrypt.checkpw(password.encode('utf-8'), hash_in_bytes)

@app.route('/login', methods=["POST", "GET"])
def login():
    correct_user = False

    if request.method == "POST":
        login = request.form.get(key="email")
        password = request.form.get(key="password")
        correct_user = check_credentials(login, password)
        if correct_user:
            return redirect("/")
        else:
            return render_template("error.html")
    else:
        return render_template("login.html")