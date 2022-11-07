from flask import Flask,  render_template, request, redirect, url_for, session # pip install Flask
from flask_mysqldb import MySQL,MySQLdb # pip install Flask-MySQLdb
from notifypy import notify

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("login.html")  


@app.route('/templates/registro.html', methods = ["GET", "POST"])
def registro():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    tipo = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    interes = cur.fetchall()

    cur.close()

    notificacion = notify()
    
    

    if request.method == 'GET':
        return render_template("registro.html", tipo = tipo, interes = interes )
    
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tip = request.form['tipo']
        interes = request.form['interes']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES (%s,%s,%s,%s,%s)", (name, email, password,tip,interes,))
        mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message="ya te encuentras registrado en 🤵 MORE LOVE 👰, por favor inicia sesión y empieza a descubrir este nuevo mundo."
        notificacion.send()
        return redirect(url_for('login'))

if __name__ == '__main__':
    
    app.run(debug=True, port=3050)