from flask import Flask, jsonify
import asyncio
import nats
from nats.aio.client import Client as NATS

app = Flask(__name__)
nc = NATS()

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"Message": "How you doin'"})
def receive_request():
    data = request.data
    nc.publish("nginx_requests", data)
    return "Request received and sent to NATS Server", 200

if __name__ == '__main__':
    nc.connect(servers=["nats://nats.svc:4222"])
    app.run(host="0.0.0.0", port=5000)