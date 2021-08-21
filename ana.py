@Client.on_message(
    filters.private
    & filters.command("kullanim")
    )
async def kl(client, message):
       await message.reply_text(f"""<b>
Merhba🖐🏻, {message.from_user.mention} şimdi sana bu bot nasıl kullanılır onu anlatıcam...
\n /atag - Adminleri etiketler Ör\:Mesajınızı yazın ve gönderin NOT:(/atag@LuciTagBot böyle değil.) 
\n /all - Kullanıcıları etiketler Ör\:Mesajınızı yazın ve gönderin NOT:(/all@LuciTagBot böyle değil.) 
\n /cancel - Etiketleme işlemini durdurur Ör\:Mesajınızı yazın ve gönderin NOT:(/cancel@LuciTagBot böyle değil.) 
\n /kullanim - Botu nasıl kullanmanız gerektiği hakkında bilgi videosunu atar.
</b>""" )
        time.sleep(1)
        await client.send_video(chat_id=message.chat.id, video= "https://telegra.ph/file/cb18ca71b8a030b4c6652.mp4", caption="**@LuciTagBot'u nasıl kullanmanız gerektiği hakkında bilgi videosu...**")
