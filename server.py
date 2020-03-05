from flask import Flask, render_template, request, jsonify
import data

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder='', template_folder='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# used for store clothes data into database
@app.route('/server', methods=['POST'])
def server():
    # first get text info
    print(request.form)
    data.store_insert(request.form)
    # then get the image
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return "no file name"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "ok"

# used for store clothes data into database
@app.route('/serverRetrieve',)
def serverRetrieve():
    type = int(request.args.get('type'))
    print("type is ", type)
    ret = data.store_retrieve(type)
    return jsonify(ret)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')