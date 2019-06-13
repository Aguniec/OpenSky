import requests


class Flights():
    def __init__(self):
        response = requests.get("https://opensky-network.org/api/states/all?")
        data = response.json()
        self.flights_and_numbers = data["states"]

    def make_flight_and_number_dict(self):
        self.flights_and_numbers_dict = {}
        for vectors in self.flights_and_numbers:
            self.flights_and_numbers_dict[vectors[2]] = vectors[1]

        return self.flights_and_numbers_dict

    def make_flight_frequency_dict(self):
        self.frequency_dict = {}
        for vectors in self.flights_and_numbers:
            if vectors[2] in self.frequency_dict:
                self.frequency_dict[vectors[2]] += 1
            else:
                self.frequency_dict[vectors[2]] = 1

        return self.frequency_dict
