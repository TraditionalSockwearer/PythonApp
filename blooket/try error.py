try:
    import os
    os.system('python.exe -m pip uninstall pyside6')
    os.system('python -m pip uninstall pyside6')
    os.system('python.exe -m pip uninstall pillow')
    os.system('python -m pip uninstall pillow')
    os.system('python.exe -m pip uninstall pyperclip')
    os.system('python -m pip uninstall pyperclip')

except ImportError as ie:
    print('error')


