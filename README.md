# [Pyretic](https://microsoftlabs.github.io/Zoom-AutoRecorder/)
Installer Wizard for GNU/Linux Based Systems. (Facts written below are about prototype of the given project, I will try to implement most of the features. Help and advices on this project are most welcome)

### Introduction
Pyretic is FLOSS project aimed at easing the installing of packages, softwares on GNU/Linux based systems. It also aims to streamline the flow of software installation and inform the users about software license, details and other useful infos as well modify app permission during installation.

### Features
1. Standard Installer Wizard
2. Compile files from source using community based scripts. Just enter Github/ Gitlab/ Source Code links and you are good to go.(If I get enough help!)
3. Install from .deb, .appImage, sharedLibrary files etc.
4. *Modify app permission while installing.*
5. Clean UI.(I only know tkinter ,but I think Kivy or PyQT4 may be a better choice)
  - I have ruled out PyQT5 due to its restrictive licensing scheme, else it was best suited for the project.
6. Apply Patches on projects based on community based scripts.
  - An example would be like OBS doesn't work on low end PCs, for which it requires a flag to be applied to allow software encoding. The script can detect software name with user consent and search for any patches available and check PC specs and apply if applicable. [Somewhat more like windows compatibility checker.]
7. Support all major package manager with room to add any new package manager in future if required.
8. Allow user to modify order of preference of package manager, including blocking any if he/she wanted.
9. Show License and Readme file and permissions in wizards.
10. Support for App Installation, Uninstallation and other features.
11. Show list of installed softares and packages with feature to modify them(permission etc)
12. Support creating Start Menu and Desktop Icons.
13. Keep history of patches and updates with an option to roll back.
14. Download from Binary available on Github/ Gitlab Release page with compatibility check(from ArchWiki etc).
15. CLI Support(in Future Updates)
16. Give user power to install softwares without switching logins.
17. GivClean UI.(I only know tkinter but i think Kivy, PyQT may be a better choice)Clean UI.(I only know tkinter but i think Kivy, PyQT may be a better choice)


### Download
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white"
     alt="Download from GitHub"
     height="60">](https://github.com/Microsoftlabs/Pyretic/releases)

### Notes
- This app is not meant any other OS like Windows etc, however community based PR are welcome!

### Build an executable
- Make sure you have fulfilled the following requirements:
     1. [Python v3](https://www.python.org/) is installed.

     2. Python libraries: datetime, os, errno, sys, tkinter, PIL, time, sqlite3, subprocess, math, platform, ttkthemes
          - (All libraries except PIL and ttkthemes are installed by default in Python).
          - PIL can be installed by using the given commands in Terminal/CMD.
               ```markdown
               pip install pillow ttkthemes
               OR
               pip3 install pillow ttkthemes
               ```
- You can build your executable by using pyinstaller, Nuitka, or any other [compiler](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_comparisons.html) that you like.
- Then install your favourite compiler using their documentation.
     - For pyinstaller, run ```pip3 install pyinstaller``` or ```pip install pyinstaller```
     - For Nuitka, run ```pip3 install nuitka``` or ```pip install nuitka```, and then you'll need a [C compiler](https://nuitka.net/doc/user-manual.html#requirements), which will be automatically downloaded on the first run, if absent.
- Open the Code directory in the File Explorer and open the Windows PowerShell or terminal at that location and run the given commands.
     - UNIX-based Systems (Linux, macOS, etc.)
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data:data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - Windows
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data;data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - [Not Recommended for Novice Users] Any operating system(s).Unstable; contains bugs
          ```markdown
          python3 -m nuitka --standalone --nofollow-imports --remove-output --no-pyi-file --include-package=PIL --include-module=ttkthemes --output-dir=app_build --enable-plugin=tk-inter --onefile --include-data-dir=data=data --windows-icon-from-ico=data/icon.ico main.py
          ```
- The build will be created in the dist directory if using pyinstaller and app_build/main.dist if Nuitka is used.
- Run
     - Nuitka on Windows or pyinstaller: Run main.exe or main
     - On Linux-based OS, Nuitka creates a shared-library file named 'main' which can be run by opening the terminal in main.dist and typing ```./main```
- Also, see [Workaround for Nuitka Build](#workaround-for-nuitka-builds) for fixing the errors in Nuitka builds.

### Workaround for Nuitka Builds
After building the binary, copy the 'ttkthemes' folder from the site-packages folder (in the lib directory) in your standard Python installation location to main.dist directory, to remove import errors.
- To run the binary, open a terminal in the <Project-location>/app_build/main.dist directory, then type and run main.exe or ./main, depending on your OS.

- Running may cause an error after the app window is closed. (Any suggestions/workarounds for this are welcome.)
     ```
     ............/Pyretic/app_build/main.dist/tkinter/__init__.py", line 4025, in __del__
     TypeError: catching classes that do not inherit from BaseException is not allowed
     )
     ```
- Novice users are warned against using the Nuitka build because of its comparatively more complex installation than pyinstaller, increased build size, and present bugs in compiling the script on it. (Nuitka builds are faster performance-wise, btw.)

### ⚠ Warning
- Since the app is in the early development phase, it might be possible that it may not work at all. Feel free to report any bugs if they exist.
     
### Alternatives
- To be very honest, I couldn't find any alternatives even semi-functional. Prime reason for this amy be since majority of Linux userbase are tech-nerds they don't have any problem in using terminal which seems easier to them than actually making one.
- However, If you get any get any alternatives feel free to raise a PR. 

### Thanks!
