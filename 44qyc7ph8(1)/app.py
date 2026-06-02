from flask import Flask, render_template, jsonify

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="static"
)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/api/stats")
def stats():
    return jsonify({
        "points": 120,
        "tasks": 12,
        "challenges": 5
    })

@app.route("/api/leaderboard")
def leaderboard():
    return jsonify([
        {"name": "Rohit", "points": 450},
        {"name": "Kiran", "points": 400},
        {"name": "Rahul", "points": 350}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)