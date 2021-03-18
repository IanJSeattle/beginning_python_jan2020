two_cards = [(2, 'hearts'), (3, 'spades')]
total = 0
for items in two_cards:
    number = items[0]
    suit = items[1]
    print(f'{suit} {number}')
    total += number
    answer = input('Press enter to hit, or "s" to stay ')
    if answer == "s":
        break

print(f'number of points: {total}')