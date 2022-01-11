##################### Hard Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

today_tuple = (dt.datetime.now().year, dt.datetime.now().month)
data = pandas.read_csv('birthdays.csv')

birthday_dictionnary = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dictionnary:
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    birthday_personne = birthday_dictionnary[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_personne['name'])

    with smtplib.SMTP('smtp.gmail.com') as connexion:
        connexion.starttls()
        connexion.login(user='boriskamtou@gmail.com', password='')
        connexion.sendmail(msg=f'Subject: Happy Birthday\n\n {contents}', from_addr='boriskamtou@gmail.com',
                           to_addrs=birthday_personne['email'])
