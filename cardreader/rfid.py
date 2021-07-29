import smartcard
#from smartcard.util import toHexString
import time
import numpy as np

def parseRFID():
    while True:
        time.sleep(0.5)
        try:
            reader = smartcard.System.readers()
            if not reader:
                print("No readers")
                return None
            else:
                conn =  reader[0].createConnection()
                conn.connect()
                #[0xFF, 0x82, 0x00, 0x00, 0x06,KEY(6 bytes)]
                LOADKEY = [0xFF, 0x82, 0x00, 0x00, 0x06,255,255,255,255,255,255]
                response = conn.transmit(LOADKEY)
                if response[1] == 144:
                    #print("Key A loaded successfully")
                    time.sleep(1)
                    #auth block
                    # COMMAND = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, BLOCK, KEY-TYPE, 0x00]
                    COMMAND = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x00, 0x60, 0x00]
                    response = conn.transmit(COMMAND)
                    #print(response)
                    time.sleep(2)
                    #[0xFF, 0xB0, 0x00, BLOCK-NUMBER, 0x10]
            #        read = [0xFF, 0xB0, 0x00, 0x00, 0x10] #Read block 0
                    read = [0xFF, 0xB0, 0x00, 0x04, 0x10] #Read block 0
                    data=''
                    try:
                        data, sw1, sw2 = conn.transmit(read)
                        #data, sw1, sw2 = cs.connection.transmit(getuid)
                    except smartcard.Exceptions.NoCardException:
                        pass
                    except smartcard.Exceptions.CardConnectionException:
                        pass
                    #pdata=toHexString(data) 
                    if (len(data)>0):
                        indx=9
                        str=''
                        while (indx<=16):
                            if (data[indx]==254):
                                break
                            else:
                                str=str+chr(data[indx])

                            indx = indx +1

                        return str
                else:
                    return None
        except smartcard.Exceptions.NoCardException:
            pass
        except smartcard.Exceptions.CardConnectionException:
            pass
            
if __name__ == '__main__':

    while True:
        try:
            data=parseRFID()
            print(data)
        except smartcard.Exceptions.NoCardException:
            pass
        except smartcard.Exceptions.CardConnectionException:
            pass        
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    sys.exit()

