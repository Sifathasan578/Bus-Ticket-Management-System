print('WELCOME TO DIGITECHBITS TICKET BOOKING SYSTEM')

# Initialize seat details
lst = list(range(1, 51))         # seat status
fname = [""] * 50                # first names
lname = [""] * 50                # last names
agep = [0] * 50                  # ages

while True:
    print("\n1. Book Ticket")
    print("2. Check Ticket Status")
    print("3. Cancel Ticket")
    print("4. Check Detail of Booked Ticket")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            tic = int(input('Enter seat number (1-50): '))
            if tic < 1 or tic > 50:
                print("Invalid seat number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if lst[tic - 1] == 'B':
            print("\n*************************")
            print("Seat is already booked. Try another seat.")
            print("*************************\n")
        else:
            fname1 = input('Enter your first name: ')
            lname1 = input('Enter your last name: ')
            try:
                age1 = int(input('Enter your age: '))
            except ValueError:
                print("Invalid age input.")
                continue

            lst[tic - 1] = 'B'
            fname[tic - 1] = fname1
            lname[tic - 1] = lname1
            agep[tic - 1] = age1

            print('\n*************************')
            print("Your ticket is booked!")
            print('*************************\n')

    elif choice == 2:
        print("\nSeat Status (B = Booked):")
        for i in range(50):
            status = lst[i]
            print(f"{status:>3}", end=' ')
            if (i + 1) % 10 == 0:
                print()
        print()

    elif choice == 3:
        try:
            tic = int(input('Enter seat number to cancel (1-50): '))
            if tic < 1 or tic > 50:
                print("Invalid seat number.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

        if lst[tic - 1] != 'B':
            print('\n*************************')
            print("This seat is not booked.")
            print('*************************\n')
        else:
            lst[tic - 1] = tic
            fname[tic - 1] = ""
            lname[tic - 1] = ""
            agep[tic - 1] = 0

            print('\n*************************')
            print("Your ticket is canceled.")
            print('*************************\n')

    elif choice == 4:
        try:
            s = int(input('Enter seat number (1-50): '))
            if s < 1 or s > 50:
                print("Invalid seat number.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

        index = s - 1
        if lst[index] != 'B':
            print('\n*************************')
            print("This seat is not booked.")
            print('*************************\n')
        else:
            print('\n*************************')
            print(f"Customer Name: {fname[index].title()} {lname[index].title()}")
            print(f"Age: {agep[index]}")
            print('*************************\n')

    elif choice == 5:
        print("\nThank you for using DIGITECHBITS Ticket Booking System. Goodbye!")
        break

    else:
        print('\n*************************')
        print("Invalid option. Please try again.")
        print('*************************\n')