#!/usr/bin/env python
# coding: utf-8

# In[1]:


from MySetClass import *
# %matplotlib inline
# import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'qt5')


deck = createDeck()
table, deck = generateTableBeginning(deck)

scoreP = 0
scoreC = 0 

# %matplotlib inline

showTable(table)
# while len(deck) > 0
# table, scoreP = playersTurn(table, scoreP)


# In[2]:


# %matplotlib inline
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

while len(deck) > 0: 
    # %matplotlib inline
    table, scoreP, errM = playersTurn(table, scoreP)
    if errM == 'Problem':
        break
    table, setOrNot, scoreC = computersTurn(table, scoreC)
    # %matplotlib inline
    # fig.canvas.draw()
    if setOrNot == False:
        print('Cards were added to the table.')
        table, deck, errMsg = hitMe(table, deck)
        showTable(table)
    showTable(table)
    print('Length of deck is', len(deck))
    print('Length of table is', len(table))
    print('Player score is', scoreP)
    print('Computer score is', scoreC)


# In[ ]:


while setInTable(table) == True:
    showTable(table)
    table, scoreP, errM = playersTurn(table, scoreP)
    if errM == 'Problem':
        break
    table, setOrNot, scoreC = computersTurn(table, scoreC)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




