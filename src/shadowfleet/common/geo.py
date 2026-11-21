import math
EARTH_RADIUS_M = 6371000  

def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return the great-circle distance between two points in meters.

    Uses the haversine formula on a spherical Earth. Since haversine formula assumes
    the world is perfect sphere, the result can deviate from the true distance
    by a few tenths of a percent.

    Args:
        lat1: Latitude of the first point, in decimal degrees.
        lon1: Longitude of the first point, in decimal degrees.
        lat2: Latitude of the second point, in decimal degrees.
        lon2: Longitude of the second point, in decimal degrees.

    Returns:
        Distance in meters.
    """
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_latitude = phi_2 - phi_1
    delta_longitude = math.radians(lon2 - lon1)
    a = pow(math.sin(delta_latitude / 2), 2) + math.cos(phi_1) * math.cos(phi_2) * pow(math.sin(delta_longitude / 2), 2)
    d = 2*EARTH_RADIUS_M*math.asin(math.sqrt(a))
    return d