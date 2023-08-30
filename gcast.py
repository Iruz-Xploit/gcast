from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep, time
from colorama import Fore,Style, init as color_ama
color_ama(autoreset=True)
import json, re, sys, os, random

banner = Style.BRIGHT+Fore.YELLOW +  """

   ____               _   
  / ___| ___ __ _ ___| |_ 
 | |  _ / __/ _` / __| __|
 | |_| | (_| (_| \__ \ |_ 
  \____|\___\__,_|___/\__|
                          
  Support : Cocentz404 || Youtube : Cocentz404"""

putih = Style.BRIGHT+Fore.WHITE
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
reset = Fore.RESET
biru = Style.BRIGHT+Fore.BLUE


os.system('clear') 
print(banner)
print("\n")
print(f'{hijau}[+] Indonesia/English')
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik("This Is An Illegal Program\n[+] All Risks Borne by Users...!\n")
if not os.path.exists('session'):
    os.makedirs('session')
if len(sys.argv) < 2:
    print( Fore.RED + '\n\nUsage : python main.py +62' + Fore.RESET)
    sys.exit(1)
api_id = 29826983
api_hash = '8de0ed7bbdc2d04c1938226d6bb9af38'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input(Fore.WHITE + 'Enter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input(Fore.RESET + 'Your 2fa Password : ')
        me = client.start(phone_number, passw)
saia = client.get_me()
print('[*]Account:',saia.first_name)
print('[*]Phone:',saia.phone,'\n')
channel_username = '@gcstbosss'
channel_entity = client.get_entity('@gcstbosss')
print('Memulai Bot Gcast..!')


while True:
  try:
    
    client.send_message(entity=channel_entity, message='.gcast DESAHANNYA BIKIN ANGEEE DIBIIYOUUH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Rdyyy ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast akuuuu udahhhh ANGHEE bangtttt di byyuiiioooihh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast lagi pd mainin lubang pipis di bihyoo ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast CCHOLLKEEE BAAREEENGGG DDBHEWWWWYOOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast HALLO DDDlllBBBlllOOOO ADDAA LLlllVVVEEE NGGGIEEEWWWEE ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Pgnnn beb,akuu re4ddy lagi yaaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast HALLO DDDlllBBBlllOOOO ADDAA LLlllVVVEEE NGGGIEEEWWWEE ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast bukannya mandi malah ngweek dibiyoowwh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast dbyoughhtr adaaaa yg onmeekcg bngett buruaann ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast LIIAAATT tNGEEWEEEe SINIIIHH SAMAAAa AKUUu PINKKKk BANNGETTTt DIIBIIYIYIYIIIOOOOOOOOHHh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Liiippeeesoooo ooommekkkk diiibbiiooihh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Kerja sambil ngewhekk debeohku ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Laiippssooo bbaarrrbaarr ooommeeggkk diiibbbeeiiioohh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Vecees yu pc ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast 𝘉𝘰𝘤𝘪𝘭 𝘥𝘪 𝘦𝘸𝘦 𝘵𝘢𝘯𝘵𝘦 𝘯𝘺𝘢 𝘴𝘦𝘯𝘥𝘪𝘳𝘪
𝘍𝘶𝘭𝘭 𝘷𝘪𝘥𝘦𝘰 𝘤𝘦𝘬 𝘥𝘪 𝘣𝘪𝘰𝘰𝘰 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast sɪɴɪ ʟɪᴠᴇsʜᴏᴡᴡᴡ ᴅɪ ʙɪʏʏʏᴏᴏʜʜʜsᴋᴜʜʜ ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast ʟɪᴠᴇsʜᴏᴡᴡ ʙᴀʀʙᴀʀʀ ᴏᴜᴍᴇᴄᴋ ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast AADAAA MEMEEEKKKSS DBHHUUIIOOKKK ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast 1BATLEEE  OMEKCKK VS BATLEEE COLY DI BIUHHHHHHH1 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Call anu nya sesudah mandi ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Siniiiiiii ke biohhhhh 😠😠😠😠 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast BENING BANGAT CEWENYA DI BIIIIOOOIOIOOO LAGI NYEPONGGGGGGG TUH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast KAYA CEWE KOREAAA YANG LAGI DI ODOK ODOK DI BYIIIIOOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast 𝕆ℍℍℍ 𝕀ℕ𝕀 𝕐𝔸ℕ𝔾 𝕃𝔸𝔾𝕀 𝕍𝕀ℝ𝔸𝕃𝕃 𝔻𝕀𝔹𝕀𝕐𝕆𝕆𝕆𝕆𝕆 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast 1SOKK1NN TM0 CUANN DIBYIOUHHH1HH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Opnpcs ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Inpo cowo sange ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast AKKKHUUUU LAGHHIII OMMHHE3XGK DBHYEIIIOOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Cholmekin aku beo ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast zaaayaaa basah bgt ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast om,ekin zayaa sini ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast ahhh sayang ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast sinii aku open ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast sayangg ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast morningg babeee ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast o,mekin zayaa cini ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast langsung ajaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast piwwpiwww ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast temnin colmk pliss ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast BUKANYA KERJA MALAH NGHEWEEEKKK DBEIIYOOHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Owwmmekkkiinn aku deebeoh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast udahhh cekbcekk bgtt nih di bgiooo ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast corrrrtttt bareng nadiaaaaa di byyuioooooooh aku ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast PtrrriiOpppnnPciessspullbodi😍 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast temenin dong😔 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast LIVESHOW GABUTAN TARUHANBOLA THE GANK DIBYOWWHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast rate punyaku kak ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast AKKKHUUUU LAGHHIII OMMHHE3XGK DBHYEIIIOOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast Pgnnn beb,akuu re4ddy lagi yaaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast 𝙾𝚛𝚍𝚎𝚛 𝚅𝚒𝚌𝚒𝚎𝚜 𝚕𝚊𝚗𝚐𝚜𝚞𝚗𝚐 𝚊𝚓𝚊 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(150)
    client.send_message(entity=channel_entity, message='.gcast OOOOIMMEEEECCKK DDDDDlllEEBBEEOOOOI ')
    
  except:
    print(f'{hijau} Gcast gagal.! {putih} gcast by : iruz')
    sleep(150)

sys.exit()
client.disconnect()
