dict1 = {'Alice':85,'Bob':80,'Marley':75}
a = input("Enter the student's name: ")
for key in dict1.keys():
    if a in dict1:
        print("{}'s marks is:".format(key),dict1[a])
        break
    else:
        print("Student not found")
        break
