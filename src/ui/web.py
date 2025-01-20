from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/subscriptions", methods=["GET", "POST", "DELETE"])
def manage_subscriptions():
    if request.method == "GET":
        return jsonify({"subscriptions": subscription_manager.list_subscriptions()})
    elif request.method == "POST":
        repo = request.json.get("repo_url")
        subscription_manager.add_subscription(repo)
        return jsonify({"message": "Subscription added."})
    elif request.method == "DELETE":
        repo = request.json.get("repo_url")
        subscription_manager.remove_subscription(repo)
        return jsonify({"message": "Subscription removed."})

if __name__ == "__main__":
    app.run(debug=True)
