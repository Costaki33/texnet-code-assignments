import math


def haversine(lat1, lon1, lat2, lon2, unit='km'):
    """
    Calculates the great circle distance in km or mi between two points on the earth given as decimal points

    :parameter lat1, lon1: Latitude and longitude of the first point.
    :parameter lat2, lon2: Latitude and longitude of the second point.
    :parameter unit: 'km' for kilometers, 'mi' for miles. Default is 'km'.
    :return: Distance between provided points in the specified unit of measure
    """

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of the Earth
    r = 6371  # km
    if unit == 'mi':
        r = 3956  # miles

    distance = r * c

    return distance


lat1, lon1 = 37.9838, 23.7275  # Athens, Greece
lat2, lon2 = 45.4642, 9.1900  # Milan, Italy

distance_miles = haversine(lat1, lon1, lat2, lon2, 'mi')
print(f"Distance: {distance_miles:.2f} miles")