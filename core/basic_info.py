import phonenumbers
from phonenumbers import carrier, geocoder


def checking_phone(phone_number):
    try:
        if len(phone_number) < 9 or len(phone_number) > 15:
            return False

        result = {}

        parsed_number = phonenumbers.parse(phone_number, None)
        country = phonenumbers.geocoder.description_for_number(parsed_number, "en")
        operator = phonenumbers.carrier.name_for_number(parsed_number, "en")
        result.update(
            {
                "Phone number": phone_number,
                "Country":  country,
                "Operator": operator
            }
        )
        return result

    except phonenumbers.phonenumberutil.NumberParseException:
        print('Phone number not exists')
        return False
