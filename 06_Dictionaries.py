
# coding: utf-8

# In[18]:

with open("/Users/simonwager/ROSALIND/Python_Village/06_rosalind_ini6.txt", 'r') as f:
    content = f.read()

file = content.split('\n')
file2 = ' '.join(file)
senls = file2.split(' ')
dict = {}
m = 0
for i in senls:
    if i == "":
        senls.remove(i)
for word in senls:
    n = 0 # word count
    for i in range(0, len(senls)):
        if senls[m] == senls[i]:
            n = n+1
    dict[word] = n
    m = m+1
for key, value in dict.items():
    print(key, value)


# In[ ]:




# In[ ]:



