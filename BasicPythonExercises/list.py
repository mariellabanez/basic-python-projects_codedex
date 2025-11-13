# Write code below 💖
playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
playlist.append('FAMOUS by ADP')
playlist.pop(2)
playlist.remove('Pinegrove - Darkness')

for i in range(len(playlist)):
  print(playlist[i])