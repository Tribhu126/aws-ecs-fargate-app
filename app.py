from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

profile_data = {
    "name": os.getenv("NAME", "Tribhuvan Sharma"),
    "certification": "AWS Certified Solutions Architect",
    "specialization": os.getenv(
        "SPECIALIZATION",
        "Cloud Architecture & Solutions Consulting"
    ),
    "architecture": [
        "Docker",
        "Amazon ECS",
        "AWS Fargate",
        "Application Load Balancer",
        "CloudWatch Logs",
        "Auto Scaling"
    ],
    "region": "eu-central-1",
    "deployment": "Rolling Deployments"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/profile")
def profile():
    return jsonify(profile_data)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)