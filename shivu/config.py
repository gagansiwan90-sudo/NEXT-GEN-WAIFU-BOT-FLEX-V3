class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6584789596"
    sudo_users = ["5630057244", "2010819209", "5702598840", "6101457748", "6154972031", "1735664760", "7036005233", "6100011620", "7297953309", "6412447141", "7244871367", "5530116994", "6584789596", "949302414"]
    OWNER_ID = "8546535996"
    sudo_users = "8053803602"
    GROUP_ID = -1003942224732
    TOKEN = "8768582373:AAH2WcT3jCTBwn2B0nY4VJ2EsswW9-v9PxY"
    mongo_url = "mongodb+srv://Elevenyts:Elevenyts@cluster0.vuyc1u2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "AdamBot_support"
    UPDATE_CHAT = "waifugrabbbbotupdates"
    BOT_USERNAME = "waifuhub_officialBot"
    CHARA_CHANNEL_ID = "-1003985910295"
api_hash="0dfa074770803265e8c61ddda0ad6fb0"
api_id="34224204"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
