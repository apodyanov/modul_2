def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    corect_domen = (".com", ".net", ".ru")
    if "@" not in recipient and sender or not (recipient.endswith(corect_domen) and sender.endswith(corect_domen)):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient,'.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient, '!')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient, '!')