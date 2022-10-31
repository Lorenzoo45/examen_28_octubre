import hashlib

def descifrar():
    try:
        
        print("Desencriptar tu propia clave-->PULSE 1:")
        print("Desencriptar la primera clave-->PULSE 2:")
        opcion = input("Pulse 1 o 2: ")
        if opcion == "2":
            resolverhash = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
        if opcion == "1":
            resolverhash = str(input("Hash a resolver: "))

        type = input("Indica el tipo de encriptación: ")

        resolvedor = open("10-million-password-list-top-1000000.txt", 'r')
        for x in resolvedor.readlines():
            a = x.strip("\n").encode('utf-8')
            if type == 'md5':
                a = hashlib.md5(a).hexdigest()
            elif type == 'sha1':
                a = hashlib.sha1(a).hexdigest()
            elif type == 'sha224':
                a = hashlib.sha224(a).hexdigest()
            elif type == 'sha256':
                a = hashlib.sha256(a).hexdigest()
            elif type == 'sha384':
                a = hashlib.sha384(a).hexdigest()
            elif type == 'sha512':
                a = hashlib.sha512(a).hexdigest()
            else:
                raise Exception('El tipo de encriptación %s no es válido.' %str(type))

            if a == resolverhash:
                print("Contraseña: %s - Has resuelto: %s - Encriptado con: %s" %(str(x.rstrip()),str(a),str(type)))
                break

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    descifrar()



    