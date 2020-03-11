numbers = [2, 2, 3, 5, 6, 7, 7]
uniques = []
for number in numbers:
    print(number)
    if number not in uniques:
        uniques.append(number)
print(uniques)