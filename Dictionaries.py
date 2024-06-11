customer={
    "name":"Gagan \n",
    "age":30,
    "is_varifies":True
}

# print(customer.get("Age","22 Years"))

# we can update 

customer["name"]="Kumar"

# print(customer.get("name"))


# convert a numbr into a words

phone=input("phone: ")
digits_map={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output+=digits_map.get(ch,"!NONE")+" "
print(output)