from flask import Flask, render_template, send_from_directory, request, jsonify
app = Flask(__name__)

num = 0

@app.route('/')
def index():
    return render_template('index.html', number=num)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/increase', methods=["POST"])
def increase():
    global num
    data: dict[str, int] = request.get_json()
    if not data:
        return 400
    n = data.get("number", None)
    if n == None:
        return 400
    num = max(num, n)

    return jsonify({"counter": num}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 