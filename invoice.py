# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19hh-BODHNYWk0biCEKGVdsFk_SKHk4ca

# **IMS**
## *Inventory Management System*
TO Generate Invoice of Sales
"""

import json

sales_file= open("Sales.json","r")
Sales = sales_file.read()
Sales = json.loads(Sales)
sales_file.close()

Sales

#Menu for invoice generation

print('<----------------------------------------- Welcome to Invoice Generator  --------------> \n Input 1 To print particular Invoice \n Input 2 To Print list of all Invoices')
choice = int(input("Enter your Input : "))

if choice == 1:
  #Printing particular Invoice
  invoice = input("Enter Invoice Number! : ")
  if invoice not in Sales.keys():
   print(invoice +"Id  Invoice Not Found!")
  else:
   our_invoice = Sales[invoice]
   print("ID: ",invoice)
   print("Invoice Date: ",our_invoice['date'])
   print("Items:- \n")
   sno=1
   inv_total=0
   for item in our_invoice['items']:
     print("S no. \t \t Name \t \t \t Quantity \t \t \t  Total \n")
     print(sno , "\t \t ",item['name']," \t ",item['quantity']," \t \t \t \t  ",item['total'],"\n")
     sno +=1
     inv_total +=item['total']
   print("----------------------------------------------------------------------------------------")
   print("\t  \t  \t  \t  \t  \t \t \t Net Total:",inv_total)

elif choice == 2:
  #Printing lit of all invoices

  print("All invoices are as Follows : \n")

  for invoice in Sales.keys():
    invoice_data = Sales[invoice]
    #print(len(invoice_data['items']))
    print("\n Invoice ID :"+invoice+" \t \t \t \t \t \t Date: "+invoice_data['date']+"\n Total Items: ",len(invoice_data['items']))
    print("\n <----------------------------------------------------------------------------------> \n")