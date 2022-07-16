'''import pymysql
UPDATE mysql.user
SET Password=PASSWORD("Ivisivis5")
WHERE User="root";
'''


'''
from __future__ import print_function
import MySQLdb
import mysql.connector
import pymysql

hostname = 'database-1.czejdnwyu0eq.ap-south-1.rds.amazonaws.com'
username = 'root'
password = 'Ivisivis5'
database = 'management_server'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using mysqlclient (MySQLdb):" )

myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using mysql.connector:" )

myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using pymysql:" )

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
'''

'''
import aiomysql
import asyncio

loop = asyncio.get_event_loop()

hostname = 'database-1.czejdnwyu0eq.ap-south-1.rds.amazonaws.com'
username = 'root'
password = 'Ivisivis5'
database = 'management_server'
async def search_tel(telephone):
    conn = await aiomysql.connect(host="hostname", port="3306",
                                  user="username", password="password",
                                  db="database", loop=loop)
    cursor = await conn.cursor()
    await cursor.execute(f"SELECT TRUE FROM users WHERE telefon={telephone}")
    print(cursor.description)
    result = await cursor.fetchall()
    print(result)
    if result == 1:
        conn.close()
        return True
    else:
        conn.close()
        return False
tel = "000000000"
loop.run_until_complete(search_tel(telephone=tel))
'''


'''
import pymysql

conn = pymysql.connect(host='database-1.czejdnwyu0eq.ap-south-1.rds.amazonaws.com',user='root',password = "Ivisivis5",db='management_server',)
cur = conn.cursor()
cur.execute("show databases")
output = cur.fetchall()
print(output)      
conn.close()
'''
'''
from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route('/raw',methods=['GET','POST'])
def sample():
    if(request.method == 'GET'):
        data = 'hey there'
        return data
if __name__ == '__main__':
    app.run()





'''
'''
from flask import Flask
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)
class helloworld(Resource):
    def __init__(self):
        pass
    def get(self):
        return{'hello':'world'}
api.add_resource(helloworld,'/')
if __name__ == '__main__':
    app.run(debug=True)
'''



from flask import Flask
app = Flask(__name__)
@app.route('/')
def helo_name(name):
    return 'hey there'
@app.route('/man')
def sample():
    return 'im here'
if __name__ == '__main__':
    app.run()

































