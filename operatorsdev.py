# # # There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
# # tr1=98
# # tr2=94
# # tr3=41
# # tr4=96
# # tr5=11
# # answer=(tr1+tr2+tr3+tr4+tr5)/5
# # print("the average height of the trees is ", answer)

# Write a program to calculate the number of notes in the given amount?

amt = int(input("Enter amount"))
usd100=amt // 100
amt = amt%100

usd50=amt // 50
amt = amt%50

usd10=amt // 10
amt = amt%10

usd5=amt // 5
amt = amt%5

usd1=amt // 1


print("Notes of 100:", usd100)
print("Notes of 5:", usd50)
print("Notes of 10:", usd10)
print("Notes of 5:", usd5)
print("Notes of 1:", usd1)