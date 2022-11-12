from airports import Airports
from airlines import Airlines
from trip import Trip
from itertools import permutations


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
        trip = Trip([start, end], aircraft, price,
                    departure_date, [start, end])
        return trip

    def set_trip_one_city_round_way(self, start, end, departure_date):
        trip1 = self.set_trip_one_city_one_way(
            start, end, departure_date)

        trip2 = self.set_trip_one_city_one_way(
            end, start, departure_date)

        return [trip1, trip2]

    def set_trip_two_city_one_way(self, trip_info, departure_date):
        trip1 = self.set_trip_one_city_one_way(
            trip_info[0], trip_info[1], departure_date)

        trip2 = self.set_trip_one_city_one_way(
            trip_info[1], trip_info[2], departure_date)

        return [trip1, trip2]

    def set_trip_multi_city_one_way_fixed_route(self, trip_info, departure_date):
        trips = []
        for i in range(0, len(trip_info)-1):
            trip = self.set_trip_one_city_one_way(
                trip_info[i], trip_info[i+1], departure_date)
            trips.append(trip)
        return trips

    def set_trip_multi_city_flexible_route(self, trip_cities, departure_date):
        start_city = trip_cities[0]
        flexible_cities = trip_cities[1:]
        for sequence in permutations(flexible_cities):
            for i in range(0, len(flexible_cities)):
                print(sequence[i])

    def __repr__(self) -> str:
        return f'TravelAgent: {self.name}'
