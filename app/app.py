from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'pav' 
 
mysql = MySQL(app)
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        role = details['role']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, role) VALUES (%s, %s)", (name, role)) # MySQL table name is user
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
