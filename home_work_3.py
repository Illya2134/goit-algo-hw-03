
# Перше завдання
import datetime
from datetime import datetime

def get_days_from_today():
    date_input = input("Ведіть дату у форматі РРРР-ММ-ДД: ") 
    now_date = datetime.today()
    date_input_convert = datetime.strptime(date_input, "%Y-%m-%d")
    diff_date = (now_date - date_input_convert).days
    if diff_date > 0:
        print(f"З ціеї дати пройшло {diff_date} днів.")
    else:
        print(f"До цієї дати залишилось {diff_date} днів.") 
    
get_days_from_today()



# Друге завдання 
import random

def get_numbers_ticket(min, max, quantity):
    win_numbers = []
    
    if ((min < 0) or (max > 1001) or (max < min) or (min > quantity or quantity > max)):
        print("Одне із значень не дійсне")
        
    else:
        numbers_generate = list(range(min, max))
        win_numbers = random.sample(numbers_generate, quantity)
        sorted_win_numbers = sorted(win_numbers)
        print(sorted_win_numbers)
    return

get_numbers_ticket(1, 49, 6)
get_numbers_ticket(-1, 49, 6)
get_numbers_ticket(1, 1002, 6)
get_numbers_ticket(52, 49, 6)
get_numbers_ticket(1, 49, 61)


#Трете завдання 
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "8 097  888-12-21"
]

def normalize_phone(phone_number): 
    patt = r"[\+\d]"
    plus_and_numbers = re.findall(patt, phone_number)
    clear_numbers = "".join(plus_and_numbers)
    if len(clear_numbers) == 10:
        clear_numbers = "+38" + clear_numbers
    elif len(clear_numbers) == 11:
        clear_numbers = "+3" + clear_numbers
    elif len(clear_numbers) == 12:
        clear_numbers = "+" + clear_numbers
            
    return clear_numbers

for phone in raw_numbers:
    print(normalize_phone(phone))



#Четверте завдання 
    
import datetime

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.30"}
]

def get_upcoming_birthdays():
    congratulation_day = []
    for user in users:
        birthay_date = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d')
        now_date = (datetime.datetime.now()).date()
        birthay_date_this_year = datetime.datetime(now_date.year, birthay_date.month, birthay_date.day).date()
        if (birthay_date_this_year - now_date).days < 0:
            birthay_date_this_year = datetime.datetime(now_date.year + 1, birthay_date.month, birthay_date.day).date()
        elif (birthay_date_this_year - now_date).days < 7 :
            if birthay_date_this_year.weekday() == 5:
                birthay_date_this_year = birthay_date_this_year + datetime.timedelta(days = 2)
            elif birthay_date_this_year.weekday() == 6:
                birthay_date_this_year = birthay_date_this_year + datetime.timedelta(days = 1)
            list_congratulation_day = {'name':user['name'], 'congratulation_day': datetime.datetime.strftime(birthay_date_this_year, '%Y-%m-%d')}
            congratulation_day.append(list_congratulation_day)   
    return congratulation_day
    

print(get_upcoming_birthdays())
