def vaccum_cleaner_agnet (status_of_room):
    # here first we will unpack the tuple and take both room and its status value but seperate it into two variables  
    room, status = status_of_room
    if status == "Dirty":
        return "I will be cleaning the room."
    elif room == "A":
        return "Move to room B."
    elif status == "Clean":
        return "Room B is clean."
    else:
        return "Move to room A"
# Here in the status of room we have a number of list of possible status of the room A and B 
# either it could be clean or dirty
status_of_room = [
    ("A", "Clean"),
    ("A", "Dirty"),
    ("B", "Clean"),
    ("B", "Dirty")]
# Runging loop so the value from the list will be taken and check via the if-else conditional and display the resutl 
for s in status_of_room:
    action_performed = vaccum_cleaner_agnet (s)
    print (s, "->", action_performed)
