#  -*- coding: utf-8 -*-
# note: windows console dies because utf-8 encoding.
# run command 'chcp 65001' in console to fix console encoding.
# importing ctypes to do some windows magic shit.
import ctypes
import mal2


# note: windll is windows only. need alternative solution to do this in *nix systems.
# what do?
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
 
titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
    	length = GetWindowTextLength(hwnd)
    	buff = ctypes.create_unicode_buffer(length + 1)
    	GetWindowText(hwnd, buff, length + 1)
    	titles.append(buff.value)
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)
 
for title in titles:
	print(title)