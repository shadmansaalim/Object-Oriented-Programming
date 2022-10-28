# Numbers and characters map
numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D':  3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Star_Cinema:
    __hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        # PRIVATE
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        seats = []
        for i in range(0, self.__rows):
            s_col = []
            for j in range(0, self.__cols):
                s_col.append(False)
            seats.append(s_col)
        self.__seats[id] = seats

    def book_seats(self, name, phone, id, customer_seat_list):
        movie_name = ""
        time = ""
        for show in self.__show_list:
            if (show[0] == id):
                movie_name = show[1]
                time = show[2]
                break

        if (len(movie_name) == 0):
            print(
                "-------------------------------------------------------------------------\n")
            print("ID didn't match any show!")
            print(
                "\n-------------------------------------------------------------------------")
            return

        for seat in customer_seat_list:
            max_rows = characters[self.__rows]
            if (seat[0] >= 'A' and seat[0] <= max_rows and int(seat[1]) < self.__cols and len(seat) == 2):
                continue
            else:
                print(
                    "-------------------------------------------------------------------------\n")
                print(f"INVALID SEAT NO - {seat}. TRY AGAIN!")
                print(
                    "\n-------------------------------------------------------------------------")
                return

        unavailable = []
        for seat in customer_seat_list:
            if (self.is_seat_available(id, seat) == False):
                unavailable.append(seat)

        if (len(unavailable)):
            print(
                "-------------------------------------------------------------------------\n")
            print("BOOKING FAILED! THE FOLLOWING SEATS ARE ALREADY BOOKED : ", end="")
            for seat in unavailable:
                print(seat, end=" ")
            print(
                "\n\n-------------------------------------------------------------------------")
            return

        print("##### TICKET BOOKED SUCCESSFULLY!! #####")
        print("-------------------------------------------------------------------------\n")
        print(f"NAME : {name}")
        print(f"PHONE NUMBER : {phone}")
        print("")
        print(f"MOVIE NAME: {movie_name}\t\tSHOW ID: {id}\t\tTIME: {time}")
        print("TICKETS: ", end="")
        seats = self.__seats[id]
        for seat in customer_seat_list:
            row = numbers[seat[0]]
            col = int(seat[1])
            if (seats[row][col] == False):
                seats[row][col] = True
                print(f"{characters[row]}{col}", end=" ")
            else:
                pass
        print(f"\nHALL: {self.__hall_no}")
        print("\n-------------------------------------------------------------------------")

    def view_show_list(self):
        print("-------------------------------------------------------------------------\n")
        for show in self.__show_list:
            id = show[0]
            movie_name = show[1]
            time = show[2]
            print(f"MOVIE NAME: {movie_name}\t\tSHOW ID: {id}\t\tTIME: {time}")
        print("\n-------------------------------------------------------------------------")

    def is_seat_available(self, id, seat):
        seats = self.__seats[id]
        row = numbers[seat[0]]
        col = int(seat[1])
        if (seats[row][col] == True):
            return False
        return True

    def view_available_seats(self, id):
        movie_name = ""
        time = ""

        for show in self.__show_list:
            if (show[0] == id):
                movie_name = show[1]
                time = show[2]
                break

        if (len(movie_name) == 0):
            print(
                "-------------------------------------------------------------------------\n")
            print("ID didn't match any show!")
            print(
                "\n-------------------------------------------------------------------------")
            return

        print(f"MOVIE NAME: {movie_name}\t\tTIME: {time}")
        print("X for already booked seats")

        print("-------------------------------------------------------------------------\n")
        seats = self.__seats[id]
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                if (seats[i][j] == False):
                    char_map = characters[i]
                    print(f"{char_map}{j}\t", end="")
                else:
                    print("X\t", end="")
            print("")
        print("\n-------------------------------------------------------------------------")


hall = Hall(3, 5, 101)
hall.entry_show("ae123", "Black Adam", "OCT 26 2022 10:00 PM")
hall.entry_show("ae50", "Superman", "OCT 26 2022 08:00 PM")

while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    opt = int(input("ENTER OPTION : "))

    if (opt == 1):
        print("")
        hall.view_show_list()
        print("")

    elif (opt == 2):
        show_id = input("ENTER SHOW ID : ")
        print("")
        hall.view_available_seats(show_id)
        print("")

    elif (opt == 3):
        name = input("ENTER CUSTOMER NAME : ")
        phone = input("ENTER CUSTOMER PHONE NUMBER : ")
        show_id = input("ENTER SHOW ID : ")
        ticket_no = int(input("ENTER NUMBER OF TICKETS: "))
        customer_seat_list = []
        for i in range(0, ticket_no):
            seat_no = input("ENTER SEAT NO: ")
            customer_seat_list.append(seat_no)
        print("")
        hall.book_seats(name, phone, show_id, customer_seat_list)
        print("")
