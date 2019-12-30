import uuid
import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class EnquiryDAO:
    @classmethod
    def createEnquiry(cls, employee_id, customer_id, enquiry_detail, enquiry_type, required_days,
                      required_nights, required_country):
        try:
            enquiryID = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into enquiry (enquiry_id,employee_id,customer_id, enquiry_detail,enquiry_type,required_days,required_nights,required_country) value (%s,%s,%s,%s,%s,%s,%s,%s)",
                (enquiryID, employee_id, customer_id, enquiry_detail, enquiry_type, required_days, required_nights,
                 required_country))
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
    def getAllEnquiries(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from enquiry e ORDER BY e.created_on DESC")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()
