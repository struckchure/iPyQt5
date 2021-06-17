from app.utils import readToText


class StyleParser:

    '''
    Parse stylesheets and deserialize to class names

    ```
        style = StyleParser(
            file="/home/user/style.css"
        )
        page = Page() # Widget
        page.setStyleSheet(
            style.use(
                'p-1',
                'py-4',
                'mx-auto',
                'bg-gray-500',
                'overflow-auto'
            )
        )
    ```
    '''

    def __init__(self, file):
        self.styleSheet = readToText(file)
    
    def formatStyle(self, style):
        curlyBraceOpenPos = style.find('{') + 1
        curlyBraceClosePos = style.find('}')

        formattedStyle = style[curlyBraceOpenPos:curlyBraceClosePos].strip()

        return formattedStyle

    def getClass(self, objectName, className, formatStyle=True):
        targetPosStart = self.styleSheet.find(className)
        targetPosEnd = self.styleSheet[targetPosStart:].find('}')

        style = self.styleSheet[targetPosStart:][:targetPosEnd]
        objectName = str(objectName)\
            .replace('[', '')\
            .replace(']', '')\
            .replace("'", "")

        if formatStyle:
            # style = f'{objectName} {self.formatStyle(style)}'
            style = '%s {%s}' % (objectName, self.formatStyle(style))

        return style

    def getClasses(self, classNames, *args, **kwargs):
        style = ''

        if not kwargs.get('objectName'):
            kwargs['objectName'] = ''

        for className in classNames:
            kwargs['className'] = className
            style += self.getClass(*args, **kwargs)

        return style

    def getPsuedoClasses(self, objectName, psuedoClass, selectorSymbol='::', *args, **kwargs):
        '''
        objectName='QPushButton',
        psuedoClass={
            'focus': [
                'bg-red-500'
            ],
            'hover': [
                'bg-red-800'
            ]
        }
        '''

        style = ''

        objectName = str(objectName)\
            .replace('[', '')\
            .replace(']', '')\
            .replace("'", "")

        for psuedo in psuedoClass.keys():
            classNames = psuedoClass[psuedo]
            psuedoProperty = psuedo
            getStyle = ''

            for className in classNames:
                getStyle += self.getClass('', className, *args, **kwargs)\
                    .replace('{', '')\
                    .replace('}', '')

            psuedo_style = "%s%s%s {%s}" % (
                objectName,
                selectorSymbol,
                psuedoProperty,
                getStyle
            )

            style += psuedo_style

        return style
