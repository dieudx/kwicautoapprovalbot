from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21967179"))
    API_HASH = getenv("API_HASH", "37d5fbb9217cb56d6261e61305d92748")
    BOT_TOKEN = getenv("BOT_TOKEN", "6020397023:AAEpsRUI6Hd48qzrGQiLJvz-KmrY4vHV-Dk")
    FSUB = getenv("FSUB", "kerala_villas")
    CHID = int(getenv("CHID", "-1001836265597"))
    SUDO = list(map(int, getenv("SUDO", "5630387958").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kailastg:<kailastg>@cluster0j.eb3ewbt.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
