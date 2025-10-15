f = open("text.txt", "w+t")
f.write("Hello\n")

# Ваше решение.
f.seek(0)
reading = f.read().strip()
print(reading)

f.close()