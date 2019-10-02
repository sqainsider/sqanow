# import psycopg2
import sqlite3
from datetime import datetime, date, timedelta
import os
import sys
import json
import csv
from time import ctime
from pathlib import Path
import getpass
from cryptography.fernet import Fernet
import string
import random


sys.path.append(os.path.abspath(
    r"C: \Automation\AutoPilot\Beta\py_workspace\splunk"))

tester = getpass.getuser()
env = 'QA'


# def verify_sales_order_file(sales_order_file):
#     so_file = Path(sales_order_file)
#     if so_file.exists():
#         pass
#         print(so_file.exists())
#         print(so_file.stat())
#         print(ctime(so_file.stat().st_ctime))
#         return
#     else:
#         print(
#             f"{'Sales order:(SO-'}{sal_order}) {'does not exist on repo, please export again'}")
#         exit()


# def select_sales_order():

#     process = sys._getframe().f_code.co_name
#     print("\n")
#     print('"*** Enetr Sales Orders  ' + process)

#     print("-" * 100)
#     print('"*** Enetr Sales Orders  ' + process)
#     print("-" * 100)

#     # env = "STG"
#     # so = "115359"
#     # testdir = r"c:\Automation\AutoPilot\Beta\PY\splunk\testfiles\NetSuite"
#     # test_file = Path(testdir + "\\" + env + "-SO-" + so + ".csv")
#     global so_nbr
#     so_nbr = input('Enter Sales Order/Quit(q):')
#     print('echo', so_nbr)
#     global test_file
#     if so_nbr.lower() != 'q':
#         if verify_sales_order_file():
#             so_items()
#     else:
#         exit()


# def so_items(so_csv):

#     # so_csv = r"C:\Automation\AutoPilot\Beta\PY\splunk_dev\test_files\NetSuite\STG-SO-115362.csv"
#     with open(so_csv) as file:
#         reader = list(csv.DictReader(file))
#         # print(reader)
#         return reader


def str_to_int(text):
    number = int(text.strip())
    return number


def str_to_dcml2(text):
    if not text:
        number = 0.00
    elif text[-1:] == '%':
        number = round(float(text.strip().replace('%', ''))/100, 2)
    else:
        number = round(float(text.strip()), 2)
    return number


def str_to_float(text):
    number = float(text.strip()), 2
    return number


def str_to_date(text):
    print("aaaaaa" + text)
    dt = datetime.strptime(text.strip(), '%m/%d/%Y')
    # print(dt)
    return dt


def timestamp_str():

    dt = datetime.now().strftime('%Y%m%d-%H%M')
    return dt


def today():

    dt = datetime.now().strftime('%m/%d/%Y')
    return dt


print(today())


def timestamp():

    dt = datetime.now().strftime('%Y%m%d-%H%M')
    return dt


def run_id():
    dt = datetime.now().strftime('%Y%m%d%H%M')
    return dt
# print(run_id())


# def so_nbr():

#     so = 'so-12222'
#     return so


def timestamp_now():
    dt = datetime.now().strftime('%m/%d/%Y : %H-%M')
    return dt


def calculate_days_between(start_date, end_date):
    start_dt = datetime.strptime(start_date, "%m/%d/%Y")
    end_dt = datetime.strptime(end_date, "%m/%d/%Y")
    print(str(abs((end_dt - start_dt).days) + 1))
    return str(abs((end_dt - start_dt).days) + 1)


def calculate_end_date_by_days(start_date, days):
    start_dt = datetime.strptime(start_date, "%m/%d/%Y")
    end_dt = start_dt + timedelta(days=days-1)
    # print(end_dt)
    end_dt = f"{end_dt.month}/{end_dt.day}/{end_dt.year}"
    return end_dt


def calculate_end_date_by_months(start_date, months):
    pass
    # start_dt = datetime.strptime(start_date, "%m/%d/%Y")
    # end_dt = start_dt + timedelta(days=days-1)
    # print(end_dt)
    # return end_dt


def sku_strp(item):
    index = item.index(': ')
    sku = (item[index+2:])
    return sku


def sku_reformat(item):
    if ': ' in item:
        index = item.index(': ')
        sku = (item[index+2:]) + ' (' + item[:index] + ')'
        return sku
    else:
        return item


# *******************************************************************
# Print log to screen
# *******************************************************************
def print_log(ts_log):
    for item in ts_log:
        print(item)

# *******************************************************************
# COnnect to PostgreSQL
# *******************************************************************


# def connectPostgreSQL():

#     try:
#         connection = psycopg2.connect(user="postgres",
#                                       password="admin",
#                                       host="localhost",
#                                       port="5432",
#                                       database="Splunk.db")

#         cursor = connection.cursor()
#         # Print PostgreSQL Connection properties
#         print(connection.get_dsn_parameters(), "\n")

#         # Print PostgreSQL version
#         cursor.execute("SELECT version();")
#         record = cursor.fetchone()
#         print("You are connected to - ", record, "\n")

#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL", error)

#     finally:
#         # closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")


# # connectPostgreSQL()


# Encryption/Decryption
# *****************************************************************************
# from cryptography.fernet import Fernet
# ***************************************************************************

def pyencrypttext(text):
    message = text.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message).decode()
    return encrypted


def pydecrypttext(text):
    encrypted = text1.encode()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted).decode()


# input_file = r'C:\Automation\autopilot\Beta\vscode\py_workspace\splunk\sandbox\test.txt'
# out_file = r'C:\Automation\autopilot\Beta\vscode\py_workspace\splunk\sandbox\test.encrypted'


def pyencryptfile(inputFile, outputFile):

    input_file = inputFile
    output_file = outputFile

    with open(input_file, 'rb') as f:
        data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

    with open(out_file, 'wb') as f:
        f.write(encrypted)


# pyencryptfile(input_file, out_file)

out_file = r'C:\Automation\autopilot\Beta\vscode\py_workspace\splunk\sandbox\test999.txt'
input_file = r'C:\Automation\autopilot\Beta\vscode\py_workspace\splunk\sandbox\test.encrypted'


def pydecryptfile(inputFile, outputFile):

    input_file = inputFile
    output_file = outputFile

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(out_file, 'wb') as f:
        f.write(encrypted)


# pydecryptfile(input_file, out_file)


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))


print(random_string(10))


