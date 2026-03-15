friends_dict = {}

def add_friends(name_of_person, list_of_friends):
    if name_of_person in friends_dict:
        friends_dict[name_of_person].extend(list_of_friends)
    else:
        friends_dict[name_of_person] = list_of_friends

def are_friends(name_of_person1, name_of_person2):
    if name_of_person1 in friends_dict:
        return name_of_person2 in friends_dict[name_of_person1]
    return False

def print_friends(name_of_person):
    if name_of_person in friends_dict:
        print(' '.join(sorted(set(friends_dict[name_of_person]))))

add_friends("Алла", ["Денис", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
print_friends("Алла")