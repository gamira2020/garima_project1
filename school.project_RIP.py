import pandas as pd

while True:
    print("what do you want to do:")
    print("1.Add Electronic Item")
    print("2.Add Customer Orders")
    print("3.Show Stock and Customer Data")
    print("4.Delete an Item")
    print("5.Exit")
    select_choice = input("enter choice: ")
    if select_choice == "1":
        try:
            stock = pd.read_csv("stock.csv")
        except FileNotFoundError:
            stock = pd.DataFrame(columns=['Item', 'Quantity', 'Price per Item'])
            stock.to_csv("stock.csv", index=False)
        u_item = input('enter electronic item: ')
        stock_quantity = input('enter quantity: ')
        u_price = input('enter price: ')
        stock.loc[len(stock)] = [u_item, stock_quantity, u_price]
        stock.to_csv("stock.csv", index=False)
        print(u_item,'and details are added.')
    elif select_choice == "2":
        try:
            customers=pd.read_csv("customers.csv")
            stock = pd.read_csv("stock.csv")
        except FileNotFoundError:
            customers=pd.DataFrame(columns=['Customer','Item','Quantity','City'])
            customers.to_csv("customers.csv",index=False)
            stock = pd.DataFrame(columns=['Item', 'Quantity', 'Price per Item'])
            stock.to_csv("stock.csv", index=False)
        u_name=input("enter customer name: ")
        u_item=input('enter electronic item: ')
        customer_purchased_quantity=int(input('enter purchased quantity: '))
        u_city=input('enter city: ')
        selected_item=stock.loc[stock['Item']==u_item]
        stock_quantity = selected_item['Quantity'].values.sum()
        # WIP item filter done , customer filter left
        if selected_item.empty == False:
            if customer_purchased_quantity <= stock_quantity:
                stock.loc[selected_item.index, 'Quantity'] = stock_quantity - customer_purchased_quantity
                customers.loc[len(customers)] = [u_name, u_item, customer_purchased_quantity, u_city]
                customers.to_csv("customers.csv",index=False)
                stock.to_csv("stock.csv", index=False)
                print(u_name,'and their order details are added.')
            else:
                print(customer_purchased_quantity,"no. of ",u_item,"\bs are not available.")
        else:
            print(u_item,"Stock not available for purchase currently.")
    elif select_choice == "3":
        print("Which Data do you want to view:")
        print("1.Stock Details")
        print("2.Customer Orders")
        choice = input("enter choice: ")
        if choice == "1":
            try:
                stock = pd.read_csv("stock.csv")
            except FileNotFoundError:
                stock = pd.DataFrame(columns=['Item', 'Quantity', 'Price per Item'])
                stock.to_csv("stock.csv", index=False)
            if stock.empty == True:
                print('no items available.')
            else:
                print(stock, '\n')
        elif choice == "2":
            try:
                customers = pd.read_csv("customers.csv")
            except FileNotFoundError:
                customers = pd.DataFrame(columns=['Customer', 'Item', 'Quantity', 'City'])
                customers.to_csv("customers.csv", index=False)
            if customers.empty == True:
                print('no order records yet.')
            else:
                print(customers, '\n')

    elif select_choice == "4":
        try:
            stock=pd.read_csv("stock.csv")
            customers = pd.read_csv("customers.csv")
        except FileNotFoundError:
            stock=pd.DataFrame(columns=['Item','Quantity','Price per Item'])
            stock.to_csv("stock.csv",index=False)
            customers = pd.DataFrame(columns=['Customer', 'Item', 'Quantity', 'City'])
            customers.to_csv("customers.csv", index=False)
        u_item=input('Name the item which is to be deleted:')
        selected_item_stock=stock.loc[stock['Item']==u_item]
        selected_item_customers=customers.loc[customers['Item']==u_item]
        if selected_item_stock.empty==False:
            stock=stock.drop(selected_item_stock.index)
            customers=customers.drop(selected_item_customers.index)
            stock.to_csv("stock.csv",index=False)
            customers.to_csv("customers.csv",index=False)
            print(u_item,"and its details are deleted.")
        else:
            print(u_item,"doesn't exist in data.")
    else:
        break