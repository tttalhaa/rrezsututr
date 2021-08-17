from pyrogram import Client, filters, emoji
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
SUDO_USERS = os.getenv("SUDO_USERS")


TG = Client(
	"LuciTag Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

MENTION = "[{}](tg://user?id={})"
MESSAGE = "👋🏻Merhaba {}, Hoşgeldin!"

DUR = False
SORGU = None
WSORGU = None
WDUR = False

PM = []
GR = []

def bstart():
	BUTTON=[[InlineKeyboardButton(text="Lucifer", url="https://t.me/Lucifermiyiz")]]
	BUTTON+=[[InlineKeyboardButton(text="➕ BENİ GRUBA EKLE ➕", url=f"https://t.me/LuciTagBot?startgroup=true")]]
	return InlineKeyboardMarkup(BUTTON)

@TG.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client, message):
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	await message.reply_text(f"👋🏻Merhaba {message.from_user.mention}\n\nBen [Lucifer](https://t.me/Lucifermiyiz) Tarafından codlanan bir üye etiketleme botuyum.\n\nYardım için /help",
		disable_web_page_preview=True,
		reply_markup=bstart()
		)
@TG.on_message(
	filters.command(["start", f"start@LuciTagBot"])
	& filters.group
	)
async def star(client, message):
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	await message.reply_text(f"👋🏻Merhaba {message.from_user.mention}\n\nBen [Lucifer](https://t.me/Lucifermiyiz) Tarafından codlanan bir üye etiketleme botuyum.\n\nYardım için /help",
		disable_web_page_preview=True,
		reply_markup=bstart()
		)
	
@TG.on_message(
	filters.command(["help", f"help@LuciTagBot"])
	& filters.group
)
async def help(client, message):
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	await message.reply_text(f"👋🏻Merhaba {message.from_user.mention}\n\nKomutlar:\n/atag mesaj\n/etag mesaj\n\n/cancel\nNOT: Sadece grupta çalışır ve bota yetki vermeden çalışmaz.")
	
@TG.on_message(
	filters.command("help")
	& filters.private
)
async def hel(client, message):
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	await message.reply_text(f"👋🏻Merhaba {message.from_user.mention}\n\nKomutlar:\n/atag mesaj\n/etag mesaj\n\n/cancel\nNOT: Sadece grupta çalışır ve bota yetki vermeden çalışmaz.")

@TG.on_message(filters.command("reklam") & (filters.private | filters.group))
async def duyuru(b, m):
        text = " ".join(message.command[1:])
        for i in (PM, GR):
               await TG.send_message(chat_id=i, text=f"{text}")
               time.sleep(2)

@TG.on_message(
	filters.private
	& filters.command("stats")
	)
async def st(client: TG, message: Message):
	pm = len(PM)
	gr = len(GR)
	await message.reply_text(f"Chat: {gr/2}\nUser: {pm/2}")

	
@TG.on_message(
	filters.command(["atag", "etag","cancel"])
	& filters.private
)
async def priw(client, message):
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.tpye == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	await message.reply_text("Bu komut sadece grupta çalışır.")


@TG.on_message(
	filters.command("etag")
	& filters.group
	)
async def tag(client: TG, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Kullanıcı etiketleme başlatıldı.")
			time.sleep(1)
			SORGU = True
			async for member in TG.iter_chat_members(chat_id=chat.id, filter="etag", limit=500):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await TG.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass
		
@TG.on_message(
	filters.command("atag")
	& filters.group
	)
async def ta(client: TG, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Adminleri etiketleme başlatıldı.")
			time.sleep(1)
			SORGU = True
			async for member in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await TG.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass


		
@TG.on_message(
	filters.group
	& filters.command("cancel")
)
async def stop(client: TG, message: Message):
	global DUR
	chat = message.chat
	async for mem in TG.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("Aktif çalışan işlem yoktur.")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Etiketleme işlemi durduruldu.")	
		if message.from_user.id != mem.user.id:
			pass
		
@TG.on_message(filters.group & filters.new_chat_members)
def welcome(client, message):
	chat = message.chat.id
	for i in (PM, GR):
		if chat.id != i:
			if message.chat.type == "private":
				PM.append(chat.id)
			else:
				GR.append(chat.id)
		if chat.id == i:
			pass
	for i in message.new_chat_members:
		new_members = MENTION.format(i.first_name, i.id)
		text = MESSAGE.format(new_members)
		message.reply(text, disable_web_page_preview=True)
	
TG.run()
