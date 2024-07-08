import pandas as pd

data_dict = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

df = pd.DataFrame(data_dict)
# print(df)


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
        filter_wei = animals[animals['weight'] >= 100]
        sort_data = filter_wei.sort_values(by=['weight'], ascending=False)
        new_data = pd.DataFrame(sort_data['name'])
        return new_data


print(findHeavyAnimals(df))
