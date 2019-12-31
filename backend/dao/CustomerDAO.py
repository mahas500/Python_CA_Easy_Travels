import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def customerCreate(cls, name, username, password, email, contact_no):
        try:
            customerId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into customer (customer_id, name,username,password,email,contact_no) value (%s, %s, %s,%s, %s, %s)",
                (customerId, name, username, password, email, contact_no))
            conn.commit()
            cursor.execute("SELECT * from customer c WHERE c.customer_id = %s",
                           customerId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def customerLogin(cls, username, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer where username = %s and password= %s",
                           (username, password))
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update customer set session_id = %s where customer_id = %s",
                               (sessionId, rows.get('customer_id')))
                conn.commit()

                cursor.execute("SELECT * from customer where username = %s and password= %s",
                               (username, password))
                rows = cursor.fetchone()
                return rows
            else:
                return None
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
    def getCustomerFromCustomerUserName(cls, username):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer c WHERE c.username = %s ",
                           username)
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

            cursor.execute("SELECT * from customer c ORDER BY c.created_on")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def deleteCustomer(cls, customer_id):
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

    @classmethod
    def searchCustomer(cls, searchText):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT * FROM customer WHERE MATCH (name, email) AGAINST ('*" + searchText + "*' IN BOOLEAN MODE) ORDER BY created_on"
            cursor.execute(query)
            rows = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

            conn.close()

    @classmethod
    def getCustomerfromCustomerSessionID(cls, session_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT customer_id from customer where session_id=%s", session_id)
            rows = cursor.fetchone()

            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

