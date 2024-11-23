from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='src', template_folder='src')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style/<path:filename>')
def serve_styles(filename):
    return send_from_directory('src/style', filename)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('src/assets', filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('src/assets', filename, as_attachment=True)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)