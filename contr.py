import SCP_conn
import SSH_conn
import Encryption

while True:
    print("1. System info from a remote host.\n2. File encryption and decryption."
          "\n 3. Making QR code from remote host's system info.")
    choice = int(input("How can I help you? Give me the number of taks:"))

    #Get sysinfo from a remote computer
    if choice == 1:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        info = input("Number of info: \n1. Sysinfo \n2. CPU info \n3.Frequency info \n4. Core info\n")

        transfer_data = [info, user]

        with open("C:/Users/kliens01/teszt.txt", "w") as filehandle:
            for listitem in transfer_data:
                filehandle.write(f"{listitem}\n")

        SCP_conn.scp_conn(ip, user, pwd, "put", "system_info.py")
        SCP_conn.scp_conn(ip, user, pwd, "put", "teszt.txt")
        SSH_conn.ssh_conn(ip, user, pwd, f"python C:/Users/{user}/info.py")
        SCP_conn.scp_conn(ip, user, pwd, "get", "system_info.json")

    #Encrypt and decrypt a file
    elif choice == 2:
        Encryption.call_functions()

    elif choice == 3:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        SCP_conn.scp_conn(ip, user, pwd, "put", "qr_maker.py")
        SSH_conn.ssh_conn(ip, user, pwd, f"python C:/Users/{user}/qr_maker.py")
        SCP_conn.scp_conn(ip, user, pwd, "get", "sysinfo.png")

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
