# Flight Reservation System
# Data Structures Project: Searching and Sorting

flights = [
    {"no": 104, "airline": "IndiGo", "source": "Pune",
     "destination": "Delhi", "price": 5200, "seats": 5},

    {"no": 101, "airline": "Air India", "source": "Mumbai",
     "destination": "Pune", "price": 2800, "seats": 4},

    {"no": 105, "airline": "Akasa Air", "source": "Pune",
     "destination": "Goa", "price": 3100, "seats": 6},

    {"no": 102, "airline": "IndiGo", "source": "Delhi",
     "destination": "Mumbai", "price": 6100, "seats": 3},

    {"no": 103, "airline": "Air India", "source": "Pune",
     "destination": "Bengaluru", "price": 4500, "seats": 2}
]

bookings = []


def display_flights(data):
    print("\nFlight Details")
    print("-" * 75)
    print(f"{'No.':<8}{'Airline':<15}{'Source':<12}"
          f"{'Destination':<15}{'Price':<10}{'Seats'}")
    print("-" * 75)

    for f in data:
        print(f"{f['no']:<8}{f['airline']:<15}"
              f"{f['source']:<12}{f['destination']:<15}"
              f"{f['price']:<10}{f['seats']}")

    print("-" * 75)


# 1. Linear Search by destination
def linear_search(destination):
    result = []

    for flight in flights:
        if flight["destination"].lower() == destination.lower():
            result.append(flight)

    return result


# 2. Binary Search by flight number
def binary_search(number):
    data = sorted(flights, key=lambda f: f["no"])

    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid]["no"] == number:
            return data[mid]

        elif data[mid]["no"] < number:
            low = mid + 1

        else:
            high = mid - 1

    return None


# 3. Bubble Sort by ticket price
def bubble_sort():
    data = flights.copy()
    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j]["price"] > data[j + 1]["price"]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# 4. Merge Sort by flight number
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["no"] <= right[j]["no"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 5. Book a ticket
def book_ticket():
    try:
        number = int(input("Enter flight number: "))
        ticket_count = int(input("Enter number of tickets: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if ticket_count <= 0:
        print("Ticket count must be greater than zero.")
        return

    flight = binary_search(number)

    if flight is None:
        print("Flight not found.")
        return

    if flight["seats"] < ticket_count:
        print("Not enough seats available.")
        return

    name = input("Enter passenger name: ").strip()

    if not name:
        print("Passenger name cannot be empty.")
        return

    flight["seats"] -= ticket_count

    booking = {
        "name": name,
        "flight": number,
        "tickets": ticket_count,
        "total": flight["price"] * ticket_count
    }

    bookings.append(booking)

    print("\nBooking Successful!")
    print("Passenger:", name)
    print("Flight Number:", number)
    print("Tickets:", ticket_count)
    print("Total Amount: Rs.", booking["total"])


# 6. Display bookings
def show_bookings():
    if not bookings:
        print("No bookings available.")
        return

    print("\nBooking Details")

    for b in bookings:
        print(
            "Passenger:", b["name"],
            "| Flight:", b["flight"],
            "| Tickets:", b["tickets"],
            "| Amount: Rs.", b["total"]
        )


# Main menu
while True:
    print("\n===== FLIGHT RESERVATION SYSTEM =====")
    print("1. Display All Flights")
    print("2. Search by Destination (Linear Search)")
    print("3. Search by Flight Number (Binary Search)")
    print("4. Sort by Price (Bubble Sort)")
    print("5. Sort by Flight Number (Merge Sort)")
    print("6. Book a Ticket")
    print("7. View Bookings")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_flights(flights)

    elif choice == "2":
        destination = input("Enter destination: ")
        result = linear_search(destination)

        if result:
            display_flights(result)
        else:
            print("No flights found for this destination.")

    elif choice == "3":
        try:
            number = int(input("Enter flight number: "))
            result = binary_search(number)

            if result:
                display_flights([result])
            else:
                print("Flight not found.")

        except ValueError:
            print("Enter a valid flight number.")

    elif choice == "4":
        print("\nFlights sorted by price:")
        display_flights(bubble_sort())

    elif choice == "5":
        print("\nFlights sorted by flight number:")
        display_flights(merge_sort(flights.copy()))

    elif choice == "6":
        book_ticket()

    elif choice == "7":
        show_bookings()

    elif choice == "8":
        print("Thank you for using Flight Reservation System!")
        break

    else:
        print("Invalid choice. Please try again.")
