from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex_pattern = request.form["regex_pattern"]
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    # Simple email validation regex
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = bool(re.match(regex_pattern, email))
    return {"email": email, "is_valid": is_valid}

if __name__ == '__main__':
    app.run(debug=True)
