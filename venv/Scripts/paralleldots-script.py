#!C:\Users\shubom\PycharmProjects\myproject\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ParallelDots==3.2.8','console_scripts','paralleldots'
__requires__ = 'ParallelDots==3.2.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ParallelDots==3.2.8', 'console_scripts', 'paralleldots')()
    )
