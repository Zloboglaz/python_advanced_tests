def get_cost(weight: int):
    """  
	Стоимость доставки  
	""" 
    if weight <= 10:
        result = 'Стоимость доставки: 200 руб.'
    else:
        result = 'Стоимость доставки: 500 руб.'
    return result


def check_month(month: int):
    """  
	Название месяца по его номеру  
	""" 
    if month == 12 or (1 <= month <= 2):
        result = 'Зима'
    elif (3 <= month <= 5):
        result = 'Весна'
    elif (6 <= month <= 8):
        result = 'Лето'
    elif (9 <= month <= 11):
        result = 'Осень'
    else:
        result = 'Некорректный номер месяца'
    return result

def list_of_numbers(n: int) -> list:
    """  
	Список чисел
	""" 
    return list(range(1, n + 1))



if __name__ == '__main__':
    print(get_cost(1))
    print(check_month(10))
    print(list_of_numbers(-8))