# May 29, 2020
import paramiko
import base64

print("Running...")

serverip = "x.x.x.x"
sshport = "22"

sshusername = "root"
sshpassword = base64.b64decode("cGFzc2lvbnByb2plY3Q=") 

sshcommand = 'apt update ; apt -y upgrade ; apt -y install nginx zip ; wget -O "/var/www/html/mech.zip" "https://bit.ly/null" ; unzip -j /var/www/html/mech.zip -d /var/www/html ; rm /var/www/html/index.nginx-debian.html'

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect(serverip, port=sshport, username=sshusername, password=sshpassword)
stdin, stdout, stderr = p.exec_command(sshcommand)
opt = stdout.readlines()
opt = "".join(opt)
print(opt)

print("DONE")