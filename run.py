from sys import argv
import os
with open("config") as config:
    config = config.read()
    for conf in config.split("\n"):
        try: name, command  = conf.split(":", 1)
        except: continue
        if argv[1] == name: os.system(command)