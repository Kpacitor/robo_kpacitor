#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('robo_kpacitor.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
