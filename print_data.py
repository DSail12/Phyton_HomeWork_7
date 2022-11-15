def print_data(data):
    if len(data) > 0:
print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Заметка".center(40)))
print("-"*100)
from item in data:
print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(40))
else:
    print("Справочник пуст!")