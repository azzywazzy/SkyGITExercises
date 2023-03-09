

pelican = open("pelican.txt", "a")

line1 = pelican.write("A wonderful bird is the pelican\n")

line2 = pelican.write("His bill holds more than his belican\n")

lines = ["He can take in his beak\n", "Enough food for a week\n", "But I'm damned if I see how the helican.\n"]

pelican.writelines(lines)

pelican.close()