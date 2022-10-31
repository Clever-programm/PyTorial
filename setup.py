import sys
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [Executable('main.py',
                          targetName='PyTorial.exe',
                          base=base,
                          shortcutName='PyTorial',
                          shortcutDir='CleverProduction'
                          )]

includes = ['altgraph', 'build', 'click', 'colorama',
            'future', 'gcloud', 'httplib2', 'PIL', 'socks',
            'jws', 'oauth2client', 'packaging', 'pefile',
            'pep517', 'pyasn1', 'pyparsing', 'pyperclip',
            'PyQt5', 'pyrebase', 'requests', 'rsa',
            'six', 'soupsieve', 'tomli', 'wikipedia', 'wx']

excludes = []

zip_include_packages = []


include_files = ['Data']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'include_files': include_files,
    }
}

setup(name='PyTorial',
      version='1.0',
      description='Clever Production: PyTorial',
      executables=executables,
      options=options)