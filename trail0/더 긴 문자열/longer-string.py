A, B = input().split()
if(len(A) > len(B)):
    print(A, len(A))
elif(len(B) > len(A)):
    print(B, len(B))
else:
    print('same')