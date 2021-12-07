import os, logging, asyncio

from telegraph import upload_file

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
xavierbot = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


#start
@xavierbot.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("مـرحبآ بكـ في بوت التاك 😊❤️.!\n استطيع عمل تالك ل 1500 عضو في المجموعات ... وعمل 300 في القنوات .\n قائمه الاوامر /help ",
                    buttons=(
                      [
                         Button.url('𝑫𝒆𝒗', 'https://t.me/W_Q_Z'), 
                         Button.url('قناة الدعم 💕🍂', 'https://t.me/K_p_s_6'), 
                      ], 
                      [
                        Button.url('ضفني الي مجموعتك 🙊💕', 'https://t.me/TAAG_X2BOT?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#help
@xavierbot.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**قائمه مساعده بوت التاك**\n\nالأمر: /all \n يمكنك استخدام هذا الأمر مع النص الذي تريد إخبار الآخرين به. \n مثال: `/all هيي ` \n يمكنك استخدام هذا الأمر كإجابة. أي رسالة سيقوم البوت بوضع علامة على المستخدمين للرسالة التي تم الرد عليه"
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('𝑫𝒆𝒗', 'https://t.me/W_Q_Z'), 
                         Button.url('قناة الدعم 💕🍂', 'https://t.me/K_p_s_6'), 
                      ], 
                      [
                        Button.url('ضفني الي مجموعتك 🙊💕', 'https://t.me/TAAG_X2BOT?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#Wah bhaiya full ignorebazzi

#bsdk credit de dena verna maa chod dege

#tag
@xavierbot.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("استخدم الامر في مجموعه او قناه 💕🍂")
  
  admins = []
  async for admin in xavierbot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("يمكن للادمن فقط استخدام بوت التاك 🤓💕")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("لا يمكنني ذكر الأعضاء في المنشور القديم !!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("أعطني شيئاً. مثال: `/all هيي`")
  else:
    return await event.respond("قم بالرد علي رساله او اعطني بعض الكلمات لتاك 🤓💕")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in xavierbot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("تم التوقف!")
        return
      if usrnum == 5:
        await xavierbot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id) 
    usrnum = 0
    usrtxt = ""
    async for usr in xavierbot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("تم التوقف")
        return
      if usrnum == 5:
        await xavierbot.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


# Cancle 

@xavierbot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_mentionall(event):
  if not event.chat_id in mentionall_chats:
    return await event.respond('__لا يوجد عمليه تاك الان 🤓💕.__')
  else:
    try:
      mentionall_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**__تم ايقاف التاك 🤓💕__**\n\n**__Powered By:__ @K_P_S_6**')




print("تم تنصيب بوت التاك بنجاح 💕🍂")
print("لو محتاج مساعده @K_P_S_6")
xavierbot.run_until_disconnected()
