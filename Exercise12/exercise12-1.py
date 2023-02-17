# Collections

# Printing code as written adds each letter, O, K, E, individually
# cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'

# 'Oke' needs to be included in [] for it to work correctly
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke', 'Brie']

# Using just = will replace the initial value, but using += add in at that spot
cheese[2:3] += ['Camembert', 'Mozzarella']

# But for some reason using 0: = will just add in at that position
cheese[0:] = ['Halloumi', 'Feta']

print(cheese)
