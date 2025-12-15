fruits = ('apple', 'banana', 'guava', 'mango', 'lichi', "grapes")

for fruit in fruits:
    print(fruit)
    
print(f"\n {fruits[:4]} \n")
capital_fruits = (fruit.title() for fruit in fruits)
for fruit in capital_fruits:
    print(fruit.title())
