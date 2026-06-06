from flask import Flask, request, jsonify

app = Flask(_name_)

allowed_devices = set()

@app.route("/")
def home():
    return "License Server Running"

@app.route("/check", methods=["POST"])
def check():
    hwid = request.json.get("hwid")
    return jsonify({"allowed": hwid in allowed_devices})

@app.route("/activate", methods=["POST"])
def activate():
    hwid = request.json.get("hwid")
    allowed_devices.add(hwid)
    return jsonify({"status": "activated"})

@app.route("/block", methods=["POST"])
def block():
    hwid = request.json.get("hwid")
    allowed_devices.discard(hwid)
    return jsonify({"status": "blocked"})
