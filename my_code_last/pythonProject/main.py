import pandas as pd

data = {
    "Name": ['Amy White', 'Jack Stewart', 'Richard Lauderdale', 'Sara Johnson'],
    "Age": [50, 53, 35, 43],
    "Working Experience (Yrs.)": [5, 8, 3, 10]
}

df = pd.DataFrame(data, index=[1, 2, 3, 4])
df