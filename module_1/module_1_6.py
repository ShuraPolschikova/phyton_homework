my_dict={"Shura": "28.06.1996"}
print(my_dict)
print(my_dict["Shura"])
my_dict["Nastja"]="28.03.1990"
print(my_dict["Nastja"])
my_dict.update({"Mama": "21.11.1966", "Papa": "09.11.1965", "Sonya":"18.11.1999"})
lost=my_dict.pop("Nastja")
print(lost)
print(my_dict)
my_set={2,8,0,6,1,9,9,6, "S","h","a","l","a","s","h", ("Shura")}
print(my_set)
my_set.add("Z")
my_set.add(7)
my_set.discard("Shura")
print(my_set)