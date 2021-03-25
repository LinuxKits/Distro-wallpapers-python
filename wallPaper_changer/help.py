def server_problem():
    import os
    import time
    from tqdm import tqdm
    import socket
    import requests
    from colorama import Fore
    import header
    hostname = socket.gethostbyname(socket.gethostname())
    print(hostname)
    if hostname == '127.0.0.1':
        for _ in tqdm(range(50), ncols=100):
            pass
        print("check completed")
        print("")
        print(f"{Fore.RED}[-]u r not connected to the internet{Fore.RESET}")
    else:
        for _ in tqdm(range(50), ncols=100):
            time.sleep(0.03)
            pass
        print("check completed")
        print("u r connected to the internet.....but something else seems to b the problem")
        try:
            request = requests.get("https://github.com/happyeggchen/Distro_wallpapers")
            if request:
                print("[+]the website is also opening..try restarting ur device")
                print("do u want to restart ur device RIGHT NOW ?? ")
                print("""
                    (1) Restart RIGHT NOW !!
                    (2) DON'T restart !!   
                    """)
                restart = input(">")
                if restart == "1":
                    os.system("shutdown /r /t 1")
                elif restart == "2":
                    header.footer()
                else:
                    print("")

            else:
                print(f"{Fore.RED}[-]the website is down ... try after some time {Fore.RESET}")
        except:
            print("the server is not responding")


server_problem()
