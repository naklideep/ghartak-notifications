from flask import Flask, request, jsonify
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
CORS(app)

# Fix the private key newlines getting escaped
cred_json = json.loads(os.environ.get("FIREBASE_CREDENTIALS"))
cred_json['private_key'] = cred_json['private_key'].replace('\\n', '\n')
cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "GharTak Notification Server Running!"})

@app.route("/send-notification", methods=["POST"])
def send_notification():
    try:
        data = request.get_json()

        token = data.get("token")
        title = data.get("title")
        body = data.get("body")
        extra = data.get("data", {})

        if not token or not title or not body:
            return jsonify({"error": "token, title, body are required"}), 400

        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=extra,
            token=token,
        )

        response = messaging.send(message)
        return jsonify({"success": True, "message_id": response}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



# rest of the code stays exactly the same...