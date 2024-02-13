import pandas as pd

#converting a 2d array into dataframe
def createDataframe(student_data) -> pd.DataFrame:
    columns = ['student_id', 'age']
    df = pd.DataFrame(student_data, columns=columns)
    return df

createDataframe(student_data = [[1, 15],[2, 11],[3, 11],[4, 20]])