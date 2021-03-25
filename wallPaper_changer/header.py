def header():
    from pyfiglet import Figlet
    from random import choice
    from colorama import Fore, Back, Style

    fonts = ['slant', "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D", "doh", "isometric1", "letters",
             "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]
    font = choice(fonts)
    f = Figlet(font=font)
    print(f.renderText("Distro Wall  Paper Changer"))
    print("distro wall paper changer")
    print(f"{Fore.GREEN}{Style.BRIGHT}{Back.BLACK} Made By mrHola21 ")


def footer():
    import sys
    from colorama import Fore
    print()
    print("Another Great Work Done by mrHola21 ")
    print()
    print(f"follow me on {Fore.GREEN} GitHub")
    sys.exit(0)

