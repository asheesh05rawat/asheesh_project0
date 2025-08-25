

info ={
    "name":"asheesh",
    "ages":23,
    "arrays":["mohan","ram","raj","akash"],
    
}

print(info)
# type of dictionary-------
print(type(info))


# accessing elements of dictionary -----------
print(info["ages"])
print(info["arrays"])


# adding a new  key in dictionnary------------
info["caste"]="general"
print(info)

#---NESTED DICTIONARYS----------
dict={
   "student":"rawat ji ",
   "subjects":{
       "phy":97,
       "chem":85,
       "maths":100,
   }
}
print(dict)











i={
  "table" :["books","pens"],
  "cat":"animal",
}
print(i)

list={"c","c++","python","java","javascript","html","c","c++","c++"}
classroom = len(list)
print(list)
print("number of classes required as 1 class per subject is = ",classroom)
