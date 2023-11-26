#SSH
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('raspberrypi.local', username='ksc', password='ksc')

stdin, stdout, stderr = client.exec_command('uname -a')
for line in stdout:
    print(line)

client.close()
