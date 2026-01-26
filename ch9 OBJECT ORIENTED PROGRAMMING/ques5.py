# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, name, total_seats, fare):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare
        self.booked_seats = 0

    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= (self.total_seats - self.booked_seats):
            self.booked_seats += number_of_tickets
            return f"{number_of_tickets} tickets booked successfully."
        else:
            return "Not enough seats available."

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        return f"Available seats: {available_seats}"

    def get_fare_info(self):
        return f"Fare per ticket: {self.fare}"
# Example usage:
train = Train("Express", 100, 500)  
print(train.book_ticket(5))          # Booking 5 tickets
print(train.get_status())            # Getting status of seats
print(train.get_fare_info())        # Getting fare information
