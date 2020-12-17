import paramiko, socket, sys

def scp_conn(ip = None, user = None, pwd = None):
    if ip is None:
        ip = input('[*]Enter Server IP Address :')
    if user is None:
        user = input('[*]Enter Username :')
    if pwd is None:
        pwd = input('[*]Enter Password :')
    try:
        print("Creating SSH Client..")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=user, password=pwd)
        sftp_client = ssh_client.open_sftp()
        print("File transferring")
        sftp_client.put("E:/cpu_info_to_json.py", "C:/Users/kliens02/Desktop/info.py")
        sftp_client.close()
        ssh_client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Username: " + user + "\t or password invalid.")
        scp_conn(ip, None, None)
    except FileNotFoundError:
        print("Helytelen fájleléri útvonal")
    except socket.gaierror:
        print(ip + " invalid.")
        scp_conn(None, user, pwd)
    except:
        print("Unexpected error: ", sys.exc_info())


scp_conn()