from core.main_core import phonesearch
import asyncio
import argparse


async def process_args(args):
    print('Starting a search...')
    result = await phonesearch(phone_number=args.phone)
    if result:
        print('Check a folder "results" to find the info')
    else:
        print('This phone number is not correct')


def main():
    print(r"""| ___ \ |                    /  ___| |          | | | |    
| |_/ / |__   ___  _ __   ___\ `--.| | ___ _   _| |_| |__  
|  __/| '_ \ / _ \| '_ \ / _ \`--. \ |/ _ \ | | | __| '_ \ 
| |   | | | | (_) | | | |  __/\__/ / |  __/ |_| | |_| | | |
\_|   |_| |_|\___/|_| |_|\___\____/|_|\___|\__,_|\__|_| |_|
                                                           """)
    parser = argparse.ArgumentParser(description="This script searches for information by phone number. "
                                                 "To use all its features, open the settings.py file and "
                                                 "enter the API data you need")

    parser.add_argument('phone', help="Phone number to search")
    args = parser.parse_args()
    asyncio.run(process_args(args))


if __name__ == "__main__":
    main()

