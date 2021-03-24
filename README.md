# Distro_wallpapers-CLI-python
This is a python script or program to browse, download, configure and install the wallpapers via nitrogen from [Distro_wallpapers](https://github.com/happyeggchen/Distro_wallpapers).

# What it does
1. Interact with the user through the script by printing various options and letting the user choose an option like this :- 
```
Choose your option by entering the number to the terminal :-
(1) Download the whole repo
(2) Choose which folders to download (you'll be prompted after)
(3) Download only the raw tar files (so you can extract them to your desired location)
(4) Choose which raw tar files to download (you'll be prompted after)
(5) Quit
Enter your desired option : 
```
2. Download the files user wants to download, `git clone` if the user wants the full repo, `git pull` for the folders the user wants to download, `curl [the file the file user wants to download` or `wget [the file the user wants to download` to download the raw tar file for the distro they want
3. Extract the tar files to the user's desired location, print default dir(s) if the user is unsure :- 
```
Choose your option by entering the number to the terminal :-
(1) Extrate to /usr/share/backgrounds
(2) Extract to ~/.wallpaper
(3) Extract to custom location (you'll be prompted to enter the location)
```
4. 
