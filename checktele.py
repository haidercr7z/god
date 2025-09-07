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
    if choice == "1":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
        # مثال: q_1_a
    if choice == "2":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
        # مثال: a_b_3
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], c[0] ,d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
        # مثال: a111a1
    if choice == "4":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+'_'+d+c+d
        f2 = c+d+c+'_'+d
        f3 = c+d+'_'+d+c
        f4 = c+'_'+d+d+c
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+'_'+d+c+d
            f2 = c+d+c+'_'+d
            f3 = c+d+'_'+d+c
            f4 = c+'_'+d+d+c
            f = f1,f2,f3,f4
            f = random.choice(f)
            username = f
        else:
            pass
        # مثال: a_1a1
    if choice == "5":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], s[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], s[0], s[0], d[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: a111b
    if choice == "6":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
        # مثال: a1bot
    if choice == "7":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
        # مثال: a12bot
    if choice == "8":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: a1333
    if choice == "9":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], '_' , d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], '_' , d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        # مثال: a_bb
    else:
            pass
    if choice == "10":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], c[0] , '_' , d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0] , '_' , d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
        # مثال: aa_b
    if choice == "11":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], c[0] , c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(a)
            f = [c[0], c[0], d[0], c[0], d[0] ,d[0]]
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], c[0] , c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
             pass
        # مثال: aa11aa
    if choice == "12":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
        # مثال: abaaa
    if choice == "13":
        c = d = random.choices(a)
        d = random.choices(a)
        f =  [c[0], d[0],  '_' , c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0],  '_' , c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
        # مثال: ab_aa
    if choice == "14":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], c[0], c[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], c[0], c[0], d[0], s[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: aaa1b
    if choice == "15":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [c[0], c[0], d[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [c[0], c[0], d[0], s[0],極端
            username = ''.join(f)
        else:
            pass
        # مثال: eeww
    if choice == "16":
        c = random.choices(aa)
        d = random.choices(ee)
       極端 s = random.choices(bb)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [極端c[0], d[0], s[0], s極端[0], s[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: ewww
    if choice == "17":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(aaa)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(aaa)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: edxxx
    if choice == "18":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(aaa)
        f極端 = [s[0], s[0], s[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(aaa)
            f = [s[0], s[0], s[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: xxxde
    if choice == "19":
        c = random.choices(aa)
        d = random.choices(aaa)
        s = random.choices(ee)
        f = [s[0], c[0], c[0], c[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(aaa)
            s = random.choices(ee)
            f = [s[極端0], c[0], c[0], c[0], d[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: waaax
    if choice == "20":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [s[0], d[0], d[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [s[0], d[0], d[0], d[0], c[0]]    
            username極端 = ''.join(f)
        else:
            pass
        # مثال: wddde
    if choice == "21":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: edwww
    if choice == "22":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [s[0], s[0], s[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [s[0], s[0], s[極端0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: wwwde
    if choice == "23":
        c = random.choices(aa)
        d = random.choices(bb)
        s = random.choices(ee)
        f = [s[0], d[0], d[0], d[0],極端 c[0]]    
        username = ''.join(f)
       極端 if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(bb)
            s = random.choices(ee)
            f = [s[0], d[0], d[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: wddde
    if choice == "24":
        c = random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: 1a1111
    if choice == "25":
        c =極端 random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0]]    
            username = ''.join(f)
        else:
            pass
        # مثال: 1a111
    if choice == "26":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
        # مثال: a12bot
    if choice == "27":
        d1 = random.choice(b)
        d2 = random.choice(b)
        d3 = random.choice(b)
        l1 = random.choice(a)
        l2 = random.choice(a)
        same = random.choice(a)  
        
        # الأنماط القديمة (المحتفظ بيها)
        f2 = 'id' + d1 + d3 + d3
        f3 = 'ton' + d2 + d2 + d2
        f5 = 'x' + d1 + 'x' + d1 + 'x'
        f7 = 'q' + d1 + 'q' + d1 + 'q'
        f8 = 'vip' + d1 +極端 d1 + d1
        
        f9 = same + same + d1 + same + d2
        f10 = 'xxx' + d1 + d2
        
        while l2 == l1:
            l2 = random.choice(a)
        f12 = l1 + l2 + d3 + d3 + d3
        
        # f13: سداسي من حرفين فقط
        l3 = random.choice(a)
        l4 = random.choice(a)
        while l4 == l3:
            l4 = random.choice(a)
        f13 = (l3 + l4) * 3
        
        # f14: سداسي (حرف + رقم) بأنماط مختلفة
        l5 = random.choice(a)
        d4 = random.choice(b)
        patterns_f14 = [
            l5 + l5 + d4 + l5 + l5 + d4,   # ss2ss2
            l5 + d4 + l5 + l5 + d4 + l5,   # s2ss2s
            d4 +極端 l5 + l5 + d4 + l5 + l5    # 2ss2ss
        ]
        f14 = random.choice(patterns_f14)
        
        # f15: سباعي (حرف + رقم) بأنماط مشابهة
        l6 = random.choice(a)
        d5 = random.choice(b)
        patterns_f15 = [
            l6 + l6 + d5 + l極端6 + l6 + d5 + l6,  # ss2ss2s
            l6 + d5 + l6 + l6 + d5 + l6 + l6,  # s2ss2ss
            d5 + l6 + l6 + d5 + l6 + l6 + d5   # 2ss2ss2
        ]
        f15 = random.choice(patterns極端_f15)
        
        # ✅ الأنماط الجديدة بدل f1,f4,f6,f11
        l7 = random.choice(a)
        l8 = random.choice(a)
        c = random.choice(a)  
        new_patterns = [
            l7 + l7 + l8 + l8 + l8,       # xxyyy
            l8 + l8 + l8 + l7 + l7,       # yyyxx
            l7 + l8 + l8 + l7 + l7,       # xyyxx
            l7 + l8 + l7 + l8 + l7,       # yxyxx
            l7 + c + l8 + l8 + l8,        # xcyyy
            l8 + l8 + l7 + c +極端 l8,        # yyxcy
            c + l極端7 + l8 + l8 + l8,        # cxyyy
            "cx" + d1*3,                  # cx111
            d1*3 + "cx"                   # 111cx
        ]
        f_new = random.choice(new_patterns)
        
        # القائمة الكاملة
        f = [f2, f3, f5, f7, f8, f9, f10, f12, f13, f14, f15, f_new]
        username = random.choice(f)
        if username in banned[0]:
            d1 = random.choice(b)
            d2 = random.choice(b)
            d3 = random.choice(b)
            l1 = random.choice(a)
            l2 = random.choice(a)
            same = random.choice(a)
            
            f2 = 'id' + d1 + d3 + d3
            f3 = 'ton' + d2 + d2 + d2
            f5 = 'x' + d1 + 'x' + d1 + 'x'
            f7 = 'q' + d1 + 'q' + d1 + 'q'
            f8 = 'vip' + d1 + d1 + d1
            
            f9 = same + same + d1 + same + d2
            f10 = 'xxx' + d1 + d2
            
            while l2 == l1:
                l2 = random.choice(a)
            f12 = l1 + l2 + d3 + d極端3 + d3
            
            l3 = random.choice(a)
            l4 = random.choice(a)
            while l4 == l3:
                l4 = random.choice(a)
            f13 = (l3 + l4) * 3
            
            l5 = random.choice(a)
            d4 = random.choice(b)
            patterns_f14 = [
                l5 + l5 + d4 + l5 + l5 + d4,
                l5 + d4 + l5 + l5 + d4 + l5,
                d4 + l5 + l5 + d4 + l5 + l5
            ]
            f14 = random.choice(patterns_f14)
            
            l6 = random.choice(a)
            d5 = random.choice(b)
            patterns_f15 = [
                l6 + l6 + d5 + l6 + l6 + d5 + l6,
                l6 + d5 + l6 + l6 + d5 + l6 + l6,
                d5 + l6 + l6 + d5 + l6 + l6 +極端 d5
            ]
            f15 = random.choice(patterns_f15)
            
            l7 = random.choice(a)
            l8 = random.choice(a)
            c = random.choice(a)
            new_patterns = [
                l7 + l7 + l8 + l8 + l8,
                l8 + l8 + l8 + l7 + l7,
                l7 + l8 + l8 + l7 +極端 l7,
                l7 + l8 + l7 + l8 + l7,
                l7 + c + l8 + l8 + l8,
                l8 + l8 + l7 + c + l8,
                c + l7 + l8 + l8 + l8,
                "cx" + d1*3,
                d1*3 + "cx"
            ]
            f_new = random.choice(new_patterns)
            
            f = [f2, f3, f5, f7, f8, f9, f10, f12, f13, f14, f15, f_new]
            username = random.choice(f)
        # أمثلة: 
        # f_new: xxyyy, yyyxx, xyyxx, yxyxx, xcyyy, yyxcy, cxyyy, cx111, 111cx
    if choice == "28":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        k = random.choices(b)
        f = [c[0], d[0], s[0],k[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            k = random.choices(b)
            f = [c[0], d[0], s[0],k[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
        # مثال: vip1234
    # النوع 29 - تم استبداله بالقائمة الجديدة
    if choice == "29":
        arabic_names = [
            "Ali", "Hussain", "Haider", "Abbas", "Karrar", "Mahdi", "Mustafa",
            "Mohammed", "Ah極端med", "Jasim", "Qasim", "Murtadha", "Miqdad", "Sajad",
            "Mahmoud", "Yousef", "Ibrahim", "Ammar", "Karam", "Malik",
            "Faris", "Jaafar", "Hamza", "Mushtaq", "Nizar", "Jamal",
            "Thamer", "Qais", "Waleed", "Fadhel", "Manaf", "Moayad",
            "Anwar", "Riyadh", "Samer", "Hazem", "Tariq", "Wisam",
            "Kazem", "Falah", "Salam", "Basim", "Dhiaa", "Jaber",
            "Zahraa", "Fatima", "Mariam", "Batool", "Ruqaya", "Zainab",
            "Hawraa", "Sarah", "Mahdiya", "Noor", "Shahd", "Malak",
            "Kawthar", "Doaa", "Bashaer", "Isra", "Yasmin",
            "Farah", "Raghad", "Hanaa", "Huda", "Ibtisam", "Amira",
            "Halima", "Rahma", "Thikra", "Suad", "Najat", "Nahla"
        ]
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(arabic_names) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(arabic_names) + numbers
        # مثال: Ali12, Hussain34
    
    if choice == "30":
        # نوع: كلمات إنجليزية شائعة
        english_words = ['star', 'moon', 'sun', 'sky', 'sea', 'king', 'queen', 'gold', 'love', 'angel']
        numbers = ''.join(random.choices(b,極端 k=2))
        username = random.choice(english_words) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(english_words) + numbers
        # مثال: star12, moon34
    
    if choice == "31":
        # نوع: أسماء حيوانات
        animals = ['lion', 'tiger', 'eagle', 'wolf', 'fox', 'bear', 'shark', 'snake', 'horse', 'cat']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(animals) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(animals) + numbers
        # مثال: lion12, tiger34
    
    if choice == "32":
        # نوع: أسماء بلدان
        countries = ['egypt', 'ksa', 'uae', 'qatar', 'oman', 'iraq', 'jordan', 'lebanon', 'morocco', 'tunisia']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(countries) + numbers
        if username in banned[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(countries) + numbers
        # مثال: egypt12, ksa34
    
    if choice == "33":
        # نوع: أسماء مشاهير
        celebrities = ['mess', 'ronaldo', 'elon', 'bill', 'mark', 'jack', 'obama', 'trump', 'putin', 'kylie']
        numbers = ''.join(random.choices(b, k=2))
        username = random.choice(celebrities) + numbers
       極端 if username in banned極端[0]:
            numbers = ''.join(random.choices(b, k=2))
            username = random.choice(celebrities) + numbers
        # مثال: mess12, ronaldo34
    
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
    if ispay2[0] ==極端 "yes":
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
                    await event.edit(f"الصيد وصل لـ({極端trys}) من المحاولات")
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
                    
                    await event.client.send_file("@h_d71", "https極端://t.me/v_yip/40", caption=f'''
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
            ch =極端 str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg極端[0]}` من المحاولات !")

            @Tepthon.on極端(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
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
                await event.client.send_message(event.chat_id, f"極端مبند `{username}` ❌❌")
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
