def createFile():
    with open("bookings.txt", "a") as f:
        pass

def menu () :
    print("Welcome to Room Booking")
    print("Please select an option(number): ")
    print("1. Book room")
    print("2. Cancel booking")
    print("3. Update booking")
    print("4. List bookings")
    print("5. Help")
    print("6. Exit")

def loadBookings():
    bookings = []
    with open("bookings.txt", "r") as f:
        for line in f:
            bookings.append(line.strip().split(","))
    return bookings

def isClashing (building ,room ,  startTime ,endTime ):

    bookings = loadBookings()

    for b in bookings:
        
        bStart = b[3]
        bEnd = b[4]

        if building == b[2] and room == b[1]:

            if startTime<bEnd and bStart< endTime:
                return True 
    
    return False


def bookRoom():
    
    building = input("Enter Building name : ")
    room = input("Enter Room name : ")
    startTime = input("Enter Start time (HH:MM) : ")
    endTime = input("Enter End time (HH:MM) : ")

    clash = isClashing(building, room, startTime, endTime)
    if clash:
        print("The selected time slot for the specified room is already booked.")
        return
    bookingId = (str(len(loadBookings()) + 1))

    data = bookingId + "," + room + "," + building + "," + startTime + "," + endTime

    with open("bookings.txt", "a") as f:
        f.write(data + "\n")

    print("Room booked successfully. Booking ID: " + bookingId + "\n" + "Thank You")

def cancelBooking():
    bId = input("Enter Booking ID to cancel: ")
    bookings = loadBookings()

    with open("bookings.txt", "w") as f:
        for b in bookings :
            if b[0] != bId:
                f.write(",".join(b) + "\n")
    print("Booking canceled successfully. Booking ID: " + bId)

def listBookings():
    bookings = loadBookings()
    if not bookings:
        print("No bookings found.")
        return
   
    print("\n1. List All Bookings")
    print("2. List by Building")
    print("3. List by Room")
    choice = input("Enter your choice: ")

    if choice == "1":
        for b in bookings:
            print(f"Booking ID: {b[0]}, Room: {b[1]}, Building: {b[2]}, Start Time: {b[3]}, End Time: {b[4]}")
    elif choice == "2":
        foundBuilding = False
        building = input("Enter Building name: ")
        for b in bookings:
            if b[2] == building:
                foundBuilding = True
                print(f"Booking ID: {b[0]}, Room: {b[1]}, Building: {b[2]}, Start Time: {b[3]}, End Time: {b[4]}")
        if not foundBuilding:
            print("No bookings found for the specified building.")

    elif choice == "3":
        room = input("Enter Room name: ")
        foundRoom = False
        for b in bookings:
            if b[1] == room:
                foundRoom = True
                print(f"Booking ID: {b[0]}, Room: {b[1]}, Building: {b[2]}, Start Time: {b[3]}, End Time: {b[4]}")
        if not foundRoom:
            print("No bookings found for the specified room.")
    else:
        print("Invalid choice. Please try again.")


def updateBooking():
    bId = input("Enter Booking ID to update: ")
    bookings = loadBookings()
    
    with open("bookings.txt", "w") as f:
        for b in bookings :
            if(b[0]) != bId:
                f.write(",".join(b) + "\n")
    
    print("Select new details for the booking: ")
    bookRoom()



def help():
    print("Help Information:")
    print("1. To book a room, select option 1 ")
    print("2. To cancel a booking, select option 2 ")
    print("3. To update a booking, select option 3 ")
    print("4. To list bookings, select option 4 ")
    print("5. To get help, select option 5 ")
    print("6. To exit the program, select option 6 ")





def main ():
    createFile()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            bookRoom()
        elif choice == "2":
            cancelBooking()
        elif choice == "3":
            updateBooking()
        elif choice == "4":
            listBookings()
        elif choice == "5":
            help()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
