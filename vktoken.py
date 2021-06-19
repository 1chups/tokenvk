import vk_api
import requests
from vk_api.utils import get_random_id

menu = """
[1] Отправить сообщение       [5] Забанить аккаунт                   [9]   
[2] Изменить статус           [6] Удалить пользователя из друзей     [10]
[3] Изменить пароль           [7] Заблокировать пользователя         [11]
[4] Создать пост на стене     [8] Разблокировать пользователя        [12]
"""

print(banner)
tok = input("Введите токен: ")
token = vk_api.VkApi(token = tok) 
vk = token.get_api()

print(menu)

while True:
    sel = input(">> ")
    if sel == '1':
        idv = input("Введите ID: ")
        mess = input("Введите сообщение: ")
        vk.messages.send(user_id=idv, message=mess, random_id=get_random_id())
        print("Сообщение успешно отправлено!")

    if sel == '2':
        status = input("Введите статус: ")
        token.method("status.set", {"text": status})
        print("Статус успешно изменён!")

    if sel == '3':
        old_password = input("Введите старый пароль: ")
        new_password = input("Введите новый пароль: ")
        vk.account.changePassword(old_password=old_password, new_password=new_password)
        print("Пароль успешно изменён!")

    if sel == '4':
        post = input("Введите текст для поста: ")
        vk.wall.post(message=post)
        print("Успех!")

    if sel == '5':
        print("Страница заблокирована!")
        vk.wall.post(message='Красная сова никогда не спит\n vto.pe\n Синий кит')

    if sel == '6':
        userid = input("Введите ID: ")
        vk.friends.delete(user_id=userid)
        print("Пользователь успешно удалён из друзей!")

    if sel == '7':
        blockid = input("Введите ID: ")
        vk.account.ban(owner_id=blockid)
        print("Пользователь успешно заблокирован!")

    if sel == '8':
        unbanid = input("Введите ID: ")
        vk.account.unban(owner_id=unbanid)
        print("Пользователь успешно разблокирован!")