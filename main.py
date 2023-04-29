import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = "TOKEN"
GROUP_ID = GROUP_ID


def main():
    vk_session = vk_api.VkApi(token=TOKEN)

    longpollVK = VkBotLongPoll(vk_session, GROUP_ID)
    for event in longpollVK.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            ID_USER = event.obj.message["from_id"]
            vk = vk_session.get_api()
            USERNM = vk.users.get(user_ids=str(ID_USER), fields="city")[0]
            msg = f"Привет, {USERNM['first_name']}!"
            if USERNM["city"]:
                msg += f"\nКак поживает {USERNM['city']['title']}?"
            vk.messages.send(user_id=ID_USER, message=msg,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == "__main__":
    main()
