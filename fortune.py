import random
filename = "fortune.txt"
content = open(filename).read()
print(random.choice(content.split("%")))
