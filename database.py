import ast
print("EHAX In-Memory Database")
database = {}
while True:
    command = input("DB >  ")
    parts = command.split()
    if len(parts) == 0:
        print("Please enter a command")
        continue
    if parts[0] == "SET" :
        if len(parts) !=3:
            print("Usage: SET <key> <value>")
            continue
        key = parts[1]
        value = parts[2]
        database[key]= value
        print ("OK")
    elif parts[0] == "GET":
        if len(parts) != 2:
            print("Usage: GET <key>")
            continue
        key = parts [1]
        if key in database:
            print(database[key])
        else:
            print("Key not found")
    elif parts[0] == "EXISTS":
        if len(parts) != 2:
            print("Usage: EXISTS <key>")
            continue
        key = parts[1]
        print (key in database)
    elif parts[0] == "DEL":
        if len(parts) != 2:
            print("Usage: DEL <key>")
            continue
        key = parts[1]
        if key in database:
            del database[key]
            print("Deleted")
        else:
            print("Key not found")
    elif parts[0] == "SAVE":
        if len(parts) != 2:
            print("Usage: SAVE <filename>")
            continue
        filename = parts[1]
        file = open(filename, "w")
        file.write(str(database))
        file.close()
        print("Database saved successfully")
    elif parts[0] == "LOAD":
        if len(parts) != 2:
            print("Usage: LOAD <filename>")
            continue
        filename = parts[1]
        file = open(filename, "r")
        data = file.read()
        database = ast.literal_eval(data)
        file.close()
        print("Database loaded successfully")
    elif parts[0] == "EXIT":
        print("Exiting database...")
        break
    else:
        print("Unknown command")
    