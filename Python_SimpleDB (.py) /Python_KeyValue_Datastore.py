#!/usr/bin/env python
# coding: utf-8

# In[92]:


# SimpleDB using Dictionary, list and key:values 
# For this we only use a json import to read and write to/from file, 
# and Python's own Dictionary object. 
import json

# We define our dictionary "{}" and list "[]" and populate them. 
datastore = { "office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "office",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}


# In[97]:


# Accessing and printing data from a specific dictionary object can be done, 
# like with "parking"
print(datastore["office"]["parking"])


# In[100]:


# Knowing that the value for "medical" is a list. 
# We can then use index numbers ie. "[2]" to access specific room-data, 
# based on our entries.

print(datastore["office"]["medical"][1])


# In[103]:


# Assigning a portion of the datastore to a variable to efficiently address it. 
spaces = datastore['office']['medical']


# In[104]:


# Here is a method to find and change a value in the database.
for item in spaces:
    if item.get('use') == "examination" :
       item['price'] = ('250€')

# Finding the entry and printing new value, new change of 'price' is now stored in the DB.
for item in datastore['office']['medical']: 
    if item.get('use') == "examination" :
        print('The {} room now costs {}'.format(item.get('use'), item.get('price')))


# In[90]:


# Creating a file and dumping all data. 
with open("medicaloffice.json","w") as f:
    json.dump(my_data,f)
f.close()


# In[91]:


# Opening created and updated file(if changes were made in the db) 
# and prints all stored data.
with open("medicaloffice.json","r",) as f:
    jsondata=json.load(f)
    print(jsondata)
f.close()


# In[ ]:




