some_rando_list = []

some_rando_list.append("Blah")

some_rando_list.extend(["yadda", "hello", "ahoy", "Blah"])

print(some_rando_list)

print(some_rando_list.count("Blah"))

print(some_rando_list)

if "yadda" in some_rando_list:
    print("Found the word!")
else:
    print("Word not there")

some_rando_list.sort()