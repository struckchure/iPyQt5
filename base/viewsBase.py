from base.layoutsBase import LayoutBase


class ViewBase(LayoutBase):

    MOUNTED = False
    LOADED = False

    def __init__(self, *args, **kwargs):
        super(ViewBase, self).__init__(*args, **kwargs)

        '''
        Use default settings => setDefaults()
        '''
        self.setDefaults()

        self.runPre()
        self.runPost()

    def setDefaults(self):
        pass

    def runPre(self):
        '''
        Run methods before rendering
        '''
        self.beforeMount()

    def runPost(self):
        '''
        run methods after rendering
        '''
        self.didMount()

    def didMount(self):
        self.MOUNTED = True
        self.LOADED = True

    def beforeMount(self):
        pass
