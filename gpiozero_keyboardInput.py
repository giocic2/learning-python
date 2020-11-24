import gpiozero
import signal
import curses

led11=gpiozero.LED("BOARD7")
led12=gpiozero.LED("BOARD11")
led21=gpiozero.LED("BOARD12")
led22=gpiozero.LED("BOARD13")
led31=gpiozero.LED("BOARD15")
led32=gpiozero.LED("BOARD16")

ledMatrix=[[led11,led12],[led21,led22],[led31,led32]]

# Si inizia dal led in posizione (1,1).
# Ricorda che Python è zero-based.
rowIndex=0
columnIndex=0
ledMatrix[rowIndex][columnIndex].on()



# Funzioni per spostarsi.
def up(row,column):
	if (row>0):
		row-=1
	return row,column

def down(row,column):
	if (row<2):
		row+=1
	return row,column

def left(row,column):
	if (column>0):
		column-=1
	return row,column

def right(row,column):
	if (column<1):
		column+=1
	return row,column

# Dizionario delle azioni possibili con la tastiera.
actions = {
	curses.KEY_UP: up,
	curses.KEY_DOWN: down,
	curses.KEY_LEFT: left,
	curses.KEY_RIGHT: right,
}


def main(window):
	global rowIndex
	global columnIndex
	while True:
		key = window.getch()
		action=actions.get(key)
		ledMatrix[rowIndex][columnIndex].off()
		rowIndex,columnIndex=action(rowIndex,columnIndex)
		#print("Row: "+str(rowIndex+1)+", Column: "+str(columnIndex+1))
		ledMatrix[rowIndex][columnIndex].on()

curses.wrapper(main)
