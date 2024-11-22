#Q3 ask user for size of the triangle and print a right angle triangle

tri_dem = int(input("Enter triangle dimensions: "))

for x in range(1,tri_dem+1):
    tri = "*" * x
    print(tri)