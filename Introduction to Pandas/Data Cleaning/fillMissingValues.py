import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    replace_null = ['None', 'null']
    products['quantity'] = products['quantity'].replace(replace_null, 0)
    products['quantity'] = products['quantity'].fillna(0)
    return products