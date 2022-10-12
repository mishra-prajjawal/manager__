with open("tlds-alpha-by-domain.txt","r") as src : 
    a = src.readlines()
    ls = [] 
    for i in a :
        ls.append("."+i.strip().lower())
print(ls)
