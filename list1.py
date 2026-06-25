results = ["Mario", "Luigi"]

results.append("Princess") # add to last of the list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

print(results)

results.append(["Bowser", "Donkey Kong Jr."]) # this will append the list itselt to the results list
print(results)
results.remove(["Bowser", "Donkey Kong Jr."])
print(results)
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)

results.remove("Bowser") # remove element

print(results)

results.insert(0, "Bowser") # add to list at a specific index

print(results)

print(results.index("Mario")) # print index of element

results.reverse() #reverse list

print(results)