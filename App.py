from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
import mysql.connector
import datetime
import time

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/CompanyLogin")
def CompanyLogin():
    return render_template('CompanyLogin.html')


@app.route("/NewCompany")
def NewCompany():
    return render_template('NewCompany.html')


@app.route("/newcompany", methods=['GET', 'POST'])
def newcompany():
    if request.method == 'POST':
        name = request.form['t1']
        mobile = request.form['t2']
        email = request.form['t3']

        username = request.form['t4']
        Password = request.form['t5']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cregtb where username='" + username + "' ")
        data = cursor.fetchone()
        if data:
            data = "Already Register  UserName!"
            return render_template('goback.html', data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into cregtb values('','" + name + "','" + mobile + "','" + email + "','" + username + "','" + Password + "')")
            conn.commit()
            conn.close()
            data = "Record Saved!"
            return render_template('goback.html', data=data)


@app.route("/clogin", methods=['GET', 'POST'])
def clogin():
    if request.method == 'POST':
        username = request.form['Name']
        password = request.form['Password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cregtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)



        else:

            session['uname'] = username


            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM cregtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('CompanyHome.html', data=data)


@app.route("/CompanyHome")
def CompanyHome():
    uanme =  session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cregtb where USerNAme='"+ uanme +"'")
    data = cur.fetchall()

    return render_template('CompanyHome.html', data=data)


@app.route("/ClamInfo")
def ClamInfo():
    uanme =  session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurtb where Cname='"+ uanme +"' and Status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurtb where Cname='" + uanme + "' and Status !='waiting'")
    data1 = cur.fetchall()

    return render_template('ClamInfo.html', data=data,data1=data1)

@app.route("/Approved")
def Approved():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cursor = conn.cursor()
    cursor.execute(
        "Update  insurtb set Status='Approved'  where id='" + id + "'")
    conn.commit()
    conn.close()
    un = request.args.get('un')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from regtb where username='" + un + "'")
    data = cursor.fetchone()
    if data:
        sendmsg(data[2], 'Insurance Clam Accept')

    return ClamInfo()



@app.route("/Reject")
def Reject():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cursor = conn.cursor()
    cursor.execute(
        "Update  insurtb set Status='Reject'  where id='" + id + "'")
    conn.commit()
    conn.close()
    un = request.args.get('un')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from regtb where username='" + un + "'")
    data = cursor.fetchone()
    if data:
        sendmsg(data[2],'Insurance Clam Reject')

    return ClamInfo()

@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)


@app.route("/CompanyInfo")
def CompanyInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cregtb ")
    data = cur.fetchall()

    return render_template('CompanyInfo.html', data=data)


@app.route("/AdminReport")
def AdminReport():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM entrytb  ")
    data = cur.fetchall()
    return render_template('AdminReport.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['Name'] == 'admin' and request.form['Password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)

        else:
            data = "UserName or Password Incorrect!"

            return render_template('goback.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['t1']

        mobile = request.form['t2']
        email = request.form['t3']
        vno = request.form['t6']
        username = request.form['t4']
        Password = request.form['t5']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' or  VehicleNo='" + vno + "'")
        data = cursor.fetchone()
        if data:
            data = "Already Register  VehicleNo Or UserName!"
            return render_template('goback.html', data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into regtb values('','" + name + "','" + mobile + "','" + email + "','" + vno + "','" + username + "','" + Password + "')")
            conn.commit()
            conn.close()
            data = "Record Saved!"
            return render_template('goback.html', data=data)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['Name']
        password = request.form['Password']
        # session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)



        else:
            session['vno'] = data[4]
            session['uname'] = data[5]
            session['mob'] = data[2]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    username = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/Predict")
def Predict():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT username FROM cregtb   ")
    data = cur.fetchall()
    return render_template('Predict.html', data=data)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        import cv2
        t1 = request.form['t1']
        username = session['uname']

        file = request.files['file1']
        import random
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save('static/Out/' + savename)

        import warnings
        warnings.filterwarnings('ignore')

        import tensorflow as tf
        classifierLoad = tf.keras.models.load_model('body.h5')

        import numpy as np
        from keras.preprocessing import image

        test_image = image.load_img('static/Out/' + savename, target_size=(200, 200))
        img1 = cv2.imread('static/Out/Test.jpg')
        # test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifierLoad.predict(test_image)

        result1 = ''

        if result[0][0] == 1:

            result1 = "front"


        elif result[0][1] == 1:

            result1 = "rear"

        elif result[0][2] == 1:
            result1 = "side"

        file1 = request.files['file2']
        import random
        fnew1 = random.randint(1111, 9999)
        savename1 = str(fnew1) + ".png"
        file1.save('static/Out/' + savename1)

        import warnings
        warnings.filterwarnings('ignore')

        import tensorflow as tf
        classifierLoad = tf.keras.models.load_model('level.h5')

        import numpy as np
        from keras.preprocessing import image

        test_image = image.load_img('static/Out/' + savename1, target_size=(200, 200))
        img1 = cv2.imread('static/Out/Test1.jpg')
        # test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifierLoad.predict(test_image)

        result2 = ''

        if result[0][0] == 1:

            result2 = "minor"


        elif result[0][1] == 1:

            result2 = "moderate"

        elif result[0][2] == 1:
            result2 = "severe"

        if result1 == "front" and result2 == "minor":
            value = "30000 - 50000 INR"
        elif (result1 == "front" and result2 == "moderate"):
            value = "60000- 80000 INR"
        elif (result1 == "front" and result2 == "severe"):
            value = "90000 -110000 INR"

        elif (result1 == "rear" and result2 == "minor"):
            value = "40000 - 60000 INR"

        elif (result1 == "rear" and result2 == "moderate"):
            value = "70000 - 90000 INR"

        elif (result1 == "rear" and result2 == "severe"):
            value = "110000 - 130000 INR"

        elif (result1 == "side" and result2 == "minor"):
            value = "60000 - 80000 INR"

        elif result1 == "side" and result2 == "moderate":
            value = "90000 - 110000 INR"

        elif result1 == "side" and result2 == "severe":
            value = "120000- 150000 INR"

        else:
            value = "160000 - 500000 INR"

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into insurtb values('','" + username + "','" + savename + "','" + savename1 + "','" + value + "','Waiting','" + t1 + "')")
        conn.commit()
        conn.close()

        return render_template('Predict.html', prediction=value)


@app.route("/Status")
def Status():
    username = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurtb where username='"+ username +"'   ")
    data = cur.fetchall()
    return render_template('Status.html', data=data)

@app.route("/AClamInfo")
def AClamInfo():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2vehicledamageinsdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurtb w  ")
    data = cur.fetchall()
    return render_template('AClamInfo.html', data=data)


def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
