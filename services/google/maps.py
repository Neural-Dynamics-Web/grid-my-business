# region				-----External Imports-----
import requests
import typing
import math
import os
# endregion


def find_nearest_businesses(longitude: float,
                            latitude: float,
                            query: str)\
    -> typing.List[typing.Dict]:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"\
        + "?location={latitude}, {longitude}"\
        + "&query={query}"\
        + "&key={key}"
    
    google_api_key = os.environ.get("GOOGLE_KEY")
    url = url.format(longitude=longitude,
                     key=google_api_key,
                     latitude=latitude,
                     query=query)
    
    base_point = {"location": {"lng": longitude,
                               "lat": latitude}}

    results = requests.get(url=url)\
        .json().get("results", [])

    if results:
        sort = lambda o:\
            distance(second_point=o["geometry"],
                     first_point=base_point)
        results = sorted(results, key=sort)

    return results[:20]


def distance(second_point: typing.Dict,
             first_point: typing.Dict)\
    -> float:
    x_axis = second_point["location"]["lat"]\
           - first_point["location"]["lat"]
    
    y_axis = second_point["location"]["lng"]\
           - first_point["location"]["lng"]
    
    return math.sqrt(x_axis ** 2 + y_axis ** 2)