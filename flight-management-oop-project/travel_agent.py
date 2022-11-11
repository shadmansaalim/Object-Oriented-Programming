from airports import Airports
from airlines import Airlines


class TravelAgent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None
        self.airports = Airports()
        self.airlines = Airlines()
    '''
        params:
        start : Departing city code
        end: Destination city code
        departure_date: Date when you start the trip

        return :
        aircraft, price

        Notes : Use Airlines to select aircraft
    '''

    def set_trip_one_city_one_way(self, start, end, departure_date):
        price = self.airports.get_ticket_price(start, end)
        distance = self.airports.get_distance_between_airports(start, end)
        aircraft = self.airlines.get_aircraft_by_distance(distance)
        return [aircraft, price]

    def set_trip_one_city_two_way(self):
        pass

    def set_trip_multi_city_one_way(self):
        pass

    def set_trip_multi_city_round(self):
        pass

    def __repr__(self) -> str:
        return f'TravelAgent: {self.name}'
