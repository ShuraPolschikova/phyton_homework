calls=0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    my_string=str(string)
    result=(len(my_string),my_string.upper(),my_string.lower())
    count_calls()
    return result
def is_contains(string,list_to_search):
    string=str(string).lower()
    list_to_search=list(list_to_search)
    count_calls()
    for i in range (len(list_to_search)):
        if str(list_to_search[i]).lower()==string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info("YAUMAMYprogrammist"))
print(string_info("no eto poka ne TOCHNO..."))
print(string_info("budem staraCA"))
print(is_contains("black",["white", "orange", "green", "black", "red"]))
print(is_contains("subaru",["audi", "BMW", "volkswagen", "mers"]))
print(calls)