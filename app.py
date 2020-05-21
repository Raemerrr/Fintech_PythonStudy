from flask import Flask, jsonify, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite3"
app.secret_key = "fintech"


db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.String(50),primary_key=True)
    pw = db.Column(db.String(50))


@app.route("/")
def main():
    return jsonify({"name":"raemin"})

@app.route("/<name>")
def myName(name):
    return name

@app.route("/num/<int:num>")
def myNum(num):
    myDan = ""
    for i in range(1,10):
        myDan += "%d * %d = %d</br>"%(num,i,num*i)
    return myDan

with open("stocklist.json","r") as JSON:
    myJSON = json.load(JSON)

@app.route("/stock")
def stock():
    return jsonify(myJSON)

@app.route("/rank")
def rank():
    mySort = []
    for k in myJSON.keys():
        mySort.append([k,myJSON[k]["rank"]])
    mySort.sort(key=lambda x: x[1])
    return mySort

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        if not 'user-id' in session.keys():
            return render_template('signup.html')
        else:
            return render_template('welcome.html',user=session['user-id'])
    else:
        form_dic=request.form.to_dict(flat=True)
        user = User.query.filter_by(id=form_dic['user-id']).first()
        if user != None and user.pw==form_dic['user-pw']:
            session['user-id'] = user.id
            return render_template('welcome.html',user=form_dic['user-id'])
        return "아이디나 비밀번호가 틀렸습니다."

#templates
@app.route("/hello")
def hello():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)