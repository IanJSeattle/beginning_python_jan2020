two_of_hearts = (2, 'hearts')
seven_of_spades = (7, 'spades')
cards = [two_of_hearts, seven_of_spades]

total_value = 0

for card in cards:
    suit = card[1]
    value = card[0]    
    print(f'{suit} of {value}')
    total_value += value # equivalent to "running_total = running_total + price"

print(f'points {total_value}')