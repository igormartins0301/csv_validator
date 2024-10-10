# %%
import pandera as pa
from pandera import Check, Column

sales_schema = pa.DataFrameSchema({
    'sale_id': Column(str, checks=Check.str_length(36)),
    'sale_date': Column(pa.DateTime),
    'product_id': Column(str, checks=Check.str_length(36)),
    'product_name': Column(str),
    'category': Column(
        str,
        checks=Check.isin([
            'Electronics',
            'Clothing',
            'Books',
            'Furniture',
            'Food',
        ]),
    ),
    'quantity': Column(int, checks=Check.greater_than(0)),
    'unit_price': Column(float, checks=Check.greater_than(0)),
    'total_price': Column(float, checks=Check.greater_than(0)),
    'customer_id': Column(str, checks=Check.str_length(36)),
    'customer_name': Column(str),
    'country': Column(str),
})
