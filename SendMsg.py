# Для примера использования 2 методов
# def get_user_status(user_id):
#     status = session.method('status.get', {user_id: user_id})
#     print(status['text'])
#
#
# def set_user_status():
#     text = input()
#     vk.status.set(text=text)


import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from mtok import token, peer_id

session = vk_api.VkApi(token=token)
vk = session.get_api()


def send_msg():
    msg = input("Введи сообщение: ")
    vk.messages.send(peer_id=peer_id, message=msg, random_id=0)

while True:
	send_msg()