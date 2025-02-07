def find_pythagorean_triplets(n):
    triplets = []
    # Проходимо по всіх значеннях a, b, c
    for a in range(1, n+1):
        for b in range(a, n+1):  # починаємо з a, щоб уникнути повторів
            for c in range(b, n+1):  # починаємо з b, щоб уникнути повторів
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets

# Приклад використання:
n = int(input("Введіть значення n: "))
triplets = find_pythagorean_triplets(n)

# Вивести всі знайдені трійки
if triplets:
    print("Знайдені пифагорові трійки:")
    for triplet in triplets:
        print(triplet)
else:
    print(f"Не знайдено пифагорових трійок для n = {n}.")
