s=input()
s_new= ""
for i in range(len(s)) :
    if s[i] == "э":
        s_new+= "е"
    else:
        s_new+= s[i]
print(s_new)