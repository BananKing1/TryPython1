def är_primtal(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Ange ett positivt heltal: "))
        if n <= 0:
            print("Du måste ange ett positivt heltal.")
        else:
            break
    except ValueError:
        print("Det måste vara ett heltal.")

print(f"Primtal mindre än eller lika med {n}:")
for num in range(2, n + 1):
    if är_primtal(num):
        print(num, end=" ")
        