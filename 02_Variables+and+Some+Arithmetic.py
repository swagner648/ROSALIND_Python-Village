
# coding: utf-8

# In[8]:

with open("/Users/simonwager/ROSALIND/Python_Village/02_rosalind_ini2.txt", 'r') as f:
    content = f.read()

a = int((content.split(" "))[0])
b = int((content.split(" "))[1])
c = a*a + b*b
print(c)


# In[ ]:



