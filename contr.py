import SCP_conn
import SSH_conn
import Encryption

while True:
    print("1. System info from a remote host.\n2. File encryption and decryption.")
    choice = int(input("How can I help you? Give me the number of taks:"))

    #Get sysinfo from a remote computer
    if choice == 1:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        info = input("Number of info: \n1. Sysinfo \n2. CPU info \n3.Frequency info \n4. Core info\n")


        file = open('C:/Users/kliens01/teszt.txt', 'w')
        file.write(info)
        file.close()

        SCP_conn.scp_conn(ip, user, pwd, "put")
        SSH_conn.ssh_conn(ip, user, pwd)
        SCP_conn.scp_conn(ip, user, pwd, "get")

    #Encrypt and decrypt a file
    elif choice == 2:
        Encryption.call_functions()

    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 0:
        break
