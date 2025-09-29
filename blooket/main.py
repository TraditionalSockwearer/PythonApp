# Error code 123 = login error
# Error code 10 = Import error / restart
# Error code 0 = App closed
#
#
#
#
#
#
import os, sys
import subprocess
key = 's94546'
result = os.getlogin()
print(result)
if result == "arjun":
    print(key, "found su")
elif result == '2019ASharma':
    print(key, "found su")
elif result == '2019asharma':
    print(key, "found su")
elif result == 'admin':
    print('get a life')
elif result == '2019HLegg':
    print(key, "found su")
elif result == '2019hlegg':
    print(key, "found su")
elif result == '2019Hlegg':
    print(key, "found su")
elif result == '2019JDandison':
    print(key, "found su")
elif result == '2019jdandison':
    print(key, "found su")
elif result == '2019Jdandison':
    print(key, "found su")
else:
    print(result, "No key")
    exit(123)
reslt = subprocess.check_output(
    f'C:/Users/{result}/AppData/Local/Programs/Python/Python37/python.exe -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
    stdin=None, stderr=None, shell=False, universal_newlines=True)
reslt2 = subprocess.check_output(
    f'python.exe -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
    stdin=None, stderr=None, shell=False, universal_newlines=True)
reslt3 = subprocess.check_output(
    f'python -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
    stdin=None, stderr=None, shell=False, universal_newlines=True)
reslt4 = subprocess.check_output(
    f'pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
    stdin=None, stderr=None, shell=False, universal_newlines=True)
re = str(reslt)
print(re)
re1 = str(reslt2)
print(re1)
re2= str(reslt3)
print(re2)
re3 = str(reslt4)
print(re3)
# 1
if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
    print('found')
    instance = f'C:/Users/{result}/AppData/Local/Programs/Python/Python37/python.exe -m '
else:
    print('incorrect method')
    reslt = subprocess.check_output(
        f'python.exe -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
        stdin=None, stderr=None, shell=False, universal_newlines=True)
    re = str(reslt)
    # 2
    print(re)
    if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
        print('found')
        instance = f'python.exe -m '
    else:
        print('incorrect method')
        reslt = subprocess.check_output(
            f'python -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
            stdin=None, stderr=None, shell=False, universal_newlines=True)
        re = str(reslt)
        print(re)
        # 3
        if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
            print('found')
            instance = f'python -m '
        else:
            print('incorrect method')
            reslt = subprocess.check_output(
                f'python -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
                stdin=None, stderr=None, shell=False, universal_newlines=True)
            re = str(reslt)
            # 4
            print(re)
            if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
                print('found')
                instance = f''
            else:
                print('incorrect method')
try:
    import pyperclip
except ImportError as o:
    print('not installed')
    os.system(f'{instance}pip uninstall pyside6')
    os.system(f'{instance}pip uninstall pillow')
    os.system(f'{instance}pip uninstall pyperclip')
    os.system(f'{instance}pip install --user --upgrade pip  --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location')
    os.system(f'{instance}pip install --user pyside6  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
    os.system(f'{instance}pip install --user pillow  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
    os.system(f'{instance}pip install --user pyperclip  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
try:
    # IMPORT PACKAGES AND MODULES
    # ///////////////////////////////////////////////////////////////
    from gui.uis.windows.main_window.functions_main_window import *

    # IMPORT QT CORE
    # ///////////////////////////////////////////////////////////////
    from qt_core import *
    import pyperclip

    # IMPORT SETTINGS
    # ///////////////////////////////////////////////////////////////
    from gui.core.json_settings import Settings

    # IMPORT PY ONE DARK WINDOWS
    # ///////////////////////////////////////////////////////////////
    # MAIN WINDOW
    from gui.uis.windows.main_window import *

    # IMPORT PY ONE DARK WIDGETS
    # ///////////////////////////////////////////////////////////////
    from gui.widgets import *
    from gui.uis.pages.files_rc import *

    # IMPORT MATERIALS
    # //////////////////////////////////////////////////////////////
    from gui.uis.pages.files_rc import *

except ImportError as ie:
    print(f"Well an error has occured: {ie} \nPress enter to reinstall if 'n' is present it will stop")
    a = input()
    if a == 'n':
        print('wow')
    elif a == 'N':
        print('wow')
    else:
        ################################################################################################################################
        try:
            import os

            os.system(
                f'{instance}pip uninstall pyside6')

            os.system(
                f'{instance}pip uninstall pillow')

            os.system(
                f'{instance}pip uninstall pyperclip')

            os.system(
                f'{instance}pip install --user --upgrade pip  --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location')

            os.system(
                f'{instance}pip install --user pyside6  --trusted-host pypi.org --trusted-host files.pythonhosted.org')

            os.system(
                f'{instance}pip install --user pillow  --trusted-host pypi.org --trusted-host files.pythonhosted.org')

            os.system(
                f'{instance}pip install --user pyperclip  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        except OSError as osio:
            print(
                f'Os issue: {osio}')

        exit(10)
        ####################################################################################################################################################################################
login(True, True)
# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"


# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Get Title Bar Btn And Reset Active
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
        if btn.objectName() == "btn_page_2":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        if btn.objectName() == "btn_page_3":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one(btn.objectName())

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

            # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        print(p)


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication()
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
