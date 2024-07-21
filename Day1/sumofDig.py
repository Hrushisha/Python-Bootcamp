# sum of digits from string 
#s='a1b2c3'


s=input()
sum=0
for i in range(0,len(s)):  #index starts from 0
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)        


