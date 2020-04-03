import datetime
from classes.BotHandler import BotHandler

token = "1173528624:AAE_VmquAJvssAkON6TVtAW_dQS0kTjMWZs"

ekivoki_bot = BotHandler(token)  
commands = ('/help', '/start', '/new_game', '/invite_friends', '/new_team') 
path_to_help_file = './files/help.txt'


def main():  
    new_offset = None

    while True:
        ekivoki_bot.get_updates(new_offset)

        last_update = ekivoki_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() == '/help':
            help_file = open(path_to_help,'r')
            help_string = help_file.read()
            ekivoki_bot.send_message(last_chat_id, help_string)


        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()