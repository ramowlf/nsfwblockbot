import os
from telethon import TelegramClient, events, types
from telethon.tl.types import Message
import requests
import traceback

ramazan_ozturk = "27833866"
ramazan_abi = "3648a12e9a8df3f448d4aeaac2ab91ab"
yenir_omega = "Bot token gir"

sikim_dimdik_ramowlf = "1408982914"
yarram_kalkti_ramowlf = "Bg6HBgRzD4DYszy7bGRerhGcfvnb4eGe"

ramowlf = TelegramClient("ramazan_öztürk", ramazan_ozturk, ramazan_abi).start(bot_token=yenir_omega)

@ramowlf.on(events.NewMessage(pattern="/start"))
async def sikkirigi(ramazan):
    await ramazan.reply("nsfw içerikli fotoğrafları silerim hocam altyapı sahibi @ramowlf")
    
@ramowlf.on(events.NewMessage)
async def yarrak(ramazan):  
    try:
        if ramazan.photo or ramazan.video or ramazan.gif:
            ramazann = await ramazan.download_media(file="amcık")

            try:
                with open(ramazann, 'rb') as ramo:
                    response = requests.post(
                        url="https://api.sightengine.com/1.0/check.json",
                        files={'media': ramo},
                        data={
                            'models': 'nudity',
                            'api_user': sikim_dimdik_ramowlf,
                            'api_secret': yarram_kalkti_ramowlf
                        }
                    )

                if response.status_code == 200:
                    calma_oc = response.json()
                    nudity = calma_oc.get("nudity", {}).get("raw", 0)

                    if nudity > 0.3:
                        await ramazan.delete()
                        print("NSFW içerikli medya silindi.")
                else:
                    print("api yarra yemiş")
            finally:
                if os.path.exists(ramazann):
                    os.remove(ramazann)

    except Exception:
        traceback.print_exc()

@ramowlf.on(events.MessageEdited)
async def azginimyarrak(ramazan):
    message = ramazan.message
    if message.photo or message.video or message.gif or message.sticker:
        try:
            await message.delete()
        except Exception:
            pass
            
ramowlf.run_until_disconnected()