from ast import Return
import imp
from flask import Flask,render_template,redirect, request
app= Flask(__name__)
from sundaes import Sundae


@app.route('/')
def index():
    all_sundaes = Sundae.get_all()
    print(all_sundaes)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)