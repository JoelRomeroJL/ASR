from pysnmp.hlapi import *

def consultaSNMP(comunidad,host,oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad, mpModel=0),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))
    if errorIndication:
        print(errorIndication)
        resultado = "Down"
        return resultado
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            varB=(' = '.join([x.prettyPrint() for x in varBind]))

            cadena = "Windows"
#           sistema= varB.find(cadena)

#            resultado = "Up"

            if cadena in varB:
                print("Windows")
                resultado="UpWindows"
            else:
                print("Linux")
                resultado="UpLinux"


        return resultado
