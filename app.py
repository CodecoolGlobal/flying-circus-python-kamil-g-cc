from flask import Flask, make_response, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "moj sekretny klucz"

@app.route('/')
def index():

    ile_razy = session.get('ktory_raz_jestem', default=1)
    session['ktory_raz_jestem'] = ile_razy + 1

    response = make_response(render_template("index.html", visits = ile_razy))
    response.set_cookie('kamil_ciasteczko', value="bylem tutaj, Tony Halik")

    return response

@app.route('/login', methods=["POST", "GET"])
def login():
    correct_user = False

    if request.method == "POST":
        # zweryfikowac dane z formularza
        if correct_user:
            return redirect("/")
        else:
            return render_template("error.html")
    else:
        return render_template("login.html")