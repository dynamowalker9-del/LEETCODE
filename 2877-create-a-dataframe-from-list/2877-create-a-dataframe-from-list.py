import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    y=pd.DataFrame(student_data)
    y.columns=["student_id","age"]
    return y