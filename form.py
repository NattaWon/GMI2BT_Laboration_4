from flask import Flask, render_template, request, Response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/postjson', methods=['POST'])
def printjson():
    print(request)
    form_info = request.form  # dict från form
    formatted_info = f'Firstname: {form_info["firstName"]}Lastname: {form_info["lastName"]} Address: {form_info["adress"]} Zipcode, City: {form_info["zipcode"]} \nEmail: {form_info["email"]} '
    return formatted_info

if __name__ == "__main__":
    app.run(debug=True)
