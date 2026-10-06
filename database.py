print("EHAX In-Memory Database")
database = {}
while True:
    command = input("DB >  ")
    parts = command.split()
    print(parts)
    if parts[0] == "SET" :
        key = parts[1]
        value = parts[2]
        database[key]= value
        print ("OK")
    elif parts[0] == "GET":
        key = parts [1]
        print (database[key])
    elif parts[0] == "EXISTS":
        key = parts[1]
        print (key in database)
    elif parts[0] == "DEL":
        key = parts[1]
        del database[key]
        print("Deleted")