# pop items from motorcycle list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}. ")
