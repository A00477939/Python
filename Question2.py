#I have downloaded a csv file from online
import pandas as pd

def countVowels(a):
    COUNT=0
    for char in a:
        if(char in 'aeiouAEIOU'):
            COUNT = COUNT+1
    return COUNT
    


data = pd.read_csv('/Users/hritikarora/Documents/Python/countries of the world.csv')

data = data.assign(Count=data['Country'].apply(countVowels))

print(data)
