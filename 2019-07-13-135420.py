#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# In[9]:


games= ''
while games== '':
    games= int(input('please choose a number:'))
    
    
    
for game in range(games):
    pick= None
    attempts= 0
    
    
    real = random.randint(1, 26)
    
    while real != pick:
        pick= int(input('pick a number'))
        attempts +=1
        
        if real != pick:
            if real > pick:
                print('high')
            else:
                print('low')
                
        else:
            print('lucky in %s' %attempts)
        


# In[ ]:




