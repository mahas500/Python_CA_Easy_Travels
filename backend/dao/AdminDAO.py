import pymysql

from dbconfig import mysql
from flask import jsonify


class AdminDAO:
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    @classmethod
    def adminlogin(cls, username, password):
        try:

            cls.cursor.execute("SELECT * FROM employee e where e.username = %s and e.password = %s",
                               (username, password))
            rows = cls.cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cls.cursor.close()
            cls.conn.close()
