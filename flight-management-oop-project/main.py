from travel_agent import TravelAgent


def main():
    travel_agent = TravelAgent('Alex Nguyen')
    trip_info1 = travel_agent.set_trip_one_city_one_way(
        'DAC', 'PRA', '05/07/2056')
    print('Aircraft', trip_info1.aircraft)
    print('Price', trip_info1.price)


if __name__ == '__main__':
    main()
