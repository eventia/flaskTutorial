from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

#global variables
id_global = 'bob'
pw_global = '1111'

# 페이지

# @decorator
@app.route('/')
def home():
    return 'My Homepage'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# API 역할
@app.route('/userlogin', methods=['POST'])
def userlogin():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    global id_global
    global pw_global

    if (id_receive == id_global) and (pw_receive == pw_global):
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'fail'})

@app.route('/userupdate', methods=['POST'])
def userupdate():
    global id_global
    global pw_global

    id_global = request.form['id_give']
    pw_global = request.form['pw_give']

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)