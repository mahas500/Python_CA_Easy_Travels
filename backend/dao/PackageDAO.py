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

            cursor.execute("select * from package")

            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
