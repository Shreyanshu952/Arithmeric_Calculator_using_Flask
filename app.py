# Testing  an arithmetic calculator API using flask and postman

from flask import Flask, request, jsonify
import json

# create an object for class Flask

app = Flask(__name__)

@app.route("/")
def HomePage():
    return "This is the home page of the designed calculator"

@app.route("/calculate", methods = ["GET"])
def Calculator():

    '''
    For requesting data or inputs from postman we pass the request in the form of json
    '''

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

    #return jsonify(result)

    '''
    we can return the result without using jsonify as well. Written below
    '''

    return f"The operation is {operation} and the result is {result}"

if __name__=="__main__":
    app.run(port = 81, debug=True)