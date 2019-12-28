import uuid

import pymysql

from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def customerCreate(cls, name, username, password, email, contact_no):
        try:
            sessionId = str(uuid.uuid4())
            customerId= str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into customer (customer_id, name,username,password,email,contact_no,session_id) value (%s, %s, %s,%s, %s, %s,%s)",
                (customerId, name, username, password, email, contact_no, sessionId))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def customerEnquiry(cls, name, username, password, email, contact_no):
        try:
            enquiryID= str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into enquiry (enquiry_id,employee_id,customer_id, enquiry_details,enquiry_type,required_days,required_nights,required_country) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (enquiryID, name, username, password, email, contact_no))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getCustomerFromCustomerId(cls, customer_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer c WHERE c.customer_id = %s ",
                           customer_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()