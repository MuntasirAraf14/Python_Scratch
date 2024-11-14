command = ""
started = False
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")

        else:
            started = True
        print("Car started..")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped")    
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
            """
        )
    elif command == "quit":
        break
    else:
        print("Sorry I dont understand these")