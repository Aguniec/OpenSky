import requests
import json
import sqlite3
import collections


def get_data():
    response = requests.get(
        "https://opensky-network.org/api/states/all")
    data = response.json()
    return data

    # print(resposne.json())


def data_to_database():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    sql_command = """ CREATE TABLE flights (
        number VARCHAR(20) , country VARCHAR(20));"""
    cursor.execute(sql_command)
    connection.commit()

    connection.close()


def input_data():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    _data = get_data()
    for item in _data["states"]:
        #        print(item)
        raw_sql_command = """ INSERT INTO flights (number, country) VALUES ("{flight_number}", "{flight_country}");""".format(
            flight_number=item[1], flight_country=item[2])
#        sql_command = raw_sql_command.format
        cursor.execute(raw_sql_command)
#        print(item[1])
    connection.commit()
    connection.close()


def get_all_data_from_base():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    cursor.execute("""SELECT * from flights;""")
    _result = cursor.fetchall()
    connection.commit()
    connection.close()
    return _result


def get_flight_country_from_base():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    _result = cursor.execute("""SELECT country from flights;""")

#     = cursor.fetchall()

    return _result


def make_country_dict():
    connection = sqlite3.connect("database.sql")
    cursor = connection.cursor()
    _data = get_flight_country_from_base()
    freq = {}
    for item in _data:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    freq = collections.OrderedDict(
        sorted(freq.items(), key=lambda t: t[1]))
    flight_dict = {}
    for k, v in freq.items():
        flight_dict["country {}".format(k)] = "number of flights {}".format(v)

    return(flight_dict)
#    print(dict(freq))
#    for key, value in freq.items():
#        print("{} : {}".format(key, value))
#    return freq.items()

    #    data_to_database()
print(make_country_dict())
