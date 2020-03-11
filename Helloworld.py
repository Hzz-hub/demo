command = ""
state = True
while True:
    command = input("> ").lower()
    if command == "start":
        if state:
            print("Car started...")
        else:
            print("the car is starting!!!")
        state = False

    elif command == "stop":
        if not state:
            print("Car stopped...")
            state = True
        else:
            print("to  start the car")
    elif command == "help":
        print("""
        start - to start the cat 
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry. I don't understand this ")
