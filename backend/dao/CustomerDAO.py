import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def customerCreate(cls, name, username, password, email, contact_no):
        try:
            sessionId = str(uuid.uuid4())
            customerId = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into customer (customer_id, name,username,password,email,contact_no,session_id) value (%s, %s, %s,%s, %s, %s,%s)",
                (customerId, name, username, password, email, contact_no, sessionId))
            conn.commit()
            cursor.execute("SELECT * from customer c WHERE c.session_id = %s",
                           sessionId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getCustomerFromCustomerId(cls, customerId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer c WHERE c.customer_id = %s ",
                           customerId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:

            print(e)
        finally:

            cursor.close()
            conn.close()

    @classmethod
    def getAllCustomersfromDB(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()



    @classmethod
    def deleteCustomerfromDB(cls, customer_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("DELETE from customer where customer_id=%s", customer_id)
            conn.commit()
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()
