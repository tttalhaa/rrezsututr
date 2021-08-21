Müşteri . on_message (
    filtreler . özel
    &  filtreler . komut ( "kullanım" )
    )
zaman uyumsuz  def  kl ( istemci , mesaj ):
         mesaj bekliyoruz . answer_text ( f"""<b>
Merhba🖐🏻, { mesaj . from_user . söz } şimdi sana bu bot nasıl kullanılır onu anlatıcam...
\n /atag - Adminleri etiketler Ör\:Mesajınızı yazın ve gönderin NOT:(/atag@LuciTagBot böyle değil.) 
\n /all - Kullanıcıları etiketler Ör\:Mesajınızı yazın ve gönderin NOT:(/all@LuciTagBot böyle değil.) 
\n /cancel - Etiketleme işlemini durdurur Ör\:Mesajınızı yazın ve gönderin NOT:(/cancel@LuciTagBot böyle değil.) 
\n /kullanim - bot anlatım videosunu atar. 
</b>""" )
        zaman . uyku ( 1 )
         müşteri bekle . send_video ( chat_id = mesaj . sohbet . id , video = "https://telegra.ph/file/cb18ca71b8a030b4c6652.mp4
