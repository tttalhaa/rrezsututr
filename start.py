from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
 filters.command("start")
 & filters.private
 )
async def start(client: Client, message: Message):
 await message.reply_text(f"Merhaba {message.from_user.mention}, ben [Lucifermiyiz](https://t.me/Lucifermiyiz) 'Bana yazmanız icin hazırlanan bir botum!\n\n/req mesaj",
  disable_web_page_preview=True,
  reply_markup=InlineKeyboardMarkup(
   [
    [
     InlineKeyboardButton(
      "Duyuru Kanalı", url="https://t.me/LuciOyunBot_Duyuru"
      )
    ],  
    [ 
     InlineKeyboardButton(
      "Sohbet Grubu", url="https://t.me/LuciOyunMerkezi"
      ) 
    ],  
    [ 
    InlineKeyboardButton(
      "Destek Grubu", url="https://t.me/LuciOyunBot_Destek"
      ) 
    ],  
    [ 
     InlineKeyboardButton(
      "➕ Luci Oyun Botu Bir Gruba Ekle ➕", url="https://t.me/LuciOyun_Bot?startgroup=true"
      )
    ],
    [
     InlineKeyboardButton(
      "➕ Luci Req Botu Bir Gruba Ekle ➕", url="https://t.me/LuciReqBot?startgroup=true"
      )
    ]
   ]
  )
 )
© 2021 GitHub, Inc.
