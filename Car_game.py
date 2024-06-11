command=""
started=False

while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print("Car is Already started!..")
        else:
            started=True
            print("Car started Ready to goo...")
    
    
    elif command == "stop":
        if not started:
            print("Car is already Stoped!..")
        else:
            started=False
            print("Car stopped...")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
''')    
    elif command == "quit":
        break 
    else:
        print("Sorry I don't Understand that!..")
      
      
