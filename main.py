import random
yesroll = 'yes'
while yesroll == 'yes':
  diceAmount = input('How many dice would you like to roll? ')
  count = 0
  while count < int(diceAmount):
    diceroll = random.randint(1,6)
    print (diceroll)
    count += 1
  else:  
    yesroll = input('Would you like to roll again? ')
