"""

#length functions
a = len("sai_sundhar")
print(a)

#string  transform functions(casee conversions)
#capatalise
a = "DHONI"
print(a.capitalize())

#title

a = "DHONI"
print(a.title())

#upper

a = "DHONI"
print(a.upper())


#lower

a = "C"
print(a.lower())

#Caseefold

a = "DHONI"
print(a.casefold())

#SWAPCASE

a = "dhoni"
print(a.swapcase())


#string check funnctions

#isnumeric

a = "DHONI"
print(a.isnumeric())

#isalpha
a = "DHONI"
print(a.isalpha())

#isdecemial

a = "456987"
print(a.isdecimal())


#isddigit
a = "456987"
print(a.isdigit())

#isasscill

a = "456987"
print(a.isascii())

#isupper
a = "dhoni"
print(a.isupper())

#islower

a = "456987"
print(a.islower())


#isspace

a = "456987"
print(a.isspace())

#isidentifers

a = "456987"
print(a.isidentifier())

#isprintable

a = "456987"
print(a.isprintable())

#string search functions

#index
 a.index(char\string)

#r-index

a.rindex(char\string)

#find

a.findchar\string)

#rfinnd
a.rfind(char\string)

#starts with
a.startswithchar\string)

#endswith
a.endswithchar\string)


 #list methods

 #append
lst =  []
lst.append("sai")
print(lst)


#insert

name = ["sai","dhoni"]
print(name.insert(0,"sai"))


#count
name = ["sai","dhoni"]
print(name.count("dhoni"))



attendences = ["dhanunjai" ,"sai","sundhar"]
if print(attendences.count("sai")> 0):
    print(attendences)


#by using index
attendences = ["dhanunjai" ,"sai","sundhar"]
attendences[1] = ["sundhar"]
print(attendences)

#extend
attendences = ["dhanunjai" ,"sai","sundhar"]
attendences1 = ["sundhar"]
attendences.extend(attendences1)
print(attendences)
print(attendences1)


#remove

b = ["dhanunjai" ,"sai","sundhar"]
b.remove("dhanunjai")
print(b)

#pop eith index
b = ["dhanunjai" ,"sai","sundhar"]
b.pop(1)
print(b)


#pop without index
b = ["dhanunjai" ,"sai","sundhar"]
b.pop()
b.pop()
b.pop()
print(b)

#clear

a = ["dhanunjai","sai","sundhar"]
print(a.clear())
print(type(a))
print(a)

#delete

a = ["dhanunjai","sai","sundhar"]
del a[1]
print(a)



a1 = input("enter a1 name:")
a2 = input("enter a2 name:")
a3 = input("enter a3 name:")

a.append(a1)
a.append(a2)
a.append(a3)
print(a)


#sort
lst = [1,2,6,5,8,66,99,52,1008]
lst.sort()
print(lst)

#reverse

lst = [1,2,6,5,8,66,99,52,1008]
lst.reverse()
print(lst)

#tuple


#index
tpl =tuple((1,2,53,6,2,2,2,5,6,99,99))
print(tpl.index(5))
print(tpl.index(99))

#count

tpl =tuple((1,2,53,6,2,2,2,5,6,99,99))
print(tpl.count(5))


#add

a : set = {'1','2','3'}
a.add('66')
print(a)

#update
a : set = {'1','2','3'}
b : set = {'d','s','s'}
a.update(b)
print(a)  #duplicates not allowed



#remove

a : set = {'1','2','3','6','100'}
a.remove('6')
print(a)

#discard
a : set = {'1','2','3','6','100'}
a.discard('p')
print(a)


#pop
a : set = {'a','f'}
a.pop()
print(a)


#union

a : set = {'1','2','3','6','100'}
b : set = {'a','f'}
s = a.union(b)
print(s)



#intersection


a : set = {'1','2','3','6','100'}
b : set = {'a','f','2','100'}
s = a.intersection(b)
print(s)


#interseection_update

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
(names1.intersection_update(names2))
print(names1)
print(names2)

#isdisjoint
names1 = {'A'}
names2 = {'Mahendra','singh','dhoni'}
print(names1.isdisjoint(names2))

#differences

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.difference(names2))

#symmetric_differences
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.symmetric_difference(names2))


#symmetric_differences_update
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
(names1.intersection_update(names2))
print(names1)
print(names2)


#isubset

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'sai'}
print(names2.issubset(names1))


#issuperset


names1 = {'dhoni'}
names2 = {'mahendra','singh','dhoni'}
print(names1.issuperset(names2))


#frozen_methods
#union

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.union(names2))

#intersection


names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.intersection(names2))

#isdisjoint


names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.isdisjoint(names2))

#differences

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.difference(names2))

#symmetric_differences
names1 = {'dhanunjai','sai','sundhar'}
names2 = {'mahendra','singh','dhoni'}
print(names1.symmetric_difference(names2))

#isubset

names1 = {'dhanunjai','sai','sundhar'}
names2 = {'sai'}
print(names2.issubset(names1))


#issuperset


names1 = {'dhoni'}
names2 = {'mahendra','singh','dhoni'}
print(names1.issuperset(names2))


"""

#frozen sets
# union
# syntax = varablename.union(variable)
#
# intersection
# syntax = varablename.intersection(variable)
#
# isdisjoint
# syntax = varablename.isdisjoint(variable)
#
# differences
# syntax = varablename.isdifferences(variable)
#
# symmetric_differences
# syntax = varablename.symmetric_differences(variable)
#
# issubset
# syntax = varablename.issubset(variable)
#
# issuperset
# syntax = varablename.issubset(variable)
#
#
# copy
# syntax = varablename.copy(variable)

