from flask import Flask,request
from operations import add, sub, mult, div

app = Flask (__name__)


@app.route('/add')
def addition():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return str(f"Addition = {result}")


@app.route('/sub')
def subtraction():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)
    return str(f"Subtraction = {result}")


@app.route('/mult')
def multiplication():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return str(f'Multiplication = {result}')


@app.route('/div')
def division():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)
    return str(f'Division = {result}')




@app.route('/math/<operations>')
def math_operation(operations):
    a = int(request.args["a"])
    b = int(request.args["b"])
    math = oper[operations](a,b)

    return str(math)

