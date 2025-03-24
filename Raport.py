import yagmail
import os
def SendRaport(result):
    EMAIL_SENDER = "Twój mail"
    EMAIL_PASSWORD = "Hasło Gmail do aplikacji (inne niż do logowanie)"
    EMAIL_RECEIVER = "Twój mail"
    attachments = []

    for file in os.listdir('A:/DjangoServerTestScrpit/errors_screen'):
        attachments.append(f'A:/DjangoServerTestScrpit/errors_screen/{file}')

    if  len(result)>0:
        message = f"❌ Testy NIEUDANE \n Wystąpiły błędy w testach: {len(result)} niepowodzeń.\n\nLista nieudanych testów:\n\n"
        message += "\n".join(str(test) for test in result)
    else:
        message = "✅ Testy UDANE \n Wszystkie testy zakończyły się sukcesem!"

    yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)
    yag.send(to=EMAIL_RECEIVER, subject="Raport testów autoamtycznych MFiszki", contents=message, attachments=attachments)
    print("✅ E-mail wysłany!")