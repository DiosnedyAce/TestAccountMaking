from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
accounts = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
        username = request.form['username']
        password = request.form['password']
        
        accounts[username] = password
        
        print(accounts)
        return  'Account created!'
    
if __name__ == '__main__':
    app.run()