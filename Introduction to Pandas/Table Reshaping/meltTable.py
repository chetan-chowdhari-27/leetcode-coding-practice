import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Use pandas.melt to reshape the DataFrame
    melted_df = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                        var_name='quarter', value_name='sales')
    return melted_df
