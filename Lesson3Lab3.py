print("___________________________________________")
for i in range(1, 11):
    print("|", i, end=" ")
    for j in range(1, 11):
        print("{:3d}".format(i * j), end=" ")
    print("\t|")
print("___________________________________________")