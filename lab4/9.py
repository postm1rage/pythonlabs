last = ""


def print_without_duplicates(message):
    global last
    if last != message:
        print(message)
        last = message
    else:
        return


print_without_duplicates("а")
print_without_duplicates("а")
print_without_duplicates("кффывафываыву")
print_without_duplicates("а")
print_without_duplicates("кффывафываыву")
print_without_duplicates("кффывафываыву")
print_without_duplicates("фыва")
print_without_duplicates("кффывафываыву")
