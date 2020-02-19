from flask import Flask, render_template, request, jsonify
import data

app = Flask(__name__, static_folder='', template_folder='')

@app.route('/')
def index():
    return render_template('index.html')

# used for store clothes data into database
@app.route('/server', methods=['POST'])
def server():
    # print(request.form)
    # name = request.form['name']
    # print("1")
    # print("2")
    print(request.form)
    # n = request.form['name']
    # t = request.form['type']
    # loc = request.form['location'])
    data.store_insert(request.form)
    # type = request.form['form']
    # location = request.form['location']
    # submit = request.form['submit']
    return "ok"

# used for store clothes data into database
@app.route('/serverRetrieve', methods=['POST'])
def serverRetrieve():
    print(request.form)
    ret = data.store_retrieve(request.form)
    return ret

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')