import Data_API_database.data_to_database as database_data
import collections


def get_all_data_from_base():
    cursor, connection = database_data.connection_with_database()
    cursor.execute("""SELECT * from flights;""")
    _result = cursor.fetchall()
    connection.commit()
    connection.close()
    return _result


def get_flight_country_from_base():
    cursor, connection = database_data.connection_with_database()
    _result = cursor.execute("""SELECT country from flights;""")
    return _result


def make_country_dict():
#    cursor, connection = database_data.connection_with_database()
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

    return flight_dict

print(make_country_dict())
