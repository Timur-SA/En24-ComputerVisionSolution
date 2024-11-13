import json as js

with open('config.json', 'r', encoding='utf-8') as config_file:
    cf = js.load(config_file)

    #Project Assemblies
    version = cf["version"]
    windowName = cf["windowName"] + ". Version: " + version

    #Colours


    #Sources
    sourceImage = cf["path"]