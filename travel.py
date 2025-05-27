class Bus:
    def _init_(self, bus_no, source, destination, total_seats):
        self.bus_no = bus_no
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.booked_seats = 0

    def display_info(self):
        print(f"Bus No: {self.bus_no} | Route: {self.source} -> {self.destination} | "
              f"Available Seats: {self.total_seats - self.booked_seats}")

    def book_ticket(self, seats):
        if self.total_seats - self.booked_seats >= seats:
            self.booked_seats += seats
            print(f"{seats} seat(s) booked successfully!")
            return True
        else:
            print("Not enough seats available!")
            return False


class TravelAgency:
    def _init_(self):
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def show_buses(self):
        print("\nAvailable Buses:")
        for bus in self.buses:
            bus.display_info()

    def find_bus(self, bus_no):
        for bus in self.buses:
            if bus.bus_no == bus_no:
                return bus
        return None


# Main Program
agency = TravelAgency()

# Adding sample buses
agency.add_bus(Bus("101", "City A", "City B", 40))
agency.add_bus(Bus("102", "City B", "City C", 35))

while True:
    print("\n--- Travel Bus Booking System ---")
    print("1. View Available Buses")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        agency.show_buses()

    elif choice == '2':
        bus_no = input("Enter Bus Number: ")
        bus = agency.find_bus(bus_no)
        if bus:
            seats = int(input("Enter number of seats to book: "))
            bus.book_ticket(seats)
        else:
            print("Bus not found!")

    elif choice == '3':
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")