import pandas as pd
import os

def schoolCount(df: pd.DataFrame):
    # Write your code here
    new_df = df[df['subjects'].apply(lambda x: len(x.split(' ')) >= 3)]
    new_df['state_code'] = new_df.state_code.str.replace('[^a-zA-Z0-9]', '')
    print(new_df.groupby(['state_code']).count())
    return new_df



if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    df = pd.read_csv('input.csv')

    result = schoolCount(df)
    fptr.write(result.to_csv(index=False))

    fptr.close()