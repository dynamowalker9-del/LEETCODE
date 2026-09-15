import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    count = person['email'].value_counts()
    
    return count[count > 1].reset_index()[['email']].rename(
        columns={'email': 'Email'}
    )

Person={
    'email':['a@b.com','c@d.com','a@b.com']
}
df3=pd.DataFrame(Person)
duplicate_emails(df3)