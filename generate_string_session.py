from pyrogram import Client as c

api_id = input('\nAPI Kimliğinizi girin:')
api_hash = input('\nApi Hash girin:')
print('\nİstenirse telefon numarasını girin!!')

u = c(':memory:', api_id=api_id, api_hash=api_hash)

with u:
    string = u.export_session_string()
    print("\nBURADA OTURUMLARINIZ DİZİNİ OLUŞTURUN, KOPYALAYIN VE PAYLAŞMAYIN:")
    print(f'\n{string}')
© 2021 GitHub, Inc.
