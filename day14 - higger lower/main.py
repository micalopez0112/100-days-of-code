from game_data import data
import random

right = 0
game_over = False

while not game_over:
    person1 = data[random.randint(0, len(data) - 1)]
    person2 = data[random.randint(0, len(data) - 1)]

    print('Compare A: ' + person1['name'] + ', a ' + person1['description'] + ', from ' + person1['country'])
    print('Against B: ' + person2['name'] + ', a ' + person2['description'] + ', from ' + person2['country'])
    print('Who has more followers? Type "A" or "B"')

    answer = input().upper()
    if answer == 'A' and person1['follower_count'] >= person2['follower_count']:
        right += 1
    elif answer == 'B' and person2['follower_count'] >= person1['follower_count']:
        right += 1
    else:
        print('You lose!')
        print(f'Final score: {right}')
        game_over = True