import subprocess
import sys
import os
from tkinter import messagebox, Tk

# List of Motorola apps to uninstall
apps_to_uninstall = [
    "com.motorola.bug2go",
    "com.motorola.gesture",
    "com.motorola.motofpstouch",
    "com.motorola.android.fmradio",
    "com.motorola.stylus",
    "com.motorola.nfwlocationattribution",
    "com.motorola.faceunlock",
    "com.motorola.hiddenmenuapp",
    "com.motorola.photoeditor",
    "com.motorola.timeweatherwidget",
    "com.motorola.colorbook",
    "com.motorola.invisiblenet",
    "com.motorola.contacts.preloadcontacts",
    "com.motorola.appdirectedsmsproxy",
    "com.motorola.launcherconfig",
    "com.motorola.spectrum.setup.extensions",
    "com.motorola.demo",
    "com.motorola.help",
    "com.motorola.dynamicvolume",
    "com.motorola.launcher3",
    "com.motorola.android.overlay.common",
    "com.motorola.bach.modemstats",
    "com.motorola.android.providers.chromehomepage",
    "com.motorola.motodisplay",
]

# Ask the user for confirmation to proceed
root = Tk()
root.withdraw()
root.attributes("-topmost", True)
result = messagebox.askquestion("SSUNOs de-m0t0", "Welcome to SSUNOs de-m0t0, press (Y) to Continue... press (N) to exit.", icon='warning')

if result == 'yes':
    try:
        # Check for dependencies before proceeding
        subprocess.check_call(['adb', 'version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "ADB is not installed or not in the system PATH.")
        sys.exit(1)

    # Uninstall the specified Motorola apps
    for app in apps_to_uninstall:
        try:
            subprocess.check_call(['adb', 'shell', 'pm', 'uninstall', '--user', '0', app])
            print(f"{app} has been uninstalled.")
        except subprocess.CalledProcessError:
            print(f"Failed to uninstall {app}.")
else:
    sys.exit(0)

# Hide the terminal window
if os.name == 'nt':
    # Windows platform
    import win32gui, win32con
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
else:
    # Linux platform
    import subprocess
    subprocess.Popen('setterm -cursor off', shell=True)
    subprocess.Popen(['xdotool', 'getactivewindow', 'windowminimize'])
