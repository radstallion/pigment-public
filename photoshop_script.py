from comtypes.client import CreateObject

def connectToPSD():
    dispatchCom = CreateObject("Photoshop.Application.80")
    return dispatchCom
