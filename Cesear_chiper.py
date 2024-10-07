import sys
ALFABETH=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def simple_cesear(m):
    lis=[]
    for i in range(0, len(m)):
        for j in range(0, len(ALFABETH)):
           if m[i]==ALFABETH[j]:
               if j+3>25:
                index=(j+3)-26
                lis.append(ALFABETH[index])
               else:
                lis.append(ALFABETH[j+3])
    return "".join(lis)

def K_cesear(m,k):
    lis=[]
    for i in range(0, len(m)):
        for j in range(0, len(ALFABETH)):
           if m[i]==ALFABETH[j]:
               if j+k>25:
                index=(j+k)-26
                lis.append(ALFABETH[index])
               else:
                lis.append(ALFABETH[j+k])
    return "".join(lis)


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to secure")
        sys.exit()
    n = sys.argv[1] #Value to check
    lis=simple_cesear(n)
    lis_k=K_cesear(n,10)
    print(lis, lis_k)