import pyperclip

f = open('lib/index.html', 'r')
pyperclip.copy(f.read())
