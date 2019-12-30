import uuid

import pymysql
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.engine import result

from dbconfig import mysql
from flask import jsonify


class PackageDAO:

    @classmethod
    def createPackage(cls, packageId, employee_id, package_display_name, unique_url_name, days, night, charges, country,
                      city, valid):
        try:

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "INSERT INTO package (package_id , employee_id , package_display_name , unique_url_name , days,night, charges ,country , city , valid) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (packageId, employee_id, package_display_name, unique_url_name, int(days), int(night), charges, country,
                 city, valid))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllPackages(cls):
        try:

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * FROM package p ORDER BY p.created_on DESC")

            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def createIternaryForPackage(cls, iternary_id, packageId, day_number, day_date, day_details):
        try:

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "INSERT INTO package_iternary (iternary_id, package_id, day_number, day_date, day_details) values (%s, %s, %s, %s, %s )",
                (iternary_id, packageId, int(day_number), day_date, day_details))
            conn.commit()
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getPackageFromPackgaeId(cls, packageId):
        try:

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("select * from package p where p.package_id = %s", packageId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getIternariesDetailsOfPackage(cls, packageId):
        try:

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("select * from package_iternary p WHERE p.package_id = %s ORDER BY p.day_number", packageId)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def PackageBookingByCustomer(cls, customer_id, package_id):
        try:

            bookingId = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into booking (booking_id, customer_id,package_id) value (%s, %s, %s)",
                (bookingId, customer_id, package_id))
            conn.commit()
            cursor.execute("SELECT * from booking WHERE booking_id = %s",
                           bookingId)
            rows = cursor.fetchone()
            return rows

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()