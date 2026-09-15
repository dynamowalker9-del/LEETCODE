import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    if employee.empty:
        return pd.DataFrame({'Employee': []})
    merged_df = employee.merge(
        employee, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )
    result_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]
    return result_df[['name_emp']].rename(columns={'name_emp': 'Employee'})
