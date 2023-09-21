
from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules import admin
import webview  # Library to create a gui window

app = Flask(__name__, static_folder='./static', template_folder='./templates')


@app.route('/')
def loginPage():
    return render_template("login.html")


@app.route('/home')
def homePage():
    return render_template("home.html")


@app.route('/admin')
def adminPage():
    data = admin.Display_stocks()

    return render_template("admin.html", data=data)


@app.route("/admin/add", methods=['POST'])
def addStock():
    if request.method == 'POST':
        New_Record = {}  # Create a dictionary to hold the form data
        New_Record['Product Name'] = request.form.get('product-name')
        New_Record['Price'] = request.form.get('price')
        New_Record['Quantity'] = request.form.get('quantity')
        print(New_Record)
        admin.Add_Stock(New_Record)

    return redirect(url_for('adminPage'))


@app.route('/edit/<int:index>', methods=['POST'])
def editStock(index):
    print("edit function")
    if request.method == "POST":
        Edited_Record = {}  # Create a dictionary to hold the form data
        Edited_Record['Product Name'] = request.form.get('product-name')
        Edited_Record['Price'] = request.form.get('price')
        Edited_Record['Quantity'] = request.form.get('quantity')
        index = int(index)

        admin.Edit_stocks(index, Edited_Record)

    return redirect(url_for('adminPage'))


@app.route('/delete/<int:index>', methods=['POST'])
def deleteStock(index):
    if request.method == "POST":
        print("delete function", index)
        index = int(index)
        admin.Delete_stocks(index)
    return redirect(url_for('adminPage'))


webview.create_window('Billing App', app)  # To enable a gui window


if __name__ == '__main__':
    # app.run(debug=True)  # Only use for development (recommended)
    webview.start()  # To start a gui
