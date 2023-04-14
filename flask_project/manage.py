from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Flask Login App!</h1>'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'Buffalo$':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))
    return render_template('login.html')


@app.route('/login/success/')
def success():
    return '<h1>Login Successful!</h1>'

@app.route('/login/failure/')
def failure():
    return '<h1>Login not successful!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
