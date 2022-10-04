array = ["chocolate", "rain", 1, 9, 11, "chocolate", "rain", "rain"]
repeated = array[0]
most = 0

for i in range(len(array)):
    if array.count(array[i]) > most:
        most = array.count(array[i])
        repeated = array[i]

new_word = input("ingresa el sustituto: ")

for i in range(len(array)):
    if array[i] == repeated:
        array[i] = new_word

print(array)