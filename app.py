from flask import Flask
import os
import random
import time

app = Flask(__name__)

@app.route("/")
def hello():
    delay = random.uniform(0.3, 0.7)
    time.sleep(delay)

    # Respond with a JSON message
    response = {"message": "Hello, world!"}
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
