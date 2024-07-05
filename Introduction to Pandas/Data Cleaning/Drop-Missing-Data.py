# 2883. Drop Missing Data

import pandas as pd
import numpy as np

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.replace(['null', 'None'], np.nan, inplace=True)
    students = students.dropna(subset=["name"],axis=0,how='any')
    return students