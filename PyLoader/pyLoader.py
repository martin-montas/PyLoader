from PyLoader.basiclayout   import InitialLayout

class PyLoader:
    '''
    '''
    def __init__(self, root):
        # use for x: 20
        self.root           =   root
        self.bg             =   "lightgrey"
        self.fg             =   "black"

        InitialLayout(self.root)
        self.root.config(bg=self.bg)



