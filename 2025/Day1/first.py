with open("2025/Day1/input.txt", "r") as f:
    input_list = f.readlines()

starting_point = 50
click = 0

for input in input_list:
    direction = input[:1]
    numbers = int(input[1:])

    if direction == "L":
        # el % con números negativos siempre devuelve un valor positivo
        starting_point = (starting_point - numbers) % 100
    elif direction == "R":
        starting_point = (starting_point + numbers) % 100

    if starting_point == 0:
        click += 1

print(click)
