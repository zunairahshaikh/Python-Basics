#a
def Unknown(X,Y):
    X = int(X)
    Y = int(Y)
    if X < Y:
        print(X+Y)
        return Unknown(X+1,Y)*2
    elif X==Y:
        return 1
    else:
        print(X + Y)
        return Unknown(X - 1, Y)% 2

#bi
call1 = Unknown(10,15)
print(call1)
call2 = Unknown(10,10)
print(call2)
call3 =Unknown(15,10)
print(call3)

print()

#c
# def IterativeUnknown(X,Y):
#     total = 1
#     X = int(X)
#     Y = int(Y)
#     print(X + Y)
#     if X ==Y:
#         return total
#     elif X<Y:
#         X+=1
#         total*=2
#         return total
#     else:
#         X-=1
#         total = total %2
#         return total
#
# sq = IterativeUnknown(10,15)
# print(sq)

