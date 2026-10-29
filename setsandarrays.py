# set1={"Apple", "Apple", "Bananna", "Crushed Peaches", "Cantaloupe"}
# set2={"Orange", "Orange", "Pinealpple", "Apple"}
# set1.add("Donkey Fruit")
# print(set1,set2)
# common_set=set1.intersection(set2)
# print(common_set)

import array as arf
fruit_counts=arf.array('i',[3,5,2,4])
print("Fruit counts array- ", fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts after adding items- ", fruit_counts)

count_of_4=fruit_counts.count(4)
print("Number of times 4 appears- ", count_of_4)

fruit_counts.reverse()
print("Reversed fruit counts array- " ,fruit_counts)

