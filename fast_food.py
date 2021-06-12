import pandas as pd
import json
from pymongo import MongoClient

# function built in jupyter notebook and copied here
def load_data():
    #
    fast_food = pd.read_csv("restaurants.csv")
    fast_food.head()
    # In[3]:
    fast_food = fast_food[["address", "latitude", "longitude", "name", "province", "city"]]
    fast_food
    # In[4]:
    fast_food = fast_food.rename(columns={"province": "state"})
    fast_food
    # In[5]:
    fast_food.isnull().sum()
    # In[6]:
    fast_food.dtypes
    # In[7]:
    names_standardized = []
    # https://stackoverflow.com/questions/55902042/python-keep-only-alphanumeric-and-space-and-ignore-non-ascii
    values = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789 ")
    #
    for index, row in fast_food.iterrows():
        for character in row["name"]:
            if character not in values:
                row["name"] = row["name"].replace(character, "")
        row["name"] = row["name"].title()
        names_standardized.append(row["name"])

    fast_food["name"] = names_standardized
    fast_food["name"]
    # In[8]:
    fast_food_dict = fast_food.to_dict(orient="records")
    # In[9]:
    fast_food.to_csv("fast_food.csv", index=False)
    # In[10]:
    myclient = MongoClient("mongodb://localhost:27017/")
    myclient.drop_database("fastfood")
    # database 
    db = myclient["fastfood"]
    # Created or Switched to collection
    collection = db["collection"]
    # In[11]:
    collection.insert_many(fast_food_dict)
    # In[ ]:




