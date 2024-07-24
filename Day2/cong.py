#in this we use only valid words 
cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
     }
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2,
    }
    #above 18 age should be consider for the partiesfiltered_cong = filter_above_18(cong)


cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
diff=abs(cong_sum-bjp_sum)        #abs absolute it is a function
if cong_sum>bjp_sum:
    print('cong win:',diff)
else:
    print('bjp win:',diff)            



