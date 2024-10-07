from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# Serve the audio and image files
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('static', filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)