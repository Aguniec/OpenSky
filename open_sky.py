from opensky_api import OpenSkyApi

api = OpenSkyApi()
states = api.get_states()
for s in states.states:
    print("callsign: {}, origin_country:{}".format(s.callsign, s.origin_country))
