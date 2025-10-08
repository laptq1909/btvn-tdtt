Animal_Quantity = int(input("Ex15 quantity: "))
Total_Legs = int(input("Ex15 legs: "))
Chickens = (4 * Animal_Quantity - Total_Legs) // 2
Dogs = Animal_Quantity - Chickens

if Dogs != int(Dogs) or Chickens != int(Chickens) or Dogs < 0 or Chickens < 0:
    print("Invalid")
else:
    print(Chickens, end=" ")
    print(Dogs)