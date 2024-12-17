def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    corect_domen = (".com", ".net", ".ru")
    if "@" not in recipient and sender or not (recipient.endswith(corect_domen) and sender.endswith(corect_domen)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient + '!') # при использовании '+' знак ! также приклеивается как и с f строкой
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient + '!')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')