from flask import Flask, make_response, render_template, session

app = Flask(__name__)
app.secret_key = "moj sekretny klucz"

@app.route('/')
def index():

    ile_razy = session.get('ktory_raz_jestem', default=1)
    session['ktory_raz_jestem'] = ile_razy + 1

    response = make_response(render_template("index.html", visits = ile_razy))
    response.set_cookie('kamil_ciasteczko', value="bylem tutaj, Tony Halik")

    return response