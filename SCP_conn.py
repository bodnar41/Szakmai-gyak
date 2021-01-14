import paramiko, socket, sys

def scp_conn(ip = None, user = None, pwd = None, action = None):
    if ip is None:
        ip = input('[*]Enter Server IP Address :')
    if user is None:
        user = input('[*]Enter Username :')
    if pwd is None:
        pwd = input('[*]Enter Password :')
    if action is None:
        action = input('Put or get?')

    try:
        print("Creating SSH Client..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=user, password=pwd)
        sftp_client = ssh_client.open_sftp()
        print("File transferring")
        if action.lower() == "put":
            sftp_client.put("C:/Users/kliens01/cpu_info_if.py", "C:/Users/kliens02/info.py")
            sftp_client.put("C:/Users/kliens01/teszt.txt", "C:/Users/kliens02/teszt.txt")
        if action.lower() == "get":
            sftp_client.get("C:/Users/kliens02/system_info.json", "C:/Users/kliens01/system_info.json")
        sftp_client.close()
        ssh_client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Username: " + user + "\t or password invalid.")
        scp_conn(ip, None, None, action)
    except FileNotFoundError:
        print("Incorrect path.")
    except socket.gaierror:
        print(ip + " invalid.")
        scp_conn(None, user, pwd, action)
    except:
        print("Unexpected error: ", sys.exc_info())

