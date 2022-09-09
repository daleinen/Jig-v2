
from src import v0
from src import v1
from src import v2
from src import v3

def main():

    display_welcome()
    user_input = get_user_mode()

    if user_input == "-a":
        display_adv()
        mode_select()
    elif user_input == "--help":
        display_help()
    else:
        v3.main3()

def display_adv():
    print("\n----------MODE SELECTION----------")
    print("m0 = The orginal program from Stand up Maths with no badness scale.")
    print("m1 = Same as m0 but with badness scale and predictions.")
    print("m2 = Same as m1 only based on how easy the puzzle can be.")
    print("m3 = Same functionality as v1 just cleaned up some asetetics.(default)")
    print("You can choose 0,1,2, or 3\n")

def display_help():
    pass

def display_welcome():
    print("\n---Welcome to Jig v2.0!---\n")
    print("Type '-a' for advanced mode, '--help' for more info")
    print("Press RETURN to get started\n")

def get_user_mode():
    return input("#:")

def mode_select():
    user_input = get_user_mode()
    if user_input in ('0', 'v0'):
        v0.main0()
    elif user_input in ('1', 'v1'):
        v1.main1()
    elif user_input in ('2', 'v2'):
        v2.main2()
    elif user_input in ('3', 'v3'):
        v3.main3()
    else:
        v3.main3()

if __name__ == "__main__":
    main()
