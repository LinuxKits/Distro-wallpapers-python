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
            13)lineageos/17.1
            14)lineageos17.1 2021-3-6
            {Fore.GREEN}
            15)manjaro_xfce/20.2.1
            16)mint/20.1
            {Fore.LIGHTBLUE_EX}
            17)plasma/5.14
            {Fore.RED}
            18)raspbian/buster
            19)solus/4.1
            20)ubuntu
            {Fore.RESET}
            """)
            number = input(">")
            if number == '1':
                pass
            if number == '2':
                pass
            if number == '3':
                pass
            if number == '4':
                pass
            if number == '5':
                pass
            if number == '6':
                pass
            if number == '7':
                pass
            if number == '8':
                pass
            if number == '9':
                pass
            if number == '10':
                pass
            if number == '11':
                pass
            if number == '12':
                pass
            if number == '13':
                pass
            if number == '14':
                pass
            if number == '15':
                pass
            if number == '15':
                pass
            if number == '15':
                pass
            if number == '15':
                pass
            if number == '15':
                pass
            if number == '15':
                pass

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


    header.footer()
