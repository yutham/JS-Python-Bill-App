from flask import Flask,render_template
 
import webview # Libray to create a gui window
 
app = Flask(__name__, static_folder='./static', template_folder='./templates')
 
@app.route('/')
def login():
    return render_template("login.html",name='cairocoders Home page')
 
@app.route('/home')
def home():
    return render_template("home.html",name='cairocoders page 2')
     
webview.create_window('Billing App', app) # To enable a gui window
 
if __name__ == '__main__':
    # app.run(debug=True) # Only use for development (recommended)
    webview.start() # To start a gui