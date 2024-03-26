from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    files = request.files.getlist('file')
    num_files = len(files)
    return render_template('result.html', num_files=num_files)

if __name__ == '__main__':
    app.run(debug=True)
