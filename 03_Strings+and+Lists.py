
# coding: utf-8

# In[12]:

with open("/Users/simonwager/ROSALIND/Python_Village/03_rosalind_ini3.txt", 'r') as f:
    content = f.read()

file = content.split("\n")
num = file[1].split(" ")
print(file[0][int(num[0]):int(num[1])+1], file[0][int(num[2]):int(num[3])+1])


# In[ ]:



