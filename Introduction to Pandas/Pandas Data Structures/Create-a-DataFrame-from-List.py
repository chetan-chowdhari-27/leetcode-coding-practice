# 2877. Create a DataFrame from List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ('student_id', 'age')
    student_data = pd.DataFrame(student_data, columns = column_names)
    return student_data

