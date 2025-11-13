import random
random = random.randint(0, 7)
fortune_list = ["Don't pursue happiness – create it.", 
"All things are difficult before they are easy.",
"The early bird gets the worm, but the second mouse gets the cheese.",
"Someone in your life needs a letter from you.",
"Don't just think. Act!",
"Your heart will skip a beat.",
"The fortune you search for is in another cookie.",
"Help! I'm being held prisoner in a Chinese bakery!"
]
def fortune():
  if random == 0:
    print(fortune_list[0])
  elif random == 1:
    print(fortune_list[1])
  elif random == 2:
    print(fortune_list[2])
  elif random == 3:
    print(fortune_list[3])
  elif random == 4:
    print(fortune_list[4])
  elif random == 5:
    print(fortune_list[5])
  elif random == 6:
    print(fortune_list[6])
  else:
    print(fortune_list[7])

fortune()