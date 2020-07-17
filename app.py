from flask import Flask, render_template, request

import functii
import trainerEng

app = Flask(__name__)

@app.route("/")
def home():
    cv = request.args.get('msg')
    #messages = Message.query.order_by(Message.id.desc()).all()
    return render_template("index.html", cv=cv)

@app.route("/detectare")
def detect_referinte():
    userText = request.args.get('msg')
    if userText.lower() == "q":
        return 'Deci, ai cam văzut cum stau lucrurile. ' \
               'Am detectat referințe. A fost o conversație ciudată. Îmi pare bine că te-am cunoscut. ' \
               'Acum, am de lucru. Ne mai vedem. Dacă mai ai întrebări, nelămuriri, te rog sa revii.' \
               'Pa!'
    return functii.referinte(userText)

@app.route("/name", methods=["GET"])
def name():
    userText = request.args.get('msg')
    return functii.nume(userText)
#render_template('nimic.html', userText=userText)

@app.route("/discut")
def dialog():
    userText = request.args.get('msg')
    return functii.convorbireIT(userText)

@app.route("/discut_modif")
def dialogRef():
    userText = request.args.get('msg')
    return functii.convorbireREF(userText)

@app.route("/ceva", methods=["GET"])
def ceva():
    cv = request.args.get('msg')
    return render_template("index.html", cv=cv)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText.lower() == "exit":
        return 'Deci, ai cam văzut cum stau lucrurile. ' \
               'Nu sunt prea bun la recunoașterea termenilor. A fost o conversație ciudată. Îmi pare bine că te-am cunoscut. ' \
               'Acum, am de lucru. Ne mai vedem. Dacă mai ai întrebări, nelămuriri, te rog sa revii.' \
               'Pa!'
    return str(trainerEng.english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()