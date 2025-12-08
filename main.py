import sqlite3, os, hashlib
from flask import Flask, jsonify, render_template, request, g

app = Flask__name__
app.database = sample.db

@app.route/
def index:
    return render_templateindex.html

@app.route/login
def login:
    return render_templatelogin.html

@app.route/restock
def restock:
    return render_templaterestock.html

#API routes
@app.route/api/v1.0/storeLoginAPI/, methods=POST
def loginAPI:
    if request.method == POST:
        # Mo