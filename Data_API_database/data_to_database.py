import requests
import sqlite3


def get_data():
    response = requests.get(
        "https://opensky-network.org/api/states/all")
    data = response.json()
    return data


def connection_with_database():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    return cursor, connection


def commit_and_close_connecition(connection):
    connection.commit()
    connection.close()


def create_table_for_flight_and_country():
    cursor, connection = connection_with_database()
    sql_command = """ CREATE TABLE flights (
        callsign VARCHAR(20) , country VARCHAR(20));"""
    cursor.execute(sql_command)
    commit_and_close_connecition(connection)


def input_data_into_table():
    cursor, connection = connection_with_database()
    _data = get_data()
    for item in _data["states"]:
        raw_sql_command = """ INSERT INTO flights (callsign, country) VALUES ("{callsign}", "{flight_country}");""".format(
            callsign=item[1], flight_country=item[2])
        cursor.execute(raw_sql_command)
    commit_and_close_connecition(connection)


# create_table_for_flight_and_country()
input_data_into_table()
