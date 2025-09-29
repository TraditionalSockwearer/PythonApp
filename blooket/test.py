aaa = """
import pip

try:
    import ewee
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
    from gui.widgekts import *
#exception is handled here
except ImportError as ie:
    print(f"Well an error has occured: {ie} \nPress enter to reinstall Or 'no' to do nothing: n")
    a=input().islower
    if a == 'no':
        pass
    else:
        ################################################################################################################################
        import os
        os.system('python.exe -m pip uninstall pyside6')
        os.system('python -m pip uninstall pyside6')
        os.system('python.exe -m pip uninstall pillow')
        os.system('python -m pip uninstall pillow')
        os.system('python.exe -m pip uninstall pyperclip')
        os.system('python -m pip uninstall pyperclip')
        os.system('python.exe -m pip install --user --upgrade pip  --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location')
        os.system('python.exe -m pip install --user pyside6  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        os.system('python.exe -m pip install --user pillow  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        os.system('python.exe -m pip install --user pyperclip  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        os.system('python -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location')
        os.system('python -m pip install --user pyside6 --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        os.system('python -m pip install --user pillow  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        os.system('python -m pip install --user pyperclip  --trusted-host pypi.org --trusted-host files.pythonhosted.org')
        ####################################################################################################################################################################################
"""
b="""
#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
os.system('python -m pip install --user PyQt5 --trusted-host pypi.org --trusted-host files.pythonhosted.org')
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class embeddedTerminal(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self._processes = []
        self.resize(800, 600)
        self.terminal = QWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        self._start_process(
            'xterm',
            ['-into', str(self.terminal.winId()),
             '-e', 'tmux', 'new', '-s', 'my_session']
        )
        button = QPushButton('List files')
        layout.addWidget(button)
        button.clicked.connect(self._list_files)

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)

    def _list_files(self):
        self._start_process(
            'tmux', ['send-keys', '-t', 'my_session:0', 'ls', 'Enter'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = embeddedTerminal()
    main.show()
    sys.exit(app.exec_())
"""
c="""
import subprocess
r = subprocess.check_output('C:/Users/arjun/AppData/Local/Programs/Python/Python37/python.exe -m pip install --user pyside6==6  --trusted-host pypi.org --trusted-host files.pythonhosted.org',
        stdin=None, stderr=None, shell=False, universal_newlines=True)
key = 's94546'
print(r)
if r == f'Requirement already satisfied: pip in c:\\users\\arjun\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
    print('found')
else:
    print('incorrect method')
"""
d=''
import os, sys
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

import subprocess
reslt = subprocess.check_output(f'C:/Users/{result}/AppData/Local/Programs/Python/Python37/python.exe -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location', stdin=None, stderr=None, shell=False, universal_newlines=True)
re = str(reslt)
print(re)
# 1
if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
    print('found')
    instance=f'C:/Users/{result}/AppData/Local/Programs/Python/Python37/python.exe -m '
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
        #3
        if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
            print('found')
            instance = f'python -m '
        else:
            print('incorrect method')
            reslt = subprocess.check_output(
                f'python -m pip install --user --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location',
                stdin=None, stderr=None, shell=False, universal_newlines=True)
            re = str(reslt)
            #4
            print(re)
            if re == f'Requirement already satisfied: pip in c:\\users\\{result}\\appdata\\roaming\\python\\python37\\site-packages (22.1.2)\n':
                print('found')
                instance = f''
            else:
                print('incorrect method')



os.system(f'{instance}pip install --user --upgrade pip  --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-warn-script-location')