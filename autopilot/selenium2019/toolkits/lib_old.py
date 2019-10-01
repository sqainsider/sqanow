#import psycopg2
# import sqlite3
from datetime import datetime, date, timedelta
from time import ctime
import os
import sys
import json
import csv

from pathlib import Path
import getpass
# from cryptography.fernet import Fernet


sys.path.append(os.path.abspath(
    r"C: \Automation\AutoPilot\Beta\py_workspace\splunk"))

local_path = "c:\Automation\AutoPilot\Beta\py_workspace\splunk"
tester = getpass.getuser()
env = 'QA'


# Lib
# ************************************************************************

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


# Date Format

def str_to_date(text):
    dt = datetime.strptime(text.strip(), '%m/%d/%Y')
    return dt


def timestamp_str():
    dt = datetime.now().strftime('%Y%m%d-%H%M')
    return dt


def today():
    dt = datetime.now().strftime('%m/%d/%Y')
    # print(dt)
    return dt


print (today())


def run_id():
    dt = datetime.now().strftime('%Y%m%d%H%M')
    return dt


def so_nbr():

    so = 'so-12222'
    return so


def timestamp():

    dt = datetime.now().strftime('%Y%m%d-%H%M')
    return dt


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


# Encryption/Decryption
# *****************************************************************************
key = 'h-cHeLLPGVSTH_P4aWBySrHfvRWEPktkasSzanJr6Y4='
# from cryptography.fernet import Fernet
# ***************************************************************************


def pyEncryptText(text):
    message = text.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message).decode()
    print(encrypted)
    return encrypted


def pyDecryptText(text):
    encrypted = text1.encode()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted).decode()
    print(decrypted)


def pyDecryptFile(inputFile, outputFile):

    input_file = inputFile
    output_file = outputFile

    with open(input_file, 'rb') as f:
        data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

    with open(out_file, 'wb') as f:
        f.write(encrypted)


def pyDecryptFile(inputFile, outputFile):

    input_file = inputFile
    output_file = outputFile

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(out_file, 'wb') as f:
        f.write(encrypted)
