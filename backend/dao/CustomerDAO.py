import uuid

import pymysql

from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def customerCreate(cls, customer_id, name, username, password, email, contact_no):
        try:
            sessionId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            sql = "insert into customer (customer_id, name,username,password,email,contact_no,session_id) values(%s, %s, %s,%s, %s, %s,%s)"
            val = (customer_id, name, username, password, email, contact_no, sessionId);
            cursor.execute(
                "insert into customer (customer_id, name,username,password,email,contact_no,session_id) value (%s, %s, %s,%s, %s, %s,%s)",
                (customer_id, name, username, password, email, contact_no, sessionId))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
