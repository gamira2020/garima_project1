import pandas as pd

while True:
    print("what do you want to do:")
    print("1.add electronic item")
    print("2.show recent electroic item order")
    print("3.delete item")
    print("exit")
    select_choice=input("enter choice: ")
    if select_choice=="1":
        try:
            eitem=pd.read_csv("eitem.csv")
        except FileNotFoundError:
            eitem=pd.DataFrame(columns=['Item','Quantity','Price','City'])
            eitem.to_csv("eitem.csv",index=False)
        u_item=input('enter electronic item: ')
        u_quantity=input('enter quantity: ')
        u_price=input('enter price: ')
        u_city=input('enter city: ')
        eitem.loc[len(eitem)]=[u_item,u_quantity,u_price,u_city]
        eitem.to_csv("eitem.csv",index=False)
        print(f'{u_item} and details are added.')
        
    elif select_choice=="2":
        try:
            eitem=pd.read_csv("eitem.csv")
        except FileNotFoundError:
            eitem=pd.DataFrame(columns=['Item','Quantity','Price','City'])
            eitem.to_csv("eitem.csv",index=False)
        if eitem.empty==True:
            print('no items available')
        else:
            print(eitem,'\n')
    elif select_choice=="3":
        try:
            eitem=pd.read_csv("eitem.csv")
        except FileNotFoundError:
            eitem=pd.DataFrame(columns=['Item','Quantity','Price','City'])
            eitem.to_csv("eitem.csv",index=False)
        u_item=input('Name the item which is to be deleted:')
        u_quantity=input('number of items to be deleted:')
        selected_item=eitem.loc[eitem['Item']==u_item]
        if selected_item.empty==False:
            eitem=eitem.drop(selected_item.index)
            print(f'{eitem})
    else:
        break    
