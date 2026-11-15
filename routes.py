import math

routes = [
    {
        "route_number": "1",
        "origin": "Public Market",
        "destination": "City Hall",
        "fare": 13
    },
    {
        "route_number": "2",
        "origin": "Bus Terminal",
        "destination": "Public Market",
        "fare": 15
    },
    {
        "route_number": "3",
        "origin": "City Hall",
        "destination": "General Hospital",
        "fare": 13
    },
    {
        "route_number": "4",
        "origin": "Town Plaza",
        "destination": "Shopping Mall",
        "fare": 15
    },
    {
        "route_number": "5",
        "origin": "Public Market",
        "destination": "University",
        "fare": 13
    },
    {
        "route_number": "6",
        "origin": "Bus Terminal",
        "destination": "City Hall",
        "fare": 15
    },
    {
        "route_number": "7",
        "origin": "Shopping Mall",
        "destination": "General Hospital",
        "fare": 18
    },
    {
        "route_number": "8",
        "origin": "University",
        "destination": "Town Plaza",
        "fare": 13
    },
    {
        "route_number": "9",
        "origin": "Train Station",
        "destination": "Public Market",
        "fare": 15
    },
    {
        "route_number": "10",
        "origin": "Sports Complex",
        "destination": "Bus Terminal",
        "fare": 20
    },
    {
        "route_number": "11",
        "origin": "Airport",
        "destination": "City Center",
        "fare": 25
    },
    {
        "route_number": "12",
        "origin": "North Terminal",
        "destination": "South Station",
        "fare": 22
    },
    {
        "route_number": "13",
        "origin": "Port Area",
        "destination": "Public Market",
        "fare": 16
    },
    {
        "route_number": "14",
        "origin": "IT Park",
        "destination": "University",
        "fare": 14
    },
    {
        "route_number": "15",
        "origin": "Central Square",
        "destination": "Industrial Zone",
        "fare": 19
    }
]


def validate_route(data, *, partial=False):
    """Return a normalized payload and an error, without changing stored routes."""
    fields = {'route_number', 'origin', 'destination', 'fare'}
    if not isinstance(data, dict) or not data:
        return None, 'Provide a non-empty JSON object'
    if data.keys() - fields:
        return None, 'Unknown route fields'
    if not partial and fields - data.keys():
        return None, 'Missing required fields'

    normalized = data.copy()
    if 'route_number' in data:
        number = data['route_number']
        if type(number) not in (str, int) or not str(number).strip():
            return None, 'route_number must be a non-empty string or integer'
        normalized['route_number'] = str(number).strip()
    for field in ('origin', 'destination'):
        if field in data:
            if not isinstance(data[field], str) or not data[field].strip():
                return None, f'{field} must be a non-empty string'
            normalized[field] = data[field].strip()
    if 'fare' in data:
        fare = data['fare']
        if (type(fare) not in (int, float) or fare < 0
                or (isinstance(fare, float) and not math.isfinite(fare))):
            return None, 'fare must be a finite, non-negative number'
    return normalized, None
