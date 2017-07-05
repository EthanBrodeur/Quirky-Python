import commands


def detect_caps_lock():
#thanks to user 'ronak' of SO
    caps =  (commands.getoutput('xset q | grep LED')[65] == '1')
    if caps:
        print('Your Caps Lock is on')

detect_caps_lock()

