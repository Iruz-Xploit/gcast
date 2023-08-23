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
                          
  Creator : MK iruz || Youtube : MK iruz
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
mengetik("[+] Ini Adalah Program Ilegal\n[+] Semua Resiko Harap Ditanggung Pengguna..!!\n[+] This Is An Illegal Program\n[+] All Risks Borne by Users...!\n")
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
    
    client.send_message(entity=channel_entity, message='.gcast zayaaa disini')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast zayaa agy o,m,e,k')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Makasi sllu ad?????? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  zayaa sngee bgeettt ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Enak bnget omck ny aahtt? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  bsaah ssniii ahah ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  aaaaaahhhh ss,nii sa,yyy ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  LLLLLlllVvVVIEEE NNNNGGllEEEEEIWEEE DDIIPROOFIIL ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  BURUUUUAANNN KEEBBIIIYIYIIOOHHHH LIIIVEE OOMMEKKK SEBELUM KEHABISANNNN ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Sinii akuu bikinn munchrattt ?? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  N3ED CWO SNGGE ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast   GEDE BGT SUSUNYA DIBYO0QH')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  PPEENGENN COLLMEX DIBYO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  ᗩᎩᝪᝪᝪ0 ᔑᏆᑎᏆᏆᏆ ᏃᏆᐯᗩᗩ ᑌᗞᕼ ᗰᑌᏞᗩᗩᏆᏆᏆ ᑎᏀᗯᗴᗴᏦᏦᏦ ᑕᑭᎢᎢᎢᎢ ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  LLLLLlllVvVVIEEE NNNNGGllEEEEEIWEEE DDIIPROOFIIL')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  zee ridi promo vip konten prib permanen langsung pc aja ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  GEDE BGT SUSUNYA DIBYO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Yug Udh mulai omeegggggg sini mas ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  GEDE BGT SUSUNYA DIBYO0QH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  ngeuwweee berruthalllll dhibiyyiioohhh buurruuamnnnnnn ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Omck prott" di byoyuuhh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  ange? sni ch ak ad bacol buru ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  mekiipinkyy lg di 33wvwee debheeiiyooo0 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  FUULLL DESSAHHH FULLLL NGGEEWEEE DIBIIYIYIYIIIOOOOOOOOOOOHHHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  temenin cllmk pliss😖')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  takeeeeemmeeeeooouuuhttttttt smpee mmpus di PARADOX byouuuhhh ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  SANGEEEEII BANGETT NIH TEMEEEININN OMEEICKK DONGG DIIIEBIIIOOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  mekiipinkyy lg di 33wvwee debheeiiyooo0 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  R2WWI`WOI A.NJRIT, NGHEWENYA BWARABWAR BGT DIBHIOO ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  FULL OSMECCCKSS DESAHHH DIYY BIYYOOOUHHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  ridiiii beb piiciiesss ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  difOtO AKuu adaa yaNG NgWWEeE niHHH?? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Enak bnget omck ny aahtt? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  UUDYDDEHH BASSSAHHH BANGETT KK ITU SINII BURUUANNNN ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  SANGE VC YU ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Pgnnn beb,akuu re4ddy lagi yaaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Malem sygku?? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast  Ayo cepettt sinihhh sibocill lagii keenakann nihh?? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast zaya pgn omek')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast zayaaaa basah bgt')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast caroline o,m,meee,kk ddi,iiii bb,ii,i,oi,oo ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast Ayo cepettt sinihhh sibocill lagii keenakann nihh?? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast temenin cllmk pliss? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast NGEEEUUUWWWWEEEE BRUTALL BANGET YANG CEWE L.l.N.K D.l,B,YYOOOO? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast tmnin ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast DHA mulaiy dhebeyonuaaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast SABTU YANGGGG MAUUUU NGOOCOOIKK SSlNNNllk KEPRROOPILLLL ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast CINI WAHHHHH PINKHKNNN BANGETTTT DI BYIUOHHHHHHHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast Yang serius bisa test call ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast ?HI??VE? ??O?E? ??WME?K ??AA?? ?I?I?? ??UU?UW??? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast MweMWEK nya kEsodok B¦Á¦ÁLLLOOKKK PANJANG Anjaayyy
Check ¦Âhi¡è¡èH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast basaaaah bgtttt ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast vc s,ni ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast SABTU YANGGGG MAUUUU NGOOCOOIKK SSlNNNllk KEPRROOPILLLL ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast CINI WAHHHHH PINKHKNNN BANGETTTT DI BYIUOHHHHHHHH ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast Kamoe kebyiuuuu buruaaahn ada omegck? ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast SABTU YANGGGG MAUUUU NGOOCOOIKK SSlNNNllk KEPRROOPILLLL ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : iruz')
    sleep(70)
    client.send_message(entity=channel_entity, message='.gcast OOOOIMMEEEECCKK DDDDDlllEEBBEEOOOOI ')
    
    )
    
    
  except:
    print(f'{hijau} Gcast gagal.! {putih} gcast by : iruz')
    sleep(70)

sys.exit()
client.disconnect()
