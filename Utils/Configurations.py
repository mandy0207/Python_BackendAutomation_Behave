import configparser

import mysql
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\msingh\PycharmProjects\pythonProject1\BackendAutomation\Utils\properties.ini")
    return config


connect_config = {
    "host": getConfig()['SQL']['host'],
    "database": getConfig()['SQL']['database'],
    "user": getConfig()['SQL']['user'],
    "password": getConfig()['SQL']['password']

}


def getAccessToken():
    return "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"


def getUsername():
    return "mandy0207"


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("connection successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
