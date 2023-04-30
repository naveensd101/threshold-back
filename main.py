# a flask app to implement threshold cryptography scheme

from flask import Flask, request, jsonify
import threshold
import json
import smtplib
from datetime import datetime
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
load_dotenv()

email = os.environ.get('email')
password = os.environ.get('password')

app = Flask(__name__)

app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/encrypt', methods=['POST'])
@cross_origin()
def encrypt():
    data = request.get_json()
    secret_int = data['secret_int']
    num_of_keys = data['num_of_keys']
    min_keys = data['min_keys']
    mail_list = data['mail_list']
    keys = threshold.threshold_enc(secret_int, num_of_keys, min_keys)
    # keys is a dictory of (i, key) pairs
    # we have to mail the keys to the users in the mail_list
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    for idx,i in enumerate(keys):
        #concatinate time to the end of subject
        SUBJECT = "Threshold Cryptography Key Service used at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        body = "Your key pair is: " + str(i) + ", " + str(keys[i])
        message = "Subject: {}\n\n{}".format(SUBJECT, body)
        s.sendmail(email , mail_list[idx], message)

    s.quit()

    return {"data":"OK"}

@app.route('/decrypt', methods=['POST'])
@cross_origin()
def decrypt():
    data = request.get_json()
    # loop through (i, key) pairs and print them
    keys = {}
    for i in data:
        print(i, data[i])
        keys[int(i)] = int(data[i])

    secret_int = threshold.threshold_dec(keys)
    return jsonify(secret_int)

@app.route('/', methods=['GET'])
def hi():
    doc = """
    <h1>Threshold Cryptography Service</h1>
    <pre>
    <code>
    there are two endpoints:
    /encrypt [POST]
    input:
    {
        "secret_int" : 666,
        "num_of_keys" : 3,
        "min_keys" : 2,
        "mail_list": ["example@gmail.com", "example@gmail.com", "example@gmail.com"]
    }
    output: OK
    send email containing the key pair according to threshold scheme
    </code>
    </pre>
    <pre>
    <code>
    /decrypt [POST]
    input:
    {
        "3": 2856086346,
        "1": 952029226
    }
    output:
    value after decryption using threshold cryptography scheme
    </code>
    </pre>
    """
    return doc

if __name__ == '__main__':
    app.run(debug=True)
