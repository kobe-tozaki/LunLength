txt1=input("input : ")
txt2=[]
w1=txt1[0]
n=1
for i in txt1[1 : ]:
    if w1==i:
        n+=1
    else:
        txt2+=i
        txt2+=str(n)
        n=1

# 注釈
print(f" 圧縮前: {txt1} --> 圧縮後: {txt2}")