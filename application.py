from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World 2 to test docker vesion'

@app.route('/admin')
def hello_world():
    return 'Hello Admin'
 
if __name__ == '__main__': 
    app.run(debug=True)
