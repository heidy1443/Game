
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts_list=figlet.getFonts()

if len(sys.argv)==1 :
    word=input("input:")
    print(figlet.renderText(word))

elif len(sys.argv)==3 and sys.argv[1] in ["-f","-font"] and sys.argv[2] in fonts_list:
    figlet.setFont(font=sys.argv[2])
    word=input("input:")
    print(figlet.renderText(word))

else:
    sys.exit("Invalid usage")








