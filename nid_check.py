#python 3.7.9

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def nid():
    return render_template("nid-form.html")

@app.route('/nid-data', methods = ['POST', 'GET'])
def nid_data():
    if request.method == 'GET':
        return f"The URL /nid-data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        req_data = {
        # "mobile" : form_data['mobile'],
        "nid" : form_data['nid'],
        "dob" : form_data['dob']
        }
        res = requests.post('https://ldtax.gov.bd/citizen/nidCheck/', data = req_data, verify=False)
        a = res.json()
        data = a['data']
        return render_template("nid-data.html", data = data)
     

if __name__ == '__main__':
    app.run(debug=True)