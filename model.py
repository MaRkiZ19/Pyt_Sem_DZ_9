import json

phone_book = {}
path = 'sem9\phone_book.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book=json.load(file, )
        return True
    except:
        return False

def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False



def checl_id():
    if phone_book:
        return max(list(map(int, phone_book))) +1
    return 1

def add_contact(new: {int: dict[str, str]}):
    contact = {checl_id(): new}
    phone_book.update(contact)

def search(word: str) -> dict[int:dict[str,str]]:
    result={}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result

def change(menu_smal, index):
    ch_cnt = phone_book.get(index)
    while True:
        select = menu_smal
        match select:
            case 1:
                ch_cnt['name'] = input('Введлите новое имя: ')
                print(f'\n Контакт успешно изменен')
            case 2:
                ch_cnt['phone'] = input('Введлите новый номер: ')
                print(f'\n Контакт успешно изменен')
            case 3:
                ch_cnt['coment'] = input('Введлите новвый комментарий: ')
                print(f'\n Контакт успешно изменен')
            case 4:
                break
    print(f'\n Спасибо, приходите еще')
    print('='*200 +'\n')
        