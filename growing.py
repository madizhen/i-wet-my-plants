import sys
import string
import time
from time import sleep

sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print("Usage: [ python ] growing.py duration_in_minutes")
    print("Example: [ python ] growing.py 10")
    print("Use a value of 0 minutes for an insta-garden.")
    print("Press Ctrl-C to exit the garden.")
    sys.exit(1)

try:
    minutes = int(sa[1])
except ValueError:
    print("Invalid numeric value (%s) for minutes.") % sa[1]
    print("Plants will not grow this quickly, please calm down.")
    sys.exit(1)

if minutes < 0:
    print("Plants take time to grow.")
    sys.exit(1)

seconds = minutes * 60

try:
    if minutes == 10:
        print("       ^^^^^^^^^^^^")
        minutes -= 2
        sleep(60 * 2)
    if minutes == 8:
        print("""|
                 | 
            ^^^^^^^^^^^""")
        minutes -= 2
        sleep(60 * 2)
    if minutes == 6:
        print("""
                       _,
                /  __/ /
                | _/ _.'
                |/__/
            ^^^^^^""")
        minutes -= 2
        sleep(60 * 2)
    if minutes == 4:
        print("""
                |\   |
                \ |  | 
                 | \ /
                  \|/    _,
                   /  __/ /
                   | _/ _.'
                   |/__/
                ^^^^^^^
            """)
        minutes -= 2
        sleep(60 * 2)
    if minutes == 2:
        print("""
                    / / )
                 |  \/.-')
                 .'/\'..)
            |\   |/  | \_)
            \ |  |   \_/
            | \ /
             \|/    _,
             /  __/ /
             | _/ _.'
             |/__/
           ^^^^^
            """)
        minutes -= 2
        sleep(60 * 2)
    if minutes == 0:
        print("""
              
                             .-.
                       __   /   \   __
                      (  `'.\   /.'`  )
                       '-._.(;;;)._.-'
                       .-'  ,`"`,  '-.
                      (__.-'/   \'-.__)/)_
                            \   /\    / / )
                             '-'  |   \/.-')
                             ,    | .'/\'..)
                             |\   |/  | \_)
                             \ |  |   \_/
                              | \ /
                               \|/    _,
                                /  __/ /
                               | _/ _.'
                               |/__/
                                \
                        ^^^^^^^^^^^^^""")
        print("Spring has sprung! I'm so excited I'm gonna wet my plants!")
except KeyboardInterrupt:
    print("""  Your plants are on fire.
            ,.   (   .      
   ("     )  )'     ,'        
 .; )  ' (( (" )    ;(, 
 _"., ,._'_.,)_(..,( . )_ 

""")
    sys.exit(1)