"""
This file will be run as a deamon and wil communicate with the chip
"""
import pyinotify
import asyncore
import json

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CLOSE_WRITE

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        f = open(event.pathname,'r')
        impression(json.load(f))

def impression(x):
    print(x)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/guillaume/git_folder/Light_server/comm_file', mask, rec=True)
notifier.loop()
