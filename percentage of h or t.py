import random
numberofstreaks = 0
streaks = 0
for exp in range(10000):
    prob = []
    for x in range(100):
        if random.randint(0,1)==0:
            prob.append('heads') 
        else:
            prob.append("tails")

    for x in range(len(prob)):
        if prob[x]==prob[x-1]:
            streaks+=1
        else:
            streaks =0
            
        if streaks ==6:
            numberofstreaks += 1
            
            
print('Chance of streak: %s%%' % (numberofstreaks / 100))
    
    
