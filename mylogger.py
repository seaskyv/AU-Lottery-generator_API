import logging
import os
import platform
from logging.handlers import RotatingFileHandler

def myLogger(name,size,level,maxNum) :
    logLevel = level.upper()
    numericLevel = getattr(logging,logLevel.upper(),10)
    systemType=platform.system()
    if systemType in ("Windows", "Microsoft"):
        logFile = os.path.dirname(os.path.abspath(name)) + '\\' +os.path.basename(name)
    else :
        logFile = os.path.dirname(os.path.abspath(name)) + '/' +os.path.basename(name)

    if not os.path.exists(logFile):
        f = open(logFile,"x")
        f.close()
    logFomatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(process)d] [%(module)s] [%(funcName)s]:[%(lineno)d] %(message)s')
    
    logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=int(size)*1024*1024, backupCount=int(maxNum), encoding=None, delay=0)
    logHandler.setFormatter(logFomatter)
    #logHandler.setLevel(numericLevel)

    aLogging = logging.getLogger()
    aLogging.setLevel(numericLevel)
    aLogging.addHandler(logHandler)
    aLogging.debug("logger init")

    return aLogging