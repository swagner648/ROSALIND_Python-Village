
# coding: utf-8

# In[13]:

with open("/Users/simonwager/ROSALIND/Python_Village/04_rosalind_ini4.txt", 'r') as f:
    content = f.read()

file1 = content.split('\n')
file = file1[0].split(' ')
sum = 0
for i in range (int(file[0]), int(file[1])+1):
    if (int(file[0]) + i) % 2 == 1:
        sum = sum + i
print(sum)


# In[ ]:



