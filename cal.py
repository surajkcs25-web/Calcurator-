inp=input()
strnb=""
oprtr=[]

for ch in inp:
    if ch in "+-*/":
        oprtr+=ch
        strnb+=','
    else:
        strnb+=ch     
nbs=list(map(int,strnb.split(",")))


i=0
while i<(len(oprtr)):
    if oprtr[i]=='/':
        nbs[i]=nbs[i]/nbs[i+1]
        nbs.pop(i+1)
        oprtr.pop(i)

    elif oprtr[i]=='*':
        nbs[i]=nbs[i]*nbs[i+1]
        nbs.pop(i+1)
        oprtr.pop(i)

    elif oprtr[i]=='+':
        nbs[i]=nbs[i]+nbs[i+1]
        nbs.pop(i+1)
        oprtr.pop(i)

    elif oprtr[i]=='-':
        nbs[i]=nbs[i]-nbs[i+1]
        nbs.pop(i+1)
        oprtr.pop(i) 

    else:
        i+=1   

print(nbs[0])
