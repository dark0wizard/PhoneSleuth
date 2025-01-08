import json
import os
from fake_useragent import UserAgent


ua = UserAgent().random

# Telegram (visit https://my.telegram.org/)
TELEGRAM_API_ID = your Telegram API ID
TELEGRAM_API_HASH = "your Telegram API HASH"

# Whatsapp (https://rapidapi.com/airaudoeduardo/api/whatsapp-data1)
WHATSAPP_HEADERS = {
    'x-rapidapi-key': "your API KEY",
    'x-rapidapi-host': "whatsapp-data1.p.rapidapi.com"
}


def save_result(phone_number, data):
    results_path = f'results/{phone_number}'
    os.makedirs(results_path, exist_ok=True)

    with open(f'{results_path}/{phone_number}_phone_data.json', "w") as json_file:
        json.dump(data, json_file, indent=4)


def split_phone_number(phone_number):
    phone_number = phone_number.lstrip('+')

    country_codes = ['1', '7', '20', '30', '31', '32', '33', '34', '36', '39', '40', '41', '44', '46',
                     '49', '52', '54', '55', '56', '57', '58', '60', '61', '62', '63', '64', '65', '66',
                     '81', '82', '84', '86', '90', '91', '92', '93', '94', '95', '98', '212', '213',
                     '216', '218', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229',
                     '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241',
                     '242', '243', '244', '245', '246', '248', '249', '250', '251', '252', '253', '254',
                     '255', '256', '257', '258', '260', '261', '262', '263', '264', '265', '266', '267',
                     '268', '269', '290', '291', '297', '298', '299', '350', '351', '352', '353', '354',
                     '355', '356', '357', '358', '359', '370', '371', '372', '373', '374', '375', '376',
                     '377', '378', '380', '381', '382', '383', '385', '386', '387', '389', '420', '421',
                     '423', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '590',
                     '591', '592', '593', '594', '595', '596', '597', '598', '599', '670', '672', '673',
                     '674', '675', '676', '677', '678', '679', '680', '681', '682', '683', '685', '686',
                     '687', '688', '689', '690', '691', '692', '850', '852', '853', '855', '856', '880',
                     '886', '960', '961', '962', '963', '964', '965', '966', '967', '968', '970', '971',
                     '972', '973', '974', '975', '976', '977', '992', '993', '994', '995', '996', '998']

    for code in sorted(country_codes, key=len, reverse=True):
        if phone_number.startswith(code):
            return code, phone_number[len(code):]

    return None, phone_number
