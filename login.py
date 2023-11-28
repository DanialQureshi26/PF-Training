from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Replace these with your actual credentials
admin_credentials = {"admin": "admin123"}
manager_credentials = {"manager": "manager123"}
user_credentials = {"user": "user123"}

@app.route('/')
def login():
    error = request.args.get('error', '')
    return render_template('login.html', error=error)

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username in admin_credentials and password == admin_credentials[username]:
        return redirect(url_for('admin_dashboard'))
    elif username in manager_credentials and password == manager_credentials[username]:
        return redirect(url_for('manager_dashboard'))
    elif username in user_credentials and password == user_credentials[username]:
        return redirect(url_for('user_dashboard'))
    else:
        return redirect(url_for('login', error='1'))

@app.route('/admin')
def admin_dashboard():
    return render_template('admin dashboard.html')

@app.route('/manager')
def manager_dashboard():
    return render_template('manager dashboard.html')

@app.route('/user')
def user_dashboard():
    return render_template('user dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

