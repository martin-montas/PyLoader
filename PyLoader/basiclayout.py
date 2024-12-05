from tkinter                    import messagebox
from PyLoader.sendButton        import SendButton
from PyLoader.urlEntry          import UrlEntry
from PyLoader.requestBox       import RequestBox

class InitialLayout:
  '''
        Initiatests the basic layout

        @param root - the root window
        @return None
  '''
  def __init__(self, root):
    self.root         = root
    self.x            = 140
    self.y            = 100
    self.left_pad     = 20
    self.fg           = "white"
    self.button_bg    = "#f58216"
    self.button_fg    = "white"
    self.bg           = "#4B3C31"
    self.bg2          = "#D3D3D3"
    self.win_width    = self.root.winfo_width()
    self.win_height   = self.root.winfo_height()

    RequestBox(self.root)

    button_rel = 69 
    # clear button for the RequestBox
    SendButton(
    self.root, "Clear",
    self.button_bg, "white",
    x=(280 - button_rel), y=709, width=10, height=0)

    # paste button for the RequestBox
    SendButton(
    self.root, "Paste",
    self.button_bg, "white",
    x=(400 - button_rel), y=709, width=10, height=0)
    UrlEntry(self.root, width=30)

  def option_selected(self, value):
     messagebox.showinfo("Selected Option", value)

  def init(self):
      pass
