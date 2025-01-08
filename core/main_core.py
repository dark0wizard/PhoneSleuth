from core.messengers.whatsapp import whatsapp_profile
from core.gooogle import google_dorks, simple_google
from core.basic_info import checking_phone
from core.messengers.telegram import scrape_telegram
from core.social.odnoklassniki import check_OK
from core.social.insta_and_amazon import amazon_insta
from core.settings import save_result


async def phonesearch(phone_number):
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number

    # Check general information
    gen_info = checking_phone(phone_number)

    if not gen_info:
        return False

    # Initial data
    data = {"General information": gen_info}

    try:
        telegram_data = await scrape_telegram(phone_number=phone_number)
    except Exception as e:
        telegram_data = f"Error: {e}"

    try:
        whatsapp_data = whatsapp_profile(phone_number[1:])
    except Exception as e:
        whatsapp_data = f"Error: {e}"

    try:
        odnoklassniki_data = check_OK(phone_number)
    except Exception as e:
        odnoklassniki_data = f"Error: {e}"

    try:
        insta_data = await amazon_insta(phone_number)
    except Exception as e:
        insta_data = {"instagram": f"Error: {e}", "amazon": f"Error: {e}"}

    try:
        google_search = simple_google(phone_number)
    except Exception as e:
        google_search = f"Error: {e}"

    try:
        dorks = google_dorks(phone_number)
    except Exception as e:
        dorks = f"Error: {e}"

    if whatsapp_data:
        data["Whatsapp"] = whatsapp_data
    if telegram_data:
        data["Telegram"] = telegram_data
    if odnoklassniki_data:
        data["Odnoklassniki"] = odnoklassniki_data
    if insta_data:
        data["Instagram"] = insta_data.get("instagram")
        data["Amazon"] = insta_data.get("amazon")
    if google_search:
        data["Google search"] = google_search
    if dorks:
        data["Google dorks"] = dorks

    save_result(phone_number=phone_number, data=data)
    return data

