import paramiko, socket, sys

def scp_conn(ip = None, user = None, pwd = None, action = None, filename = None):
    if ip is None:
        ip = input("Enter Server IP Address :")
    if user is None:
        user = input("Enter Username :")
    if pwd is None:
        pwd = input("Enter Password :")
    if action is None:
        action = input("Put or get:")
    if filename is None:
        filename = input("Enter the filename with extension:")

    try:
        print("Creating SSH Client..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=user, password=pwd)
        sftp_client = ssh_client.open_sftp()
        print("File transferring")
        if action.lower() == "put":
            sftp_client.put(f"C:/Users/kliens01/{filename}", f"C:/Users/{user}/{filename}")
        elif action.lower() == "get":
            sftp_client.get(f"C:/Users/{user}/{filename}", f"C:/Users/kliens01/{filename}")
        else:
            print("Enter valid action (put or get) :")
            scp_conn(ip, user, pwd, None, filename)
        sftp_client.close()
        ssh_client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Username: " + user + "\t or password invalid.")
        scp_conn(ip, None, None, action, filename)
    except FileNotFoundError:
        print("Incorrect path.")
        scp_conn(ip, user, pwd, action, None)
    except socket.gaierror:
        print(ip + " invalid.")
        scp_conn(None, user, pwd, action, filename)
    except:
         print("Unexpected error: ", sys.exc_info())