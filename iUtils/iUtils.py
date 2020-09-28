import configurations
import os
from iQSS import genericVariables


BASE_DIR = configurations.BASE_DIR
QSS_DIR = configurations.QSS_DIR
GENERIC_VARIABLES = genericVariables.variables


def dictMerger(*args):
    dictionary = {}

    for i in args:
        dictionary = {
            **dictionary,
            **i
        }
    
    return dictionary


def readQSS(qss, qssVariables, output_file, boundary):
    qss = open(qss, mode='r').read().split(boundary)[1].split(boundary)[0]
    
    qssVariables = dictMerger(GENERIC_VARIABLES, qssVariables)
    output_file = os.path.join(QSS_DIR, output_file)

    variables = list(qssVariables.keys())
    values = list(qssVariables.values())

    for i in variables:
        qss = qss.replace(f'${i}', str(values[variables.index(i)]))

    theme = open(output_file, mode='w')
    theme.write(qss)

    return qss


def findReplace(qss, old, new, keywords):
	qss = qss.split(keywords)[1].split(keywords)[0].replace(
		f'{old}',
		f'{new}'
	)

	return qss
