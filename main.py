from flask import Flask, render_template, send_from_directory, request, jsonify
import os
app = Flask(__name__)

file = "counter.txt"

class da:
    def __init__(self):
        self.n = 0

d = da()

def load():
    if not os.path.exists(file):
        return
    with open(file) as f:
        c = f.read()
        num = int(c)
        print(f"Loaded {num}")
        d.n = num

def save(n: int):
    with open(file, "w") as f:
        f.write(str(n))
        print(f"Saved {str(n)}")

@app.route('/')
def index():
    return render_template('index.html', number=d.n)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/increase', methods=["POST"])
def increase():
    data: dict[str, int] = request.get_json()
    if not data:
        return 400
    n = data.get("number", None)
    if n == None:
        return 400
    old = d.n
    num = max(old, n)
    print(f"Updating from {old} to {num}")
    d.n = num
    save(num)

    return jsonify({"counter": num}), 200

if __name__ == '__main__':
    load()

    app.run(host='0.0.0.0', port=8888, debug=True)
 