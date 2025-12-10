dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))
merged_dict = {}
for k, v in dict1.items():
    merged_dict[k] = merged_dict.get(k, 0) + v
for k, v in dict2.items():
    merged_dict[k] = merged_dict.get(k, 0) + v
print("Merged dictionary:", merged_dict)