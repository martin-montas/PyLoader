from PyLoader.basiclayout   import InitialLayout
from PyLoader.topMenu       import TopDefaultMenu
from PyLoader.requestText   import RequestText
from PyLoader.urlEntry      import UrlEntry

class PyLoader:
    '''
    '''
    def __init__(self, root):
        self.root           =   root
        self.bg             =   "#808080"
        self.fg             =   "black"
        self.bg2            =   "#D3D3D3"
        self.basiclayout    =   InitialLayout(self.root)
        self.topmenu        =   TopDefaultMenu(root, self.bg, self.fg)
        self.urlEntry        =   UrlEntry(root, width=30)
        self.basiclayout.init()
        self.topmenu.init()

        RequestText(self.root, self.bg2,width=0,height=0)
        self.root.config(bg=self.bg)
