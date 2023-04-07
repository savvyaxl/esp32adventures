import board
import analogio

A0 = analogio.AnalogIn(board.A0)

def read():   
    myvalue = A0.value / 65535 * A0.reference_voltage
    #print(myvalue)
    return myvalue
