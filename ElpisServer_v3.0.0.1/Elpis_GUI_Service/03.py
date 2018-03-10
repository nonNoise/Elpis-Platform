#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
# pip install wxpython
import subprocess

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.SetSize((300, 300))
        self.RUN_button = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("01run.png", wx.BITMAP_TYPE_ANY))
        self.STOP_button = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("01stop.png", wx.BITMAP_TYPE_ANY))
        self.RUN_button.SetBackgroundColour('#8FC31F')
        #self.bitmap_button_2.SetBackgroundColour('#EA5536')
        self.STOP_button.SetBackgroundColour('#C9CACA')
        self.STOP_button.Disable()
        self.Bind(wx.EVT_CLOSE, self.closeEvent)
        self.Bind(wx.EVT_BUTTON, self.RunBottonClick, self.RUN_button)
        self.Bind(wx.EVT_BUTTON, self.StopBottonClick, self.STOP_button)
        self.__do_layout()
        # end wxGlade

 
    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(0, 1, 0, 0)
        grid_sizer_1.Add(self.RUN_button, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.STOP_button, 0, wx.EXPAND, 0)
        grid_sizer_1.SetSizeHints(self)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade
    def closeEvent(self,event):
        try :
            print(self.server.poll())
            self.server.kill()
            self.Destroy()
        except AttributeError:
            self.Destroy()
        except OSError:
            self.Destroy()
    def RunBottonClick(self,event):
        self.RUN_button.SetBackgroundColour('#C9CACA')
        self.STOP_button.SetBackgroundColour('#EA5536')
        self.RUN_button.Disable()
        self.STOP_button.Enable()

        #self.server = subprocess.Popen( ["python3", "./elpis_v2/Elpis.py"] ) 
        self.server = subprocess.Popen( ["python3","server.py"]) 
        self.SetStatusText('RUN....%d' % (self.server.pid))
        import webbrowser
        #b= webbrowser.get('safari')
        #b.open_new_tab("http://localhost:1234")
        webbrowser.open_new_tab("http://localhost:1234")
        
	#run(host='localhost', port=1234)
 

    def StopBottonClick(self,event):
        self.RUN_button.SetBackgroundColour('#8FC31F')
        self.STOP_button.SetBackgroundColour('#C9CACA')
        self.STOP_button.Disable()
        self.RUN_button.Enable()
        self.server.kill()
        print(self.server.poll())
        self.SetStatusText('STOP....')

if __name__=='__main__':
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "ElsipService.")
    icon=wx.Icon('AN.ico',wx.BITMAP_TYPE_ICO)
    frame_1.SetIcon(icon)
    frame_1.CreateStatusBar()
    frame_1.SetStatusText('Hello Elpis Service.')

    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()