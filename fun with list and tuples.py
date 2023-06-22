#!/usr/bin/env python
# coding: utf-8

# In[1]:


def last(n):
    return n[-1]
def sort_list_last(tuples):
    return sorted(tuples,key=last)
print(sort_list_last([(2,5),(1,2),(2,3),(3,1),(4,3)]))


# In[ ]:




