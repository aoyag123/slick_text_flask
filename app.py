# Flaskからimportしてflaskを使えるようにする
from flask import Flask, render_template, request,redirect

import sqlite3, datetime, random

# appっていう名前でFlaskアプリを作っていくよ〜みたいな
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return render_template("index.html")



if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを、実行します。
    app.run(debug=True)