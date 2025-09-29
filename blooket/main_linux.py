import os, sys

test_names = """
import subprocess
result = subprocess.check_output("whoami")
r = str(result)
key = 's94546'
print(result)
names = ['arjun', '2019asharma']"""
key = 's94546'
result = os.getlogin()
print(result)
if result == "arjun":
    print(key, "found su")
elif result == '2019asharma':
    print(key, "found su")
elif result == '2019jdandison':
    print(key, "found su")

elif result == 'admin':
    print('get a life')
else:
    print(result, "No key")
    exit(123)

################################################################################################################################
os.system('python -m pip install --upgrade pip --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
os.system('python -m pip install pyside6 --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
os.system('python -m pip install pillow --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
os.system('python -m pip install pyperclip --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
####################################################
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

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

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"


# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
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

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
