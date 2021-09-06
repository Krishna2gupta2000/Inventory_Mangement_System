# -*- coding: utf-8 -*-
"""Untitled.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11xzBO0tXWluD0H_RSxQegFvsNc4noV6Y

# **IMS**
## *Inventory Management System*

TO ADD PRODUCT INTO INVENTORY
"""

### ADD Inventory

import json

f= open("records.json","r")
readata = f.read()
records = json.loads(readata)
num_add = int(input("How many product you want to Add Record! \n Be carefull about name spelling while input \n  "))
counter_id = len(records) +1000

lst_store =[]

for i in range(num_add):
    prod_name = input("Enter Product name: ")
    qty = int(input("Enter quantity: "))
    price = int(input("Enter Price: "))
    category = input("Enter Category: ")
    weight = float(input("Enter the weight in Kg: "))
    store = {"name":prod_name,"quantity":qty,"Price":price,"Category":category,"Weight":weight}
    lst_store.append(store)
    print("\n <--------------------------------------------------------------------> \n")

lst_store

for check in lst_store:
  new =1
  for record in records.values():
    if(record['name'].lower() == check['name'].lower()):
      record['quantity'] += check['quantity']
      new = 0
  if(new==1):
    records[str(counter_id)]={"name":check['name'],"quantity":check['quantity'],"Price":check['Price'],"Category":check['Category'],"Weight":check['Weight']}
    counter_id += counter_id


  

#record.update({counter_id:{"name":prod_name,"quantity":qty,"Price":price,"Category":category,"Weight":weight}})

f = open("records.json","w")
save = json.dumps(records)
f.write(save)
f.close()

f= open("records.json","r")
readata = f.read()
rec = json.loads(readata)
rec

for i in rec.values():
  print("Name : ",i["name"])
  print("Quantity : ",i["quantity"])
  print("Price : ",i["Price"])
  print("Category : ",i["Category"])
  print("Weight : ",i["Weight"])
  print("\n <--------------------------------------------------------------------> \n")