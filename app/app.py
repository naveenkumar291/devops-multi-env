from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "unknown")
    version = os.getenv("APP_VERSION", "unknown")

    return f"""
    <h1>DevOps Multi-Environment Application</h1>
    <p>Environment: {environment}</p>
    <p>Version: {version}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)