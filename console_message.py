HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
import datetime

def log(event,message, timestamp=False):
    timestamp = ''
    string = ''
    if event == HEADER:
        string = "["+HEADER+datetime.datetime.now.isoformat(' ')+ENDC+']'+message
    elif event == OKBLUE:
        string = "["+OKBLUE+datetime.datetime.now().isoformat(' ')+ENDC+']'+message
    elif event == OKGREEN:
        string = "["+OKGREEN+datetime.datetime.now().isoformat(' ')+ENDC+']'+message
    elif event == WARNING:
        string = "["+WARNING+datetime.datetime.now().isoformat(' ')+ENDC+']'+message
    elif event == FAIL:
        string = "["+FAIL+datetime.datetime.now().isoformat(' ')+ENDC+']'+message
    print(string)
