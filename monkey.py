import sys  
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage  
#我  
  
def insertNote(d):  
    d.startActivity(component='com.example.android.notepad/.NotesList')  
    print 'insert a new note'  
    MonkeyRunner.sleep(2)  
    d.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)  
    MonkeyRunner.sleep(2)  
  
    result=d.takeSnapshot()  
    result.writeToFile('shot1.png','png')  
    MonkeyRunner.sleep(2.0)  
  
    d.touch(267,905,MonkeyDevice.DOWN_AND_UP)  
    MonkeyRunner.sleep(5)  
    d.type("hello")  
    MonkeyRunner.sleep(1)  
    d.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)  
    print 'wwwwwwwwwwwwwwwwww'  
    MonkeyRunner.sleep(15)  
    d.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)  
    print "insert Successfully"  
    MonkeyRunner.sleep(5)  
  
  
def main():  
    print 'start'  
    device=MonkeyRunner.waitForConnection()  
    if not device:  
        print 'couldn\'t get connection'  
        sys.exit()  
    print 'found device'  
  
    insertNote(device)  
  
if __name__=='__main__':  
    main()