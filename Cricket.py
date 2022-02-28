# Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball in an array.
# In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over.
#     Sample Input1: [1,2]
#     Output1: p1: 1, p2: 2
#     Sample Input2: [1,2,3,2,1]
#     Output2: p1: 4, p2: 5

inp=[1,2,3,2,1]
p1=0
p2=0
pFlag=1
for i in inp:
    if pFlag == 1:
        p1 += i
    else:
        p2 += i
    if i%2!=0:
        pFlag=-1*pFlag

print("p1: {}, p2: {}".format(p1,p2))




