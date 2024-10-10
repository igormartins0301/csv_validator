# %%
import random

import pandas as pd
from faker import Faker

fake = Faker()


def generate_sales_data(num_records):
    sales_data = []
    categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Food']

    for _ in range(num_records):
        sale_id = fake.uuid4()
        sale_date = fake.date_between(start_date='-1y', end_date='today')
        product_id = fake.uuid4()
        product_name = fake.word().capitalize()
        category = random.choice(categories)
        quantity = random.randint(1, 20)
        unit_price = round(random.uniform(5.0, 500.0), 2)
        total_price = round(quantity * unit_price, 2)
        customer_id = fake.uuid4()
        customer_name = fake.name()
        country = fake.country()

        sales_data.append({
            'sale_id': sale_id,
            'sale_date': sale_date,
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_price': total_price,
            'customer_id': customer_id,
            'customer_name': customer_name,
            'country': country,
        })

    return pd.DataFrame(sales_data)


# Gerar 1000 registros de vendas e salvar em CSV
df = generate_sales_data(1000)
df.to_csv('sales_data.csv', index=False)
