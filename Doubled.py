
import platform
import os
os.system('termux-setup-storage')
os.system('python -m pip uninstall urllib3 && python -m pip install urllib3')
os.system('git pull')
try:os.system('touch .prox.txt')
except:pass
try:os.system('rm -rf .token.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("Dumerlib").ninex()
else:
	exit(f' Unknow device machine {arc}')












