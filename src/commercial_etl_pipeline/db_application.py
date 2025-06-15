import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

Faker.seed(42)
np.random.seed(42)

def accounts(n):

    accounts = []

    account_id = np.arange(start=1000, stop=1000+3* n, step=3)

    for i in range(n):

        account = {
            'account_id': account_id[i],
            'name': fake.name(),
            'birthday': fake.date_of_birth(minimum_age=18, maximum_age=95),
            'create_at': fake.date_between(start_date="-5y", end_date='-1w'),
            'cancelated_account': np.random.choice([True,False],p=[0.85,0.15]),
            'address': fake.address().replace('\n', ' '),
            'job': fake.job(),
            'phone': fake.phone_number(),
            'iban': fake.iban()
        }
        
        accounts.append(account)
    
    return(pd.DataFrame(accounts))

def orders(n, account_ids ,product_ids):

    orders = []
    
    order_id = np.arange(start=5555, stop=5555+3*n, step=3)

    for i in range(n):

        number_of_products = np.random.randint(low=1, high=25)
        sold_unit_price = np.random.randint(low=45,high=200)

        order = {
            'order_id': order_id[i],
            'account_id': np.random.choice(account_ids),
            'product_id':np.random.choice(product_ids),
            'number_of_products': number_of_products,
            'sold_unit_price': sold_unit_price,
            'price': number_of_products * sold_unit_price,
            'order_date': fake.date_between(start_date='-5y', end_date='-1w')
        }

        orders.append(order)

    return(pd.DataFrame(orders))

def products():
    product_name_price = {
        'Keyboard': 120, 
        'Mouse': 65, 
        'External Monitor': 540, 
        'USB Flash Drive': 12, 
        'External Hard Drive': 100,
        'Docking Station': 760,
        'PrinterScanner': 450
    }

    products = []
    product_id = np.arange(start=7777, stop=7777 + 5 * len(product_name_price), step=5)

    for i, (name, price) in enumerate(product_name_price.items()):
        product = {
            'product_id': product_id[i],
            'product_name': name,
            'stock_quantity': np.random.randint(low=1, high=1000),
            'unit_price': price
        }
        products.append(product)

    return pd.DataFrame(products)
