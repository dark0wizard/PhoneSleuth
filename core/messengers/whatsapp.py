from core.settings import WHATSAPP_HEADERS
import http.client
import json


def whatsapp_profile(phone_number):
    '''Enter a phone number without +'''
    try:
        conn = http.client.HTTPSConnection("whatsapp-data1.p.rapidapi.com")
        conn.request("GET", f"/number/{phone_number}", headers=WHATSAPP_HEADERS)
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data.decode('utf-8'))
        result["Chat_link"] = f"https://wa.me/{phone_number}"
        return result
    except Exception as e:
        print(e)
