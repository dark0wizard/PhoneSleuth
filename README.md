# PhoneSleuth
PhoneSleuth is a tool for gathering information about phone numbers from various platforms, such as WhatsApp, Telegram, and more. This tool is designed for OSINT professionals and investigators who need to collect open-source intelligence in a structured and automated way.

## Prerequisites
- Python 3.8 or higher
- A Telegram account with API credentials 
- A RapidAPI account for WhatsApp integration
- pip (Python package manager) installed
## Detailed Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dark0wizard/PhoneSleuth
   cd PhoneSleuth

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Configure the settings file: Open **settings.py** and fill in the required API keys and credentials:
   ```bash
   # Telegram (visit https://my.telegram.org/)
   TELEGRAM_API_ID = "your Telegram API ID"
   TELEGRAM_API_HASH = "your Telegram API HASH"

   # Whatsapp (https://rapidapi.com/airaudoeduardo/api/whatsapp-data1)
   WHATSAPP_HEADERS = {
       'x-rapidapi-key': "your API KEY",
       'x-rapidapi-host': "whatsapp-data1.p.rapidapi.com"
   }
4. Run the script:
  ```bash
  python main.py -h
  ```

5. First-time use with Telegram: When prompted, enter your Telegram phone number and verification code to create a session file. This file will be used for subsequent requests.

## Repositories used in this project
```bash
https://github.com/bellingcat/telegram-phone-number-checker
https://github.com/shllwrld/ok_checker
https://github.com/megadose/ignorant
```
