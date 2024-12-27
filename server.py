import os
from flask import Flask, send_from_directory, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='src', template_folder='src')

VALID_HASH = os.getenv('VALID_HASH')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style/<path:filename>')
def serve_styles(filename):
    return send_from_directory('src/style', filename)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('src/assets', filename)

@app.route('/protected_assets/<path:filename>')
def serve_protected_assets(filename):
    hash = request.args.get('hash')
    if hash == VALID_HASH:
        return send_from_directory('src/protected_assets', filename)
    else:
        return "You do not have access to this resource.", 403
    
@app.route('/src/protected_assets/<path:filename>')
def serve_protected_assets_from_src(filename):
    hash = request.args.get('hash')
    if hash == VALID_HASH:
        return send_from_directory('src/protected_assets', filename)
    else:
        return "You do not have access to this resource.", 403
    
@app.route('/src/apks/<path:filename>')
def serve_apks_from_src(filename):
    hash = request.args.get('hash')
    if hash == VALID_HASH:
        return send_from_directory('src/apks', filename)
    else:
        return "You do not have access to this resource.", 403

@app.route('/download/<filename>')
def download_file(filename):
    hash = request.args.get('hash')
    if hash == VALID_HASH:
        return send_from_directory('src/apks', filename, as_attachment=True)
    else:
        return "You do not have access to this resource.", 403

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)