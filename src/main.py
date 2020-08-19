from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3

from src.services.shortenlink import shortenlink
from src.services.findlink import findlink

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("main/index.html")

@app.route("/url", methods=["POST", "GET"])
def url():
	if request.method == "POST":
		url = request.form.get("url")
		shorten = request.form.get("shorten")
		result = shortenlink(url, shorten)
		return jsonify(result)
	else:
		return redirect(url_for("index"))

@app.route("/link/<shorten>")
def link(shorten):
	link = findlink(shorten)
	if link:
		return redirect(link)
	else:
		return jsonify({ "msg" : "not found" })

@app.route("/list")
def list():
	try:
		with sqlite3.connect("database.db") as conn:
			conn.row_factory = sqlite3.Row
			cur = conn.cursor()
			cur.execute("SELECT * FROM links")
			rows = cur.fetchall()
			msg = "Select successfully"
	except:
		result = []
		msg = "Error in select operation"
	finally:
		result = [dict(row) for row in rows]
		return jsonify({ 
			"data" : result,
			"msg" : msg 
		})
		conn.close()