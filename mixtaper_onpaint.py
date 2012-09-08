import wx
import os
import sys
import subprocess
import json

gameRoot = os.path.join(".","Games")
cassette_files = ["sideA.jpg", "sideB.jpg"]
gameList = {}

try:
    fh = open("games.txt", "r")
    gamelistJSON = "\n".join(fh.readlines())
    fh.close()
    
    gameList = json.loads(gamelistJSON)
except ValueError:
    print "Error reading gamelist.txt: text is not formatted correctly"
    sys.exit(0)


########################################################################
class MainPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent, images):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        #self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent
        self.images = images
        self.currentSide = 0
        self.bmp = images[0]
        self.sideB = images[1]
 
        sizeX = self.bmp.GetWidth()
        sizeY = self.bmp.GetHeight()
        centerX = sizeX/2
        centerY = sizeY/2
        
        self.chooser = wx.Choice(self, -1, pos=(90,65), size=(300,20), choices = gameList.keys())
        #sizer.Add(chooser, 0, wx.ALL)
 
        playButton = wx.Button(self, -1, "PLAY", pos=(centerX-50, sizeY-70), size=(100,20))
        flipButton = wx.Button(self, -1, "FLIP", pos=(sizeX-60, sizeY-70), size=(40,20))
        quitButton = wx.Button(self, -1, "X", pos=(sizeX-40, 10), size=(20,20))

 
        playButton.Bind(wx.EVT_BUTTON, self.OnPlay)
        flipButton.Bind(wx.EVT_BUTTON, self.OnFlip)
        quitButton.Bind(wx.EVT_BUTTON, self.OnQuit)
 
    def OnPlay(self, evt):
        gamenames = gameList.keys()
        gameName = gamenames[self.chooser.GetSelection()]
        gamePath = os.path.join(gameRoot, gameList[gameName])
        
        dirName = os.path.dirname(gamePath)
        exeName = os.path.basename(gamePath)
        
        print gamePath
        
        os.chdir(dirName)
        subprocess.call(exeName)
        os.chdir(gameRoot)
    
    def OnFlip(self, evt):
        if self.currentSide == 0:
            self.currentSide = 1
        else:
            self.currentSide = 0
        
        wx.PostEvent(self, wx.EraseEvent())
    
    def OnQuit(self, evt):
        self.frame.Destroy()
 
 
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""		
        image_sideA = wx.Bitmap(cassette_files[0])
        image_sideB = wx.Bitmap(cassette_files[1])
        self.bmp = image_sideA
        
        windowWidth = image_sideA.GetWidth()
        windowHeight = image_sideA.GetHeight()
        
        wx.Frame.__init__(self, None, size=(windowWidth,windowHeight),style=wx.FRAME_SHAPED)
        panel = MainPanel(self, [image_sideA, image_sideB])
        
        r = wx.RegionFromBitmap(self.bmp)
        self.SetShape(r)
        
        self.Show()
        self.Center()
        
        # The paint stuff is only necessary if doing a shaped window
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        
        
########################################################################
class Main(wx.App):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()

 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.MainLoop()