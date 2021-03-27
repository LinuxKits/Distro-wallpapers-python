def WgetDistroTarLink(distro):
    return "Wget" + "https://github.com/happyeggchen/Distro_wallpapers/raw/master/raw/latest/" + distro + ".tar.gz"


def CurlDistroTarLink(distro):
    return "curl" + "https://github.com/happyeggchen/Distro_wallpapers/raw/master/raw/latest/" + distro + ".tar.gz"


def work():
    import requests
    import subprocess
    from colorama import Fore, Style, Back
    import header
    from tqdm import tqdm
    import time
    import sys
    import help

    request = requests.get("https://github.com/happyeggchen/Distro_wallpapers")
    header.header()

    def its_open():
        for i in tqdm(range(100), desc="loa", ncols=100, unit="kb"):
            time.sleep(0.05)

        print(f"{Fore.RESET}{Back.RESET}{Style.RESET_ALL}connected successfully...")
        print(f"""
        Choose your option by entering the number to the terminal :-
        (1) Download the whole repo
        (2) Choose which folders to download (you'll be prompted after)
        (3) Download only the raw tar files (so you can extract them to your desired location)
        (4) Choose which raw tar files to download (you'll be prompted after)
        (5) Quit
        """)
        command = input(">")
        if command == '1':
            try:
                subprocess.run("git clone https://github.com/happyeggchen/Distro_wallpapers.git", shell=True)
                print("Success:)")
            except:
                print("An error occurred :(")
                print()
                print(f"Try running {Fore.RED} sudo apt-get install git ")
        elif command == '2':
            print(f"""
            {Fore.RED}  
            1)Debian
            2)Fedora
            {Fore.GREEN}
            3)MX-Linux
            {Fore.BLUE}
            4)Pop_OS!
            5)Zorin-OS
            6)antiX
            7)aosp/10
            8)bluelake/2.3
            9)deepin/20
            10)elementary
            11)endeavour/2021.02.03
            {Fore.YELLOW}
            12)gnome/3.30
            13)lineageos
            {Fore.GREEN}
            14)manjaro_xfce/20.2.1
            15)mint/20.1
            {Fore.LIGHTBLUE_EX}
            16)plasma/5.14
            {Fore.RED}
            17)raspbian/buster
            18)solus/4.1
            19)ubuntu
            {Fore.RESET}
            """)
            number = input(">")
            if number == '1':
                subprocess.run(WgetDistroTarLink("Debian"))
            elif number == '2':
                subprocess.run(WgetDistroTarLink("Fedora"))
            elif number == '3':
                subprocess.run(WgetDistroTarLink("MX-Linux"))
            elif number == '4':
                subprocess.run(WgetDistroTarLink("Pop_OS"))
            elif number == '5':
                subprocess.run(WgetDistroTarLink("Zorin-OS"))
            elif number == '6':
                subprocess.run(WgetDistroTarLink("antiX"))
            elif number == '7':
                subprocess.run(WgetDistroTarLink("aosp"))
            elif number == '8':
                subprocess.run(WgetDistroTarLink("bluelake"))
            elif number == '9':
                subprocess.run(WgetDistroTarLink("deepin"))
            elif number == '10':
                subprocess.run(WgetDistroTarLink("elementary"))
            elif number == '11':
                subprocess.run(WgetDistroTarLink("endeavour"))
            elif number == '12':
                subprocess.run(WgetDistroTarLink("gnome"))
            elif number == '13':
                subprocess.run(WgetDistroTarLink("lineageos"))
            elif number == '14':
                subprocess.run(WgetDistroTarLink("manjaro_xfce"))
            elif number == '15':
                subprocess.run(WgetDistroTarLink("mint"))
            elif number == '16':
                subprocess.run(WgetDistroTarLink("plasma"))
            elif number == '17':
                subprocess.run(WgetDistroTarLink("raspbian"))
            elif number == '18':
                subprocess.run(WgetDistroTarLink("solus"))
            elif number == '19':
                subprocess.run(WgetDistroTarLink("ubuntu"))
        elif command == '3':
            pass

        elif command == '4':
            pass
        elif command == '5':
            sys.exit(0)
        else:
            print("command not accepted")

    if request:
        its_open()
    else:
        help.server_problem()
        exit(0)

    header.footer()
