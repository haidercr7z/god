#pylint:disable=E0001
import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
aa = 'ertuiowaszxcvnm'
ee = 'mnvcxzaswertuio'
bb = 'wertuioaszxcvnm'
aaa = 'x'
banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    # النوع 1: دمج النوعين 1 و 2 (حرف_رقم_حرف/رقم)
    if choice == "1":
        # مثال: a_1_b
        chars = random.choices(a, k=2)
        num_or_char = random.choice([random.choice(b), random.choice(a)])
        username = f"{chars[0]}_{num_or_char}_{chars[1]}"
        if username in banned[0]:
            chars = random.choices(a, k=2)
            num_or_char = random.choice([random.choice(b), random.choice(a)])
            username = f"{chars[0]}_{num_or_char}_{chars[1]}"
    
    # النوع 2: دمج النوعين 4 و 10 (أنماط مختلفة من الحروف والأرقام مع شرطة)
    elif choice == "2":
        # مثال: a_bc1 أو ab_c1
        patterns = [
            f"{random.choice(a)}_{random.choice(e)}{random.choice(e)}{random.choice(b)}",
            f"{random.choice(a)}{random.choice(e)}_{random.choice(e)}{random.choice(b)}",
            f"{random.choice(a)}{random.choice(e)}{random.choice(e)}_{random.choice(b)}"
        ]
        username = random.choice(patterns)
        if username in banned[0]:
            patterns = [
                f"{random.choice(a)}_{random.choice(e)}{random.choice(e)}{random.choice(b)}",
                f"{random.choice(a)}{random.choice(e)}_{random.choice(e)}{random.choice(b)}",
                f"{random.choice(a)}{random.choice(e)}{random.choice(e)}_{random.choice(b)}"
            ]
            username = random.choice(patterns)
    
    # النوع 3: دمج النوعين 3 و 11 (أنماط مختلطة من الحروف والأرقام)
    elif choice == "3":
        # مثال: a11aa أو aa11a
        pattern_type = random.randint(1, 2)
        if pattern_type == 1:
            # نمط: حرف + رقم + رقم + حرف + حرف
            username = f"{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(a)}{random.choice(a)}"
        else:
            # نمط: حرف + حرف + رقم + رقم + حرف
            username = f"{random.choice(a)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(a)}"
        
        if username in banned[0]:
            if pattern_type == 1:
                username = f"{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(a)}{random.choice(a)}"
            else:
                username = f"{random.choice(a)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(a)}"
    
    # النوع 4: دمج الأنواع 5، 14، 15، 16، 17، 18، 19، 20، 21، 22، 23 (أنماط متنوعة)
    elif choice == "4":
        patterns = [
            # النمط 5: حرف + حرف/رقم + حرف/رقم + حرف/رقم + حرف
            f"{random.choice(a)}{random.choice(e)}{random.choice(e)}{random.choice(e)}{random.choice(a)}",
            
            # النمط 14: حرف + حرف + حرف + رقم + حرف/رقم
            f"{random.choice(a)}{random.choice(a)}{random.choice(a)}{random.choice(b)}{random.choice(e)}",
            
            # النمط 15-23: أنماط مختلفة باستخدام مجموعات الحروف المحددة
            f"{random.choice(aa)}{random.choice(aa)}{random.choice(ee)}{random.choice(bb)}{random.choice(bb)}",
            f"{random.choice(aa)}{random.choice(ee)}{random.choice(bb)}{random.choice(bb)}{random.choice(bb)}",
            f"{random.choice(aa)}{random.choice(ee)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}",
            f"{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(ee)}{random.choice(aa)}",
            f"{random.choice(ee)}{random.choice(aa)}{random.choice(aa)}{random.choice(aa)}{random.choice(aaa)}",
            f"{random.choice(bb)}{random.choice(ee)}{random.choice(ee)}{random.choice(ee)}{random.choice(aa)}",
            f"{random.choice(aa)}{random.choice(ee)}{random.choice(bb)}{random.choice(bb)}{random.choice(bb)}",
            f"{random.choice(bb)}{random.choice(bb)}{random.choice(bb)}{random.choice(ee)}{random.choice(aa)}",
            f"{random.choice(bb)}{random.choice(bb)}{random.choice(ee)}{random.choice(ee)}{random.choice(ee)}"
        ]
        username = random.choice(patterns)
        if username in banned[0]:
            username = random.choice(patterns)
    
    # النوع 5: النوع 6 (حرف + حرف/رقم + bot)
    elif choice == "5":
        # مثال: abbot
        username = f"{random.choice(a)}{random.choice(e)}bot"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(e)}bot"
    
    # النوع 6: النوع 7 (حرف + حرف/رقم + حرف/رقم + bot)
    elif choice == "6":
        # مثال: ab1bot
        username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}bot"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}bot"
    
    # النوع 7: النوع 8 (حرف + حرف/رقم + حرف/رقم + حرف/رقم + حرف/رقم)
    elif choice == "7":
        # مثال: a1234
        username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}{random.choice(e)}{random.choice(e)}"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}{random.choice(e)}{random.choice(e)}"
    
    # النوع 8: النوع 9 (حرف + حرف + _ + حرف + حرف)
    elif choice == "8":
        # مثال: aa_bb
        username = f"{random.choice(a)}{random.choice(a)}_{random.choice(a)}{random.choice(a)}"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(a)}_{random.choice(a)}{random.choice(a)}"
    
    # النوع 9: النوع 12 (حرف + حرف + حرف + حرف + حرف)
    elif choice == "9":
        # مثال: aaaaa
        username = f"{random.choice(a)}{random.choice(a)}{random.choice(a)}{random.choice(a)}{random.choice(a)}"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(a)}{random.choice(a)}{random.choice(a)}{random.choice(a)}"
    
    # النوع 10: النوع 13 (حرف + حرف + _ + حرف + حرف)
    elif choice == "10":
        # مثال: ab_cc
        username = f"{random.choice(a)}{random.choice(a)}_{random.choice(a)}{random.choice(a)}"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(a)}_{random.choice(a)}{random.choice(a)}"
    
    # النوع 11: النوع 24 (حرف/رقم + حرف + رقم + رقم + رقم + رقم)
    elif choice == "11":
        # مثال: a19999
        username = f"{random.choice(e)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(b)}{random.choice(b)}"
        if username in banned[0]:
            username = f"{random.choice(e)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(b)}{random.choice(b)}"
    
    # النوع 12: النوع 25 (حرف/رقم + حرف + رقم + رقم + رقم)
    elif choice == "12":
        # مثال: a1999
        username = f"{random.choice(e)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(b)}"
        if username in banned[0]:
            username = f"{random.choice(e)}{random.choice(a)}{random.choice(b)}{random.choice(b)}{random.choice(b)}"
    
    # النوع 13: النوع 26 (حرف + حرف/رقم + حرف/رقم + bot)
    elif choice == "13":
        # مثال: a1bbot
        username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}bot"
        if username in banned[0]:
            username = f"{random.choice(a)}{random.choice(e)}{random.choice(e)}bot"
    
    # النوع 14: النوع 27 (كلمات شائعة مع أرقام)
    elif choice == "14":
        # مثال: vip739 أو id739
        d1 = random.choice(b)
        d2 = random.choice(b)
        d3 = random.choice(b)
        patterns = [
            f"vip{d2}{d2}{d3}",      # طول 6 مثال: vip739
            f"id{d1}{d2}{d3}",        # طول 5 مثال: id739
            f"bet{d1}{d2}{d2}",       # طول 6 مثال: bet739
            f"pro{d1}{d1}{d3}",       # طول 6 مثال: pro739
            f"x{d1}{d2}{d1}x",        # طول 7 مثال: x739x
            f"king{d1}{d2}",          # طول 6 مثال: king73
            f"q{d1}{d3}{d3}q",        # طول 6 مثال: q739q
            f"vip_{d1}{d2}{d3}",      # طول 7 مثال: vip_739
            f"hero{d3}{d3}",          # طول 7 مثال: hero97
            f"xx_{d2}{d3}",           # طول 7 مثال: xx_739
            f"top{d1}{d2}{d3}",       # طول 6 مثال: top739
            f"pro_{d1}{d2}",          # طول 6 مثال: pro_73
            f"bet{d3}{d2}{d3}"        # طول 6 مثال: bet937
        ]
        username = random.choice(patterns)
        if username in banned[0]:
            username = random.choice(patterns)
    
    # النوع 15: النوع 28 (vip + 4 أرقام عشوائية)
    elif choice == "15":
        # مثال: vip1234
        numbers = ''.join(random.choices(b, k=4))
        username = f"vip{numbers}"
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=4))
            username = f"vip{numbers}"
    
    # النوع 16: أسماء عربية شائعة + أرقام (النوع 29)
    elif choice == "16":
        # مثال: ali12
        arabic_names = ['ali', 'omar', 'ahmed', 'mohamed', 'mahmoud', 'khaled', 'hassan', 'hussain']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(arabic_names) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(arabic_names) + numbers
    
    # النوع 17: كلمات إنجليزية شائعة + أرقام (النوع 30)
    elif choice == "17":
        # مثال: star12
        english_words = ['star', 'moon', 'sun', 'sky', 'sea', 'king', 'queen', 'gold', 'love', 'angel']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(english_words) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(english_words) + numbers
    
    # النوع 18: أسماء حيوانات + أرقام (النوع 31)
    elif choice == "18":
        # مثال: lion12
        animals = ['lion', 'tiger', 'eagle', 'wolf', 'fox', 'bear', 'shark', 'snake', 'horse', 'cat']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(animals) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(animals) + numbers
    
    # النوع 19: أسماء بلدان + أرقام (النوع 32)
    elif choice == "19":
        # مثال: egypt12
        countries = ['egypt', 'ksa', 'uae', 'qatar', 'oman', 'iraq', 'jordan', 'lebanon', 'morocco', 'tunisia']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(countries) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(countries) + numbers
    
    # النوع 20: أسماء مشاهير + أرقام (النوع 33)
    elif choice == "20":
        # مثال: mess12
        celebrities = ['mess', 'ronaldo', 'elon', 'bill', 'mark', 'jack', 'obama', 'trump', 'putin', 'kylie']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(celebrities) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(celebrities) + numbers
    
    return username

@Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
        
@Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await Tepthon.send_file(event.chat_id, 'banned.txt')


@Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
# .صيد 777777 نوع  يوزر القناه بدون @


@Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 0
        await event.edit(f"حسناً سأفحص نوع `{choice}` من اليوزرات على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

        @Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"الصيد وصل لـ({trys}) من المحاولات")
                elif "off" in isclaim:
                    await event.edit("لايوجد صيد شغال !")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await Tepthon(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_file(event.chat_id, "https://t.me/v_yip/40", caption=f'''
⌯ Done caught ! 🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @h_d71 )  
    ''')
                    
                    await event.client.send_file("@h_d71", "https://t.me/v_yip/40", caption=f'''
⌯ Done caught ! 🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @h_d71 ) ''')
                    
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await Tepthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await Tepthon.send_message(event.chat.id, " اجاك متاح !")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "! انتهى الصيد")
        
@Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @Tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await Tepthon(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''
Haider CHECKER
User : @{username}        
Channel 
@h_d71
    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await Tepthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(8)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await Tepthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await Tepthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''
Haider CHECKER
User : @{username}        
Channel / @v_yip
@h_d71
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await Tepthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
