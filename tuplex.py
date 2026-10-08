# # # tuplex=("1", ['4'], 0.5, 3)
# # # print(tuplex)

# tuplexx=(1, 2, 3, 4, 5, 6, 6, 6)
# print(tuplexx.count(6))

# # tuplexx= tuplexx+(9,)
# # print(tuplexx)

def palind(r):
    end=len(r) -1
    start=0
    while(start<end):
        if (r[start]!=r[end]):
            return False
        start+=1
        end-=1
    return True

r=(1,2,3,2,1)

if(palind(r)):
    print("The tuple is flip-flop")
else:
    print("The tuple is not flip-flop.")

