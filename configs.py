from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21967179"))
    API_HASH = getenv("API_HASH", "37d5fbb9217cb56d6261e61305d92748")
    BOT_TOKEN = getenv("BOT_TOKEN", "5614082421:AAGJBiLTtvFBuAPKTJre4iqlr31mtdWy-VY")
    FSUB = getenv("FSUB", "keralavillas")
    CHID = int(getenv("CHID", "-1001764340281"))
    SUDO = list(map(int, getenv("SUDO", "5630387958 5963778687").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://darshana:darshana@cluster0.elq2jqs.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
