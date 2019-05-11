#           HP3470A_34901A_Data_ACQ_Example.py
#Python Version: 2.7.13
#Date: 08-MAY-2019
#Author: Jarvis Hill (e-mail: hilljarvis@gmail.com)
#Purpose:  This code serves as a reference to control the HP/Keysight 34970A Datalogger with the 34901A switch unit 
#using a prologix GPIB-USB controller.



###############################################################################
# Modules                                                                     #
###############################################################################
import serial
import time



###############################################################################
#Globals                                                                      # 
###############################################################################

#Serial Parameters
port = 'COM11'                  #Addr of GPIB controller connected to Agilent 34970A w/ 34901A module
bytesize = 8
stopbits = 1
parity = 'N'
baud = 57600                    #GPIB controller baud rate
timeout = 10                    #Serial COM timeout

#Data log file
data_log = 'data_log.txt'

#DMM 
N_measurements = 10



###############################################################################
# FUNCTIONS                                                                   #
###############################################################################

##Reads data from DMM##
def read_data(DMM):
    data = ''
    while True:
        ch = DMM.read()
        if ch == '\n': break
        data += ch
    return data


##Identifies DAQ module##
def ID(DMM):
    DMM.write('*IDN?\r')
    instr_id = read_data(DMM)
    print instr_id
    #return instr_id


##Queries voltage measurement from 34901A DAQ module##
def read_voltage(DMM):
    DMM.write('READ?\n')
    voltage = read_data(DMM)
    #print voltage
    return voltage



###############################################################################
# MAIN PROGRAM                                                                #
###############################################################################
def main():

    #Establish Serial COMM with DMM                             
    DMM = serial.Serial(port, baud, timeout=10)

    #Verify Prologix USB-GPIB controller
    DMM.write('++ver\n')
    controller_id = read_data(DMM)
    print controller_id
    time.sleep(1)

    #Instruct USB-GPIB controller to read after write
    DMM.write('++auto 0\n')
    time.sleep(1)

    #set GPIB address of DMM in controller
    DMM.write('++addr 10\n')
    time.sleep(1)

    ##DMM.write('++mode 1')

    ##CONFIGURE DAQ module
    #Mode: DC Volts
    #Range: 100 V
    #Resolution: 0.003    
    DMM.write('CONF:VOLT:DC 100,0.003, (@101, 102, 103)\n')     #Configure channels 
    time.sleep(1)
    DMM.write('ROUTe:CHANnel:DELay 1,(@101, 102, 103)\n')       #Add read delay between specified channels
    time.sleep(0.5)
    DMM.write('ROUTe:SCAN (@101, 102, 103)\n')                  #Define list of channels to be read when the READ?/INITiate/MEASure? cmds are sent
    

    #Instruct USB-GPIB controller to read after write
    DMM.write('++auto 1\n')


    #Open data log file
    f = open(data_log, 'w')

    
    #Read Voltage
    for i in range(0,N_measurements):
        data = read_voltage(DMM)
        print data
        f.write(data+'\n')                                      #Write measurement to log file
        time.sleep(1)


    #Clean-up
    DMM.close()                                                 #Close serial connection with DMM
    f.close()                                                   #Close data log file



if __name__ == "__main__":
    main()
