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
    data = admin.display_stocks()
    return render_template("admin.html", data=data)


@app.route("/admin/add", methods=['POST'])
def addStock():
    if request.method == 'POST':
        productName = request.form.get('product-name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        new_record = {'Product Name': productName,
                      'Price': price,
                      'Quantity': quantity}
        print(new_record)
        print(admin.Add_Stock(new_record))

    return redirect(url_for('adminPage'))


@app.route('/edit/<int:index>', methods=['POST'])
def editStock(index):
    print("edit function")
    # add edit feature
    return redirect(url_for('adminPage'))


@app.route('/delete/<int:index>', methods=['POST'])
def deleteStock(index):
    print("delete function", index)
    # add delete feature
    return redirect(url_for('adminPage'))


# webview.create_window('Billing App', app)  # To enable a gui window
if __name__ == '__main__':
    app.run(debug=True)  # Only use for development (recommended)
    # webview.start()  # To start a gui
