fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
even_numbers = list(map(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
