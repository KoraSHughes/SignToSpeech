python2
	necessary for leap (2.7)
	installed with anaconda
	limitations
		no keyboard module
			so ctl-c to stop data logging
		cv2.imread can only handle png's
			(can use snip & sketch to open and resave as png)
------------------------------------------------------
installing leap libraries
------------------------------------------------------
https://developer-archive.leapmotion.com/documentation/python/devguide/Leap_SDK_Overview.html
	says to use Python Version 2.7.3
	install python 2.7.18, through Anaconda (refer to pythonWindows10.txt)
		2.7.18 is the only 2.7 version available through Anaconda
need to use a legacy release that Aadit found, because latest release doesn't have python libraries
	https://developer.leapmotion.com/releases
		V2.3.1 for Windows
	but this doesn't show up, so I just googled: leap motion v3.2.1
		https://developer.leapmotion.com/releases/leap-motion-orion-321-39frn-3b659
		the download will be the folder: LeapDeveloperKit_3.2.1+45911_win
		move to ~/docs/local/software/
		run the .exe
	then at the top of any .py file:
		import sys
		sys.path.insert(0, "C:/cygwin64/home/jlibby/docs/local/software/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/")
		sys.path.insert(0, "C:/cygwin64/home/jlibby/docs/local/software/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/x64")
		import Leap
