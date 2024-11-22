#Q1 convert triangle code to use while loop

#og code
#tri_dem = int(input("Enter triangle dimensions: "))
#for x in range(1,tri_dem+1):
 #   tri = "*" * x
  #  print(tri)


tri_size = int(input("Enter triangle size: "))
t =  1
while t < tri_size+1:
    triangle = "*" * t
    print(triangle)
    t +=1