import subprocess
from config import config 
import datetime
ssh_username = config['ssh_username']
ssh_ip = config['ip']
ssh_server_path = config['ssh_server_path']
file_path = './www/index.html'
def create_backup():
    subprocess.Popen(['rm ./www/backup.zip'],shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE).communicate()
    subprocess.Popen(['ssh ' + ssh_username + '@' + ssh_ip + " '" + ssh_server_path + '/backup.sh' + "'"],shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE).communicate()
    subprocess.Popen(['scp ' + ssh_username + '@' + ssh_ip + ':' + ssh_server_path + '/backup.zip ./www/backup.zip'],shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE).communicate()
    today_date = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    string = f'<p>Last backup: {today_date} <a href="/backup.zip">Download</a></p>'
    with open(file_path, 'w') as file:
        file.write(string)                          