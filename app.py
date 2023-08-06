# creating an arithmetic calculator using flask and postman

from flask import Flask, request, render_template

# create an object for class Flask

app = Flask(__name__)

@app.route("/")
def HomePage():
    return "This is the home page of the designed calculator"

@app.route("/calculate", methods = ["GET"])
def Calculator():
    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["numnber2"]

    if operation == "add":
        result = int(number1) + int(number2)
    elif operation == "subtract":
        result = int(number1) - int(number2)
    elif operation == "multiply":
        result = int(number1) * int(number2)
    elif operation == "divide":
        result = int(number1) / int(number2)
    else:
        result = int(number1) ** int(number2)
    return result

if __name__=="__main__":
    app.run(debug=True)