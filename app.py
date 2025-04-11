import os
from flask import Flask, request, jsonify, send_file, abort
from functools import wraps
from werkzeug.utils import secure_filename
import utils
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

KEY = os.getenv("API_KEY")

app = Flask(__name__)
CORS(app)

def verify_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('api_key') or request.headers.get('X-API-KEY')
        if not api_key or api_key != KEY:
            return jsonify({"detail": "Invalid or missing API key"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET"])
@verify_api_key
def read_root():
    return jsonify({"Hello": "World"})

@app.route("/json-to-xlsx/<int:method_id>", methods=["POST"])
@verify_api_key
def json_to_xlsx(method_id):
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"error": "JSON must be a list of objects"}), 400
    elif method_id not in [1, 2]:
        return jsonify({"error": "/<method_id>/ must be 1 or 2"}), 400

    output = utils.json_to_xlsx(data, method_id)

    if method_id == 1:
        return send_file(
            output,
            as_attachment=True,
            download_name="result.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    elif method_id == 2:
        download_url = f"{request.host_url}/download/{output}?api_key={KEY}"
        return jsonify({"url": download_url})

@app.route("/download/<token>", methods=["GET"])
@verify_api_key
def download_file(token):
    path = utils.token_map.get(token)
    if not path or not os.path.exists(path):
        abort(404, description="File not found or expired")
    return send_file(
        path,
        as_attachment=True,
        download_name=os.path.basename(path),
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.route("/xlsx-to-json", methods=["POST"])
@verify_api_key
def xlsx_to_json():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    contents = file.read()
    json_data = utils.xlsx_to_json(contents)
    return jsonify(json_data)

@app.route("/html-to-pdf/<int:method_id>", methods=["POST"])
@verify_api_key
def html_to_pdf(method_id):
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    html_content = file.read()
    pdf_data = utils.html_to_pdf(html_content, method_id)

    if method_id not in [1, 2]:
        return jsonify({"error": "/<method_id>/ must be 1 or 2"}), 400

    if method_id == 1:
        return send_file(
            pdf_data,
            as_attachment=True,
            download_name="result.pdf",
            mimetype="application/pdf"
        )
    elif method_id == 2:
        download_url = f"{request.host_url}/download/{pdf_data}?api_key={KEY}"
        return jsonify({"url": download_url})

if __name__ == "__main__":
    app.run(debug=True)
