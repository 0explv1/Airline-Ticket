# /usr/local/bin/pip3 install flask << run this to install locally
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

app = Flask(__name__)

# configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='air ticket reservation system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# define route [HOME]
@app.route('/')
def home():
    # SQL query to select data
    query = "SELECT * FROM flight WHERE status='upcoming'"
    
    with conn.cursor() as cursor:
        cursor.execute(query)
        up_flights = cursor.fetchall()  # fetch all rows from the last executed statement
        
    return render_template('mp_home.html', up_flights=up_flights)


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)