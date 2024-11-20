from Test_Miller_Rabin import test_MR

if __name__=="__main__":
    range_value=10**6
    lis=[]
    for i in range(0,range_value):
        res=test_MR(i,20)
        if res:
            lis.append(i)
            print(i)
    print(len(lis))
    