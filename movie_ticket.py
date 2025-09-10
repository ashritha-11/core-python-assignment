def book_seat(booked_seats, seat_no, total_seats):
    if seat_no < 1 or seat_no > total_seats:
        print(f"Seat {seat_no} is invalid.")
    elif seat_no in booked_seats:
        print(f"Seat {seat_no} is already booked.")
    else:
        booked_seats.append(seat_no)
        print(f"Seat {seat_no} booked successfully.")
    return booked_seats

def cancel_seat(booked_seats, seat_no):
    if seat_no in booked_seats:
        booked_seats.remove(seat_no)
        print(f"Seat {seat_no} has been canceled.")
    else:
        print(f"Seat {seat_no} was not booked.")
    return booked_seats

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
booked_seats = book_seat(booked_seats, 3, total_seats)   
booked_seats = cancel_seat(booked_seats, 5)              
available = get_available_seats(total_seats, booked_seats)

print("Available seats:", available)
