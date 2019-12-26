import pymysql

from dbconfig import mysql
from flask import jsonify
from models.employee import Employee


class AdminDAO:
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    @classmethod
    def adminlogin(cls, username, password):
        try:
            admin = Employee()
            cls.cursor.execute("SELECT * FROM employee e where e.username = %s and e.password = %s",
                               (username, password))
            rows = cls.cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            admin = resp
            return admin
        except Exception as e:
            print(e)
        finally:
            cls.cursor.close()
            cls.conn.close()
