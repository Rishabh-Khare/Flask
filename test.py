from flask import Flask ,redirect, url_for, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Biryani'
@app.route('/success/')
def success(uname):
   return 'welcome % Flask'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['user']
    print(username)
    if username == "sunil":
        return redirect(url_for('success', uname=username))

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/biryani')
def hello_wo():
    return 'Biryani Party'
if __name__ == '__main__':
    app.run()