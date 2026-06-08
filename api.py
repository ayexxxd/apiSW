from flask import Flask, jsonify
from routes.routes import bp

# Think of it as the main thing that holds our routes and settings.
app = Flask(__name__)
app.json.sort_keys = False  # This keeps the order of keys in JSON responses as we defined them.

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, ssl_context="adhoc", debug=True)

# __name__ is a special Python variable.
# When this file is run directly, __name__ becomes "__main__".