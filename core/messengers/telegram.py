from core.settings import TELEGRAM_API_HASH, TELEGRAM_API_ID
from telethon.sync import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl import types
from telethon import functions
import os

# The original repository: https://github.com/bellingcat/telegram-phone-number-checker


def get_human_readable_user_status(status: types.TypeUserStatus):
    match status:
        case types.UserStatusOnline():
            return "Currently online"
        case types.UserStatusOffline():
            return status.was_online.strftime("%Y-%m-%d %H:%M:%S %Z")
        case types.UserStatusRecently():
            return "Last seen recently"
        case types.UserStatusLastWeek():
            return "Last seen last week"
        case types.UserStatusLastMonth():
            return "Last seen last month"
        case _:
            return "Unknown"


async def get_id(phone_number):
    """This function looks for telegram_id if the phone number uses telegram"""
    async with TelegramClient('core/messengers/telegram_session.session', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
        try:
            # Add the number to Telegram contacts
            contact = InputPhoneContact(client_id=0, phone=phone_number, first_name="", last_name="")
            contacts = await client(functions.contacts.ImportContactsRequest([contact]))
            telegram_id = contacts.to_dict()['users'][0]['id']  # Get the user id
            await client(functions.contacts.DeleteContactsRequest(id=[telegram_id]))  # Delete account from contacts
        except IndexError:  # If the user does not use telegram
            return False
        except Exception as e:
            print(e)
            return False
        return telegram_id


async def scrape_telegram(phone_number):
    try:
        telegram_id = await get_id(phone_number)
        result = {'Chat_link': f'https://t.me/{phone_number}'}
        async with TelegramClient('core/messengers/telegram_session.session', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
            user_info = await client.get_entity(telegram_id)

            # Download photos
            photos = await client.get_profile_photos(user_info)
            if len(photos) > 0:
                os.makedirs(f'results/{phone_number}', exist_ok=True)
                for i, photo in enumerate(photos):
                    file_name = f'results/{phone_number}/Telegram_photo_{i}.jpg'
                    await client.download_media(photo, file=file_name)

        result.update(
            {
                "id": user_info.id,
                "access_hash": user_info.access_hash,
                "deleted": user_info.deleted,
                "username": user_info.username,
                "usernames": user_info.usernames,
                "phone": 'hidden' if not user_info.phone else user_info.phone,
                "first_name": str(user_info.first_name),
                "last_name": user_info.last_name,
                "photos": len(photos),
                "min_photo": user_info.apply_min_photo,
                "fake": user_info.fake,
                "scam": user_info.scam,
                "support": user_info.support,
                "verified": user_info.verified,
                "premium": user_info.premium,
                "contact require premium": user_info.contact_require_premium,
                "mutual_contact": user_info.mutual_contact,
                "bot": user_info.bot if not user_info.bot else {
                    "bot_nochats": user_info.bot_nochats,
                    "bot_inline_geo": user_info.bot_inline_geo,
                    "bot_business": user_info.bot_business,
                    "bot_info_version": user_info.bot_info_version,
                    "bot_inline_placeholder": user_info.bot_inline_placeholder,
                    "bot_attach_menu": user_info.bot_attach_menu,
                    "bot_can_edit": user_info.bot_can_edit
                },
                "bot_chat_history": user_info.bot_chat_history,
                "restricted": user_info.restricted,
                "restriction_reason": user_info.restriction_reason,
                "was_online": get_human_readable_user_status(user_info.status),
                "stories_hidden": user_info.stories_hidden,
                "stories_unavailable": user_info.stories_unavailable,
                "stories_max_id": user_info.stories_max_id
            }
        )

        return result
    except:
        return False
