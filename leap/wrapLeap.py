##For installation, refer to robotSoft01/notes/installation/leap.txt
##This script:
##  captures data from the leap camera
##  saves a sequence of leap images to file in: <dirParent>/trials/
##    make sure <dirParent>/trials/ exists before running this script.
##  It also plots images to screen, if isImShow = True

import getpass
usrCur = getpass.getuser()# 'jlibby', 'Aadit Patel' (no backslah), 'naiga', ...
import sys
dirLeapLib = 'C:/cygwin64/home/' + usrCur + '/docs/local/software/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/'
sys.path.insert(0, dirLeapLib)
sys.path.insert(0, dirLeapLib + '/x64' )
import Leap
import funcsLeap

def main():
    dirParent = 'C:/cygwin64/home/' + usrCur + '/docs/local/data/dataSoft01/initialTests/cameras/leap/'
    #dirTrial = dirParent + 'checkerboard03/'
    dirTrial = dirParent + 'trials/'
    isImShow = True

    duration = -1 #in secs. if -1, press ctl-c to quit. Otherwise, quite after duration

    ##freqDesired (it's a bit hacky. I'll use timeLastIt)
    ##    with imshow, 50Hz (should be 500 images)
    ##      without timeLastIt: 318, 315; 318, 317 (avg freq 31.7)
    ##      with timeLastIt: 523, 532; 558, 552, 554 (avg freq 54.38)
    ##    without imshow, 50Hz (should be 500 images)
    ##      without timeLastIt: 475, 475, 474 (avg freq 47.47)
    ##      with timeLastIt: 502, 502, 502 (avg freq 50.02)
    ##    with imshow, 30Hz (should be 300 images)
    ##      without timeLastIt: 214, 213 (avg freq 21.35)
    ##      with timeLastIt: 319, 319 (avg freq 31.9)
    ##    without imshow, 30Hz (should be 300 images)
    ##      without timeLastIt: 291, 291, 291 (avg freq 29.1)
    ##      with timeLastIt: 300, 300, 300 (avg freq 30)
    ##    with imshow, 15Hz (should be 150 images)
    ##      without timeLastIt: 127, 128, 127, 129, 128 (avg freq 12.78)
    ##      with timeLastIt: 161, 162, 161 (avg freq 16.13)
    ##    without imshow, 15Hz (should be 150 images)
    ##      without timeLastIt: 148, 148, 148 (avg freq 14.8)
    ##      with timeLastIt: 150, 150, 150 (avg freq 15)
    freqDesired = 15 #Hz

    controller = Leap.Controller()
    controller.set_policy_flags(Leap.Controller.POLICY_IMAGES)
    try:
        funcsLeap.run(controller,dirParent,dirTrial,freqDesired,duration,isImShow)
    except KeyboardInterrupt:
        sys.exit(0)
    #end except KeyboardInterrupt:
##end def main():

if __name__ == '__main__':
    main()
##end if __name__ == '__main__':
