
# coding: utf-8

# In[5]:

with open("/Users/simonwager/ROSALIND/Python_Village/05_rosalind_ini5.txt", 'r') as f:
    content = f.read()

all = content.split('\n')
odd = []
for i in range(0, len(all)):
    if i%2 == 1:
        odd.append(all[i])
fin = "\n".join(odd)
print(fin)


# In[ ]:



