# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/ae5a7b751569bb8b5062e.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "✧✧ Mewtwo-3.0 IS UP AND RUNNING SUCCESSFULLY ✧✧ \n\n"
  LEGENDX += "➥ DATABASE : ALL DATABASES FUNCTIONING PROPERLY\n\n"
  LEGENDX += "Mewtwo OS : 3.0 [LATEST]\n\n"
  LEGENDX += f"➥ USER {legendx} ☺️\n\n"
  LEGENDX += "➥ FULLY UPDATED\n\n"
  LEGENDX += "➥ TELETHON : 1.19.5 [LATEST]\n\n"
  LEGENDX += "THANKS FOR ADDING ME HERE"
  BUTTON = [[Button.url("DEVELOPER", "https://t.me/Swami_2_0_0_5"), Button.url("MASTER", "https://t.me/swami_2_0_0_5")]],
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX22")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX22,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX22")))
async def callback_query_handler(event):
# inline by Swami_2_0_0_5
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/LEGENDXOP/LEGEND-BOT"), Button.url("REPO-ULTROID X", "https://github.com/ULTROID-OP/ULTROID-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flegendxop%2Flegend-bot&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-BOTP%2FLE"), Button.url("DEPLOY-ULTROID", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT&template=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)



@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF MEWTWO 3.0", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/pogonoob/LEGEND-X")]])
# SWAMI_2_0_0_5

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
