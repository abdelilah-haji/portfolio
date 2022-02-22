import email
from email import message
from lib2to3.pgen2.token import NEWLINE
from statistics import mode
from unicodedata import name
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return "Ca n'arrive pas a etre enregistre dans la base de donnees"
    else:
        return "Erreur! Renvoyez votre message s'il vous plait"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database2, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])
