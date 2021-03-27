def server_problem():
    import os
    import sys
    import time
    from tqdm import tqdm
    import requests
    from colorama import Fore
    import header
    hostname = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(hostname, timeout=timeout)
        for _ in tqdm(range(50), ncols=100):
            time.sleep(0.03)
            pass
        print("check completed")
        print(f"{Fore.BLUE}[+]u r connected to the internet.....but something else seems to b the problem")
        try:
            request = requests.get("https://github.com/happyeggchen/Distro_wallpapers")
            if request:
                print(f"{Fore.BLUE}[+]the website is also opening..{Fore.RED}try restarting ur device{Fore.RESET}")
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
                    print("Command not accepted")

            else:
                print(f"{Fore.RED}[-]the website is down ... try after some time {Fore.RESET}")
        except requests.HTTPError and requests.ConnectionError:
            print("the server is not responding")
            sys.exit(0)

    except (requests.ConnectionError, requests.Timeout) as exception:
        for _ in tqdm(range(50), ncols=100):
            time.sleep(0.03)
            pass
        print(exception)
        print("check completed")
        print("")
        print(f"{Fore.RED}[-]u r not connected to the internet{Fore.RESET}")


server_problem()
