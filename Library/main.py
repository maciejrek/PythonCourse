import menu
import menu_module

while 1:
    inp = input("Choose version :\n 1: Text version\n 2: GUI version\n")
    if inp == '1':
        menu_module.MyApp()
        break
    elif inp == '2':
        menu.test()
        break
    else:
        print("Choose correctly... \n")
