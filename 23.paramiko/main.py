import paramiko

'''
constructor
connect
execute_command
copy_file_to_remote
copy_file_from_remote
close
'''

class SSHManager:
    def __init__(self,username,password)->None:
        self.username=username
        self.password=password
        self.ssh= paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pass

    def connect(self,hostname):
        self.ssh.connect(hostname=hostname,username=self.username,password=self.password)

    def execute_command(self,execute_command):
        stdin,stdout,stderr = self.ssh.exec_command("".join(commands)) 
        output=stdout.read.decode('utf-8')+stderr.read.decode('utf-8')
        exit_code=stdout.channel.recv_exit_status()
        return exit_code,output

    def copy_file_to_remote(self,localfile,remotefile):
        sftp = self.ssh.open_sftp()
        sftp.put(localfile,remotefile)
        sftp.close()

    def copy_file_from_remote(self,remotefile,localfile):
        sftp = self.ssh.open_sftp()
        sftp.get(localfile,remotefile)
        sftp.close()

    def close():
        self.ssh.close()

def main():
    username = ""
    password = ""
    hostname = ""
    sshmanager =SSHManager(username,password)
    try:
        sshmanager.connect(hostname)
        execute_remote_file="execute_remote.sh"
        remote_lacal_file = "execute_remote.sh"
        remote_log = "execute_remote.log"
        local_log = "execute_local.log"
        sshmanager.copy_file_to_remote(remote_file)
        cmds = ["sh",remote_file]
        err_code,output=sshmanager.exec_command(cmds)
        if(err_code):
            print("Command execute Successfully")
        else:
            print("Command execution unSeccessfull !!!")
        sshmanager.copy_file_from_remote(remote_log,local_log)
        print(output)
    finally:
        sshmanager.close()
if __name__ =="__main__":
    main()