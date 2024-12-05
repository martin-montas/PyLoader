from PyLoader.topMenu       import TopDefaultMenu

class PyLoader:
    '''
    '''
    def __init__(self, root):
        # use for x: 20
        self.root           =   root
        self.bg             =   "lightgrey"
        self.fg             =   "black"




        TopDefaultMenu(root)
        self.root.config(bg=self.bg)



