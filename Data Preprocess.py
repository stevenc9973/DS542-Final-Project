import pandas as pd

file_path = 'LD2011_2014.txt'
data = pd.read_csv(
    file_path,
    sep=';',
    decimal=',',
    parse_dates=[0]
)

data.columns = ['timestamp'] + [f'MT_{i}' for i in range(1, data.shape[1])]
data = data.set_index('timestamp')
data = data.infer_objects()
numeric_data = data.select_dtypes(include=['number'])
data[numeric_data.columns] = numeric_data.interpolate(method='time')
data.to_csv('cleaned_dataset.csv')

print(data.head())
