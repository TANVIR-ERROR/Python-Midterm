class Star_Cinema:
    __hall_list = []  # Class attribute to store the list of halls

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall(cls, hall_no):
        for hall in cls.__hall_list:
            if hall.get_hall_no() == hall_no:
                return hall
        return None

    @classmethod
    def view_all_halls(cls):
        if not cls.__hall_list:
            print("No halls are currently registered.")
            return
        for hall in cls.__hall_list:
            print(f'Hall No: {hall.get_hall_no()}')

class Hall(Star_Cinema):
    def __init__(self, hall_no, rows, cols):
        self.__seats = {}  # Dictionary to store seats information
        self.__show_list = []  # List to store show information
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def get_hall_no(self):
        return self.__hall_no

    def entry_show(self, show_id, movie_name, time):
        """Method to add a new show"""
        show = (show_id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[show_id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        print(f"Show '{movie_name}' added successfully!")

    def book_seats(self, show_id, seat_list):
        """Method to book seats for a show"""
        if show_id not in self.__seats:
            print("Invalid show ID. Please enter a correct show ID.")
            return

        for row, col in seat_list:
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Invalid seat ({row}, {col}). Please choose a valid seat.")
            elif self.__seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[show_id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        """Method to view all shows running"""
        if not self.__show_list:
            print("No shows are currently running.")
            return
        for show_id, movie_name, time in self.__show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        """Method to view available seats for a show"""
        if show_id not in self.__seats:
            print("Invalid show ID. Please enter a correct show ID.")
            return

        print(f"Available seats for show ID {show_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                seat_status = "Available" if self.__seats[show_id][row][col] == 0 else "Booked"
                print(f"Seat ({row}, {col}): {seat_status}")


# Create some halls and add shows
hall1 = Hall(1, 5, 5)
hall2 = Hall(2, 6, 6)

hall1.entry_show(101, "Inception", "5:00 PM")
hall1.entry_show(102, "Titanic", "8:00 PM")

hall2.entry_show(201, "Avatar", "6:00 PM")
hall2.entry_show(202, "Interstellar", "9:00 PM")

# Main Counter Operations
while True:
    print("\nOptions:")
    print("1: View all shows")
    print("2: View available seats for a show")
    print("3: Book seats for a show")
    print("4: Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        Star_Cinema.view_all_halls()
        hall_no = int(input("Enter hall number to view shows: "))
        hall = Star_Cinema.get_hall(hall_no)
        if hall:
            hall.view_show_list()
        else:
            print("Invalid hall number.")

    elif option == 2:
        hall_no = int(input("Enter hall number to view available seats: "))
        hall = Star_Cinema.get_hall(hall_no)
        if hall:
            show_id = int(input("Enter show ID to view available seats: "))
            hall.view_available_seats(show_id)
        else:
            print("Invalid hall number.")

    elif option == 3:
        hall_no = int(input("Enter hall number to book seats: "))
        hall = Star_Cinema.get_hall(hall_no)
        if hall:
            show_id = int(input("Enter show ID to book seats: "))
            num_seats = int(input("Enter number of seats to book: "))
            seats = []
            for _ in range(num_seats):
                row = int(input("Enter seat row: "))
                col = int(input("Enter seat column: "))
                seats.append((row, col))
            hall.book_seats(show_id, seats)
        else:
            print("Invalid hall number.")

    elif option == 4:
        print("Exiting system.")
        break

    else:
        print("Invalid option. Please try again.")
