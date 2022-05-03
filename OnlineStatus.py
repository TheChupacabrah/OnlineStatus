#Online Count Challenge
#John Hatch

statuses = {"Alice" : "online", "Bob" : "offline", "Eve" : "online", "Jackson" : "online", "JB" : "online", "Bauer Boy" : "online", "Bauerton" : "online", "Jackie B" : "online"}

def online_count(statuses):
    return sum(status == 'online' for status in statuses.values())

print("People Online: ")
print(online_count(statuses))


