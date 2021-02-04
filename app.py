from flask import Flask

app = Flask(__name__)

from flask import render_template
@app.route('/')
def hello():
    return render_template("parent.htm")

@app.route('/mypage/me')
def about_me():
    return render_template("O_mnie.htm")

@app.route('/mypage/contact')
def kontakt():
    return render_template("Contact.htm")

from flask import request, redirect

@app.route('/message', methods=['POST'])
def message():
    print(request.form)
    return redirect("/message")