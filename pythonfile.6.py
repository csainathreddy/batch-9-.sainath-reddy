





      1.) python program to capitalize the first and last character of each world in a string
2.)input:128
   output:yes  128%1==0,1282==0, and 128%8==0.
3.)l1=[1,2,3,4], ;2=[5,6,7,8]
and both l1 and l2, ans=[6,8,10,12]

1.)
s1 = input("enter string: ")
fst = s1[0].upper()
ls1 = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

2.)
n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check= temp % rem
    if check! =0:
        f1 =1
    n = n/10


if f1==0:
    print("yes")
else:
    print("no")





n = 128
for i in str(n):
    print(i)
    


11 = [8,9,0,7]
12 = [7,6,5,4]
13=[]
for val in range(len(11)):
    ans = append(ans)
    print(13)

# ? charateristics of set
1.)set can be created using{]
2.)the elemnts inside set are not indexed
3.)does not allow duplicate valus
4.)it unordered
5.)heteronous
6.)mutable or changable


#Eg:1
s1 = {9,9,89,7,76,8+7j,(8,7,5),"truck",'e'}
#print(s1)

 #*Eg:2
#s2 = {5,8,98,[9,0]}
#print(s2) -->error
#*Eg:3
#min(),max().len()

# *eg
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
# add()
s1.add(43)
print(s1)

# update()
s1.update(9, 0)
print(s1)

# ? to delete element inside set
s1 = {8, 78, 67, 'ui'}

# pop() # to dlete one element randonly
s1.pop()
print(s1)

remove()
s1.remove(978)
print(s1)

discard()
s1.discard(8967)
print(s1)

clear()l1 = []
l1 = {}
print(type(l1)) --> datatype is dict

s1 = set() # to create empty set
print(type(s1))

s1 = {8, 9, 0}
s1.clear()
print(s1)

del s1
print(s1)
'''
# * join the sets
s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
# union() --> to combin 2 sets
s3 = s1.union(s2)
print(s3)

# * intersection() --> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.intersection(s2))

# * difference()
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmtric_difference(s2))

# isdisjoit(), issubset(), issuperset()
# s1 = {8,9,0}
# s2 {6,,5,8,9,0}

#print(s={s1.issubset(s2))
#print(s2.issuperset(s1))

s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

#n1 ={1,2,3} --> s1
#for val in s1:
  # if val in s2:
  # print("Its joint set"
   #print(strl)

   # ! ----> distionary
   #eg:
   d1 = {1:100,'a':200,4.5:"hello"}
   #print(d1)
   #print(len(d1))
 
s1 = {8, 9, 0}
s2 = {6, 7, 5, 8, 9, 0}

print(s1.issubset(s2))
print(s2.issuperset(s1))

# ! ---> problem:1
s1 = {1, 2, 3, 4, 5}
s2 = {3, 2, 7, 8, 9}

for val in s1:
    if val in s2:
        str1 = "its joint set"
print(str1)


# ! ------> dictionary
# eg:1
d1 = {1:100, 'a':200, 4.5:"hllo"}
marks_stud1 = {"English": 79, "maths":20, "physics": 60}

print(d1)
print(len(d1))

# ? char of dictionary
1.) have to be surrounded by {}
2.)it have to be in the form of key, value pair
3.) it is mutable
4.) duplicate keys are not allowed,duplicate values are allowed
5.) it is unindexed
6.) it s ordered
7.) key does not allow mutable datatypes, values allow mutable datatype

d1 = {1:100, 2:200, 3:300,4:400}
# * to access element in dictionary

print(d1)
or
to access the values, have to use key 
print(d1[1]) # o/p --> 100

# ? som common functions
len(), min(), max()
print(min(d1))
print(max(d1))

# ? to find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

# ? dictionary based functions
to add element(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

# ? to replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}



join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple", "b":"boy", "g":"game"}
d1.update(d2)
print(d1)

get() ----> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))

to print all the keys()
print(d1.keys())
print(type(d1.keys()))

to print all the values
print(d1.values())

# * iterating dictionary
for val in d1: # to  iterate values alone
    print(val)
for val in d1.values(): # to iterate values alone
    print(val)

to get both key and values
for key, val in d1.items():
    print(key, val)



# ! ------> problem:1
n = int(input("Enter the value: "))
integer=[]
float_value =[]
string=[]

for val in range(n):
    value = eval(input("Enter the values: "))
    if typ(val)==int:
        integer.appnd(val)
    elif type(val) == float:
        float_value.appnd(value)
    elif type(value) == str:
        string.append(value)
    else:
        print("pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)


# ! ---> problem:2

Return a set of elements present in set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
        
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''
# ! -----> problem 3

l1 = [1,2,3,4] # key
l2 = ["a", "b", "c", "d"] # value
# ? o/p --> {1:'a', 2:'b', 3:'c', 4:'d'}


# ! or
c = 0
for val in set1, set2:
    c=c+1
    if c==1:
        for element in val:
            if element not in set2:
                set3.add(element)
print(set3)


o/p
# {20, 70, 10, 60}


 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']








    
