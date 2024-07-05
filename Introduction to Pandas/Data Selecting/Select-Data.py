# 2880. Select Data

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    filtered_stu = students[students.student_id == 101]
    return filtered_stu[["name", "age"]]
