from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask("mongoapp")

client = MongoClient("mongodb://127.0.0.1:27017")


@app.route("/web")
def webForm():
    return render_template("form.html")


@app.route("/mongodb", methods=['GET'])
def getValue():
    if request.method == 'GET':
        sname = request.args.get('sname')
        email = request.args.get('email')
        add = request.args.get('add')
        mobile = request.args.get('mobile')
        classs = request.args.get('class')
        client['library']['student'].insert_one(
            {"name": sname, "email": email, "mobile": mobile, "address": add, "class": classs})
        return render_template("response.html")
    else:
        return ("Invalid Method")


@app.route("/info")
def infoReturn():
    return render_template("info.html")


@app.route("/read", methods=['GET'])
def readData():
    cinfo = client['library']['student'].find()
    return render_template('display-stud.html', cinfo=cinfo)


app.run(host='0.0.0.0', debug=True)
