import gpiozero
import time
import signal

# Due LED che lampeggiano (in modo diverso) durante l'esecuzione dello script.
blinkLED=gpiozero.LED("BOARD11")
pulseLED=gpiozero.PWMLED("BOARD7")

blinkLED.blick()
pulseLED.pulse()

# Due LED che si scambiano alla pressione di un bottone.
button=gpiozero.Button("BOARD12")
blueLED=gpiozero.LED("BOARD13")
yellowLED=gpiozero.LED("BOARD15")

# Valore binario che indica quale dei due LED si accende.
buttonState=0

# Alla presisone del bottone, uno si spegne e l'altro di accende.
# I due LED si invertono ad ogni pressione del bottone.
# Tra una pressione e l'altra devono passare 200ms.
while True:
	if button.is_pressed:
		buttonState+=1
		print(buttonState)
		time.sleep(0.2)
	if (buttonState%2)==0:
		blueLED.on()
		yellowLED.off()
	else:
		blueLED.off()
		yellowLED.on()
