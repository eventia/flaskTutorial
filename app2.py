from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# global 변수들
# id_global = 'bob'
# pw_global = '1111'
users = [{'name': 'xxx', 'pw': 'yy'}]

# 페이지를 부르는 역할
@app.route('/')
def home():
    return 'this is home page!'

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

    global users
    # global id_global
    # global pw_global

    for user in users:
        if user['name'] == id_receive and user['pw'] == pw_receive
        return jsonify({'result':'success'})
    return jsonify({'result': 'fail', 'msg':'아이디 또는 패스워드가 틀립니다'})
    # if (id_receive == id_global) and (pw_receive == pw_global):
    #     return jsonify({'result': 'success'})
    # else:
    #     return jsonify({'result': 'fail'})

@app.route('/userregister', methods=['POST'])
def userregister():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    global users
    users.append({'name':id_receive,'pw':pw_receive})

    return jsonify({'result': 'success'})


@app.route('/userupdate', methods=['POST'])
def userupdate():
    global id_global
    global pw_global
    id_global = request.form['id_give']
    pw_global = request.form['pw_give']

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
