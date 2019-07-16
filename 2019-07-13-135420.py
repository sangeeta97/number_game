#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# In[9]:


games= ''
while games== '':
    games= int(input('please choose number of games:'))
    
    
    
for game in range(games):
    pick= None
    attempts= 0
    
    
    real = random.randint(1, 26)
    
    while real != pick:
        pick= int(input('pick a number between 1 to 25'))
        attempts +=1
        
        if real != pick:
            if real > pick:
                print('number is lower')
            else:
                print('number is higher')
                
        else:
            print('lucky in %s guesses' %attempts)
        


# In[ ]:




