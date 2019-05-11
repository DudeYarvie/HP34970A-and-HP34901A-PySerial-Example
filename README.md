# HP34970A-and-HP34901A-PySerial-Example
Example code demonstrating how to control the HP34970A datalogger and HP34901A 20-ch MUX using Python.  The Python script communicates to the instrument via the GPIB/HPIB interface using a Prologix GPIB-USB controller.  In addition to the GPIB interface, the datalogger  possesses a RS232 serial interface for instrument control as well.

## File Descriptions
 1. *HP3470A_34901A_Data_ACQ_Example.py* provides the example for using PySerial to control the HP datalogger
 2. *PrologixGpibUsbManual-6.0.pdf* user manual for GPIB controller  
 3. *HP34970A_Quick_CMD_Ref.pdf* summary of the SCPI commands used to program the 34970A mainframe and plug-in modules. 

## Usage
1. Download Python v2.7 (choose 32 or 64 bit based on the your OS bitness)
2. Set the GPIB address of the datalogger following the user manual instructions
3. Connect the Prologix GPIB-USB controller to the host PC and ensure the driver automatically downloads.  The controller should appear as a COM port on your PC if the driver installed correctly.  The driver may be found on the MFG website for manual installation.
4. Connect the Prologix GPIB-USB controller to the GPIB/HPIB port on the back of the datalogger
5. Connect the voltage source(s) to be measured to ch1,2 and or 3 of the HP34901A 20-ch MUX
6. Run the Python script
