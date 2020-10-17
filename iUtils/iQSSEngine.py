'''
	Author: Mohammed Al Ameen
	Github: https://github.com/Mohammed2702/
	E-Mail: ameenmohammed2311@gmail.com
'''

'''
	QSS Engine	
'''


class Engine:
	def __init__(
		self,
		styles:dict={},
		styleSheet:str='',
		sheetSeperator:str='',
		autoCompile:bool=True
		):
		super(Engine, self).__init__()

		self.styles = styles
		self.styleSheet = styleSheet
		self.sheetSeperator = sheetSeperator
		self.autoCompile = autoCompile

		self.compiledStyles = ''

		if self.autoCompile:
			self.defaultCompile()

	def defaultCompile(self):
		styles = self.styles
		styleSheet = self.styleSheet

		lines = open(styleSheet, mode='r').readlines()
		
		first_line = f'{lines[0]}' if len(lines) > 0 and len(lines[0]) > 1 else '{'
		last_line = f'{lines[-1]}' if len(lines) > 0 and len(lines[-1]) > 1 else '}'

		compiledStyles = open(styleSheet, mode='w')

		compiledStyles.write(first_line)

		newStyles = ''

		for style in list(styles.keys()):
			property_ = style
			value_ = styles[style]
			style = f'\t{property_}: {value_};\n'

			newStyles += style

		compiledStyles.write(newStyles)
		compiledStyles.write(last_line)

		self.compiledStyles = compiledStyles

		return True

	def customCompile(self, styles, styleSheet):
		lines = open(styleSheet, mode='r').readlines()
		
		first_line = f'{lines[0]}' if len(lines) > 0 and len(lines[0]) > 1 else '{'
		last_line = f'{lines[-1]}' if len(lines) > 0 and len(lines[-1]) > 1 else '}'

		compiledStyles = open(styleSheet, mode='w')

		compiledStyles.write(first_line)

		newStyles = ''

		for style in list(styles.keys()):
			property_ = style
			value_ = styles[style]
			style = f'\t{property_}: {value_};\n'

			newStyles += style

		compiledStyles.write(newStyles)
		compiledStyles.write(last_line)

		self.compiledStyles = compiledStyles

		return True

	def __str__(self):
		return open(self.compiledStyles.name, mode='r').read()


engine = Engine(
	styles={
		'width': '40px',
		'height': '100px',
		'background-color': 'red',
		'color': 'green',
		'border': '1px solid black'
	},
	styleSheet='/home/mohammed/Desktop/Projects/iPyQt5/iQSS/Engine.css',
	autoCompile=True
)
print(engine)
