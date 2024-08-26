immutable_var=("К",7,7,7,"О","Т",True)
print(immutable_var)
# immutable_var[0]="P"
# print(immutable_var) #изменение невозможно, так как нужно создать изменяемый список, а не кортеж)
mutable_list=["К",7,7,7,"О","Т",True]
print(mutable_list)
mutable_list[0]="S"
mutable_list[-2]="N"
print(mutable_list)