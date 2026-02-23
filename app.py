from flask import Flask, request, jsonify
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
CORS(app)


from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, messaging
import os

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "riyal1-c9fe9",
  "private_key_id": "e70fac0dd5a1d0131a57093d8dc8f2f4551b2182",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtZj96+1b9szD9\nrh4WOyLnjxGocR6PVGl1zOVlvb0BhyFR+Y3NnGtaLB9ZpCqU116j4wyhqk7vWt+m\nPDRfQi1/qlcq/esuKe0vPqmZB4706gxHBiGcHioBVB7z2NC5nLz2GJGFEYAZIp8G\nBF/oRKtLKSaxCjwew2P13W7xFa0a9PQP29KN/F7fSA+Z2eD4yBg0f4Tdq01Fqax5\nccJrmYXoFH5DXyYqfiC6P1N8UwshNV5ax4Hr4/n51F5+VQ62lmRkDUsZHXftgjjJ\nJtnGZjC7a5pTA4L2JD4TaxKfFE65P13YqCYCmZ/2GxPKonIL2aK5iVQLA4ijJQAo\nKVODRWhjAgMBAAECggEAChLwKjVy+t9Pv9U/UzxRTVGvDXGw/FPDor/qLeyFkBKp\nOWl9tw3Y4M7CbYNPpAEVMwFMaRILbvWBG9fQlR4zpYCgetNwt+hgqseBs+3P/OOi\nHfg5uKe5+gTInZMhoT79bXDE942qOwubYI6dgdGHgCDeahe1oXXpl02rld8UBQZQ\nq2q408P5XSJZ7GRaJKzqNF+2QD3HMrngS+VKuHDV7+jERnIHwOI5XG7ALhOT30Zt\nh+WHBIYptqI0XdUVx5RgmtM+zMrIzTTrieUZbvmqQ5xVD65GSfNPdNbhKv50VTSZ\n17F6TxrnLSoGKzWX17iueIizXoV1NABjVoemHZ7bJQKBgQDc5MgYNEFnF4YTNB13\nB/i/B3jUMzFyS/3LJAjqushOYlmAVfQa7fq0zAoRimNBylDtt71wZbY4wAvNPQ88\nkWVTIEUx3QuZac7s1+pFrQQ5SXLTEaDonVzUZUHLHTM+oe1Y2Wz+zA2JIgjvpr8j\nqSxlcY3TwX/fpGyeZggOTsOYFQKBgQDI9SCwIatLE/0VDnqnqURp7olA48JFtjID\nkmuGL3OzQNVvz3pLA+cDzjJCDrrXgKAkPDtkQRT2Y6Sp3Frs5N7CLpQvJqZJJqGY\n31e4O7vHBFZkfDo622Cu0nrEvgwBJ22EBOQVMDZ6qz7MAxfHuYsr63z4UlV0QFYP\nd6I3+aTklwKBgAqHjVI6C3QSlv2LWmw2IRFaFdRnrE+6d5qbWSF3Td0Oqx2G+1/d\nQDomD8TOR/T24+yw+YLGFm2WGfnqkzNb6uyPeTzrQIZLmOWJVU2E9dKVQbf1+ymb\ndrVZLk20UqEFrv6xPpTWvT5wNOTXmfzlL4yWYSBa9PGAMP1L985WytQRAoGAFdXU\nvG6cHydH247cMvWIcn4xubRFuq9mVc8GEel8B+Emj+SaZCZDZr1z5ouVL69RNz64\nMVeFAJSpIq/HzW+86JqJDWqErPQeoO67qFANQj2taXO6HAUUR0qlflUsFsAC/VJO\nuiKn+MI8q4w2fEQj5BzNUmoX0O7gqwOTw8NDcHcCgYEAuFjxiSdq7fiAzKbW11pG\n0Yqx8yhC9RrWdJLDo0wPNW047o5h/nPXzxIu2l7/67/o8MVVXK9zd7O/Gd+x98dJ\nkaB15CBl1PIxi7KD90IYQxUuK0n3IaIw95SYl6hHZJ2epx7FUtf+RMAzWHgn5Nn8\nVpkHO6zn0npb6DUa722wGHY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@riyal1-c9fe9.iam.gserviceaccount.com",
  "client_id": "110677410535866182525",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
})




firebase_admin.initialize_app(cred)

# rest stays the same...

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