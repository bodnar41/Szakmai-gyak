import SCP_conn
import SSH_conn
import Encryption

while True:
    print("=================== Sysadmin tools ===================")
    print("1. Check SSH connection.\n2. System info from a remote host.\n3. File encryption and decryption."
          "\n4. Making QR code from remote host's system info.\n5. Folder cleanup on a remote host."
          "\n6. Logging on a remote host.\n0. EXIT")
    choice = int(input("How can I help you? Give me the number of task:"))

    # Checking SSH connection
    if choice == 1:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        SSH_conn.ssh_conn(ip, user, pwd, None)

    # Get sysinfo from a remote computer
    elif choice == 2:
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

    # Encrypt and decrypt a file
    elif choice == 3:
        Encryption.call_functions()

    # Making QR from remote host's sysinfo
    elif choice == 4:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        SCP_conn.scp_conn(ip, user, pwd, "put", "QR_maker.py")
        SSH_conn.ssh_conn(ip, user, pwd, f"python C:/Users/{user}/QR_maker.py")
        SCP_conn.scp_conn(ip, user, pwd, "get", "sysinfo.png")

    # Folder cleanup
    elif choice == 5:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        SCP_conn.scp_conn(ip, user, pwd, "put", "Folder_cleanup.py.py")
        SSH_conn.ssh_conn(ip, user, pwd, f"python C:/Users/{user}/Folder_cleanup.py")
        SCP_conn.scp_conn(ip, user, pwd, "get", "Output.txt")
        with open("C:/Users/kliens01/Output.txt", 'r') as filehandle:
            data = filehandle.read()
            print(data)

    # Logging on a remote host
    elif choice == 6:
        ip = input("IP address:")
        user = input("Username:")
        pwd = input("Password:")
        remote_path = input("Enter the directory:")
        listening_time = input("Enter the time in minutes until listening:")

        transfer_data = [remote_path, listening_time]

        with open("C:/Users/kliens01/info.txt", "w") as filehandle:
            for listitem in transfer_data:
                filehandle.write(f"{listitem}\n")

        SCP_conn.scp_conn(ip, user, pwd, "put", "Logging_host.py")
        SCP_conn.scp_conn(ip, user, pwd, "put", "info.txt")
        SSH_conn.ssh_conn(ip, user, pwd, f"python C:/Users/{user}/Logging_host.py")
        SCP_conn.scp_conn(ip, user, pwd, "get", "log_info.log")

    elif choice == 7:
        pass

    elif choice == 0:
        break
