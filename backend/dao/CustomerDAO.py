import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def customerCreate(cls, name, username, password, email, contact_no):
        try:
            customerId= str(uuid.uuid4())
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
    def customerEnquiryCreation(cls, employee_id,customer_id, enquiry_detail,enquiry_type,required_days,required_nights,required_country):
        try:
            enquiryID= str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into enquiry (enquiry_id,employee_id,customer_id, enquiry_detail,enquiry_type,required_days,required_nights,required_country) value (%s,%s,%s,%s,%s,%s,%s,%s)",
                (enquiryID, employee_id,customer_id, enquiry_detail,enquiry_type,required_days,required_nights,required_country))
            conn.commit()
            cursor.execute("SELECT * from enquiry e WHERE e.enquiry_id = %s",
                           enquiryID)

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def customerLoginAuthentication(cls, username,password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sessionId = str(uuid.uuid4())

            cursor.execute("update customer set session_id = %s where username = %s",
                           (sessionId, username))
            conn.commit()

            cursor.execute("SELECT * from customer where username = %s and password= %s",
                           (username,password))
            rows = cursor.fetchone()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getCustomerFromCustomersessionId(cls, sessionId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer c WHERE c.session_id = %s ",
                           sessionId)
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

            cursor.execute("SELECT * from customer")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllEnquiryfromDB(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from enquiry")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def deleteCustomerfromDB(cls,customer_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("DELETE from customer where customer_id=%s",customer_id)
            conn.commit()
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()