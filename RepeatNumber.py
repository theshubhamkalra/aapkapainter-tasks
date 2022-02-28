# Write a code that prints out the first occurrence of a duplicate in a given array of integers
#     Sample Input: [1,2,3,2,1]
#     Output: 2
inp=[1,2,3,2,1]
dic={}
for i in inp:
    try :
        if dic[i]==1:
            print(i)
            break
        else :
            dic[i]+=1
            continue
    except:
        dic[i]=1
        continue



