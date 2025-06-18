import pandas as pd
from db_application import accounts, orders,products
from db_connection import db_connection
from sqlalchemy.exc import SQLAlchemyError


engine = db_connection()

def load_data():
    
    tbl_accounts = accounts(500)
    tbl_products = products()
    tbl_orders = orders(n=10000, account_ids=tbl_accounts['account_id'], product_ids=tbl_products['product_id'].tolist())

    try:
        tbl_accounts.to_sql(name='tbl_accounts', con=engine, if_exists='replace', index=False)
        tbl_products.to_sql(name='tbl_products', con=engine, if_exists='replace', index=False)
        tbl_orders.to_sql(name='tbl_orders', con=engine, if_exists='replace', index=False)

    except SQLAlchemyError as e:
        print(f'An error occorred while writing to SQL: {e}')

if __name__ == "__main__":
    load_data()
