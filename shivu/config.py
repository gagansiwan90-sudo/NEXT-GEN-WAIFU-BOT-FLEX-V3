class Config(object):
    LOGGER = True

    OWNER_ID = 8546535996
    SUDO_USERS = [8053803602]

    GROUP_ID = -1003942224732
    TOKEN = "8768582373:AAHHznGAcIvtoKkYE3CJxhu6nHKRh3Kz5JQ"

    API_ID = 34224204
    API_HASH = "0dfa074770803265e8c61ddda0ad6fb0"

    MONGO_URL = "mongodb+srv://Elevenyts:Elevenyts@cluster0.vuyc1u2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    PHOTO_URL = [
        "https://telegra.ph/file/b925c3985f0f325e62e17.jpg",
        "https://telegra.ph/file/4211fb191383d895dab9d.jpg"
    ]

    SUPPORT_CHAT = "AdamBot_support"
    UPDATE_CHAT = "waifugrabbbbotupdates"
    BOT_USERNAME = "waifuhub_officialBot"
    CHARA_CHANNEL_ID = -1003985910295


class Development(Config):
    LOGGER = True


class Production(Config):
    LOGGER = True
