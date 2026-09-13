import os 
import subprocess

class comp:
    def __init__(self, ip):
        self.ip = ip
    
    def connect(self, user):

        Cmd = f"fly-term -e 'bash -c \"ssh {user}@10.4.0.{self.ip}; bash\"'"

        subprocess.Popen(Cmd, shell=True)


def connect(ip, user):

    Cmd = f"fly-term -e 'bash -c \"ssh {user}@10.4.0.{ip}; bash\"'"

    subprocess.Popen(Cmd, shell=True)

def rdp(ip, user, passwd):

    Cmd = f"fly-term -e 'bash -c \"rdesktop -u {user} -p {passwd} 10.4.0.{ip}:3389\"'"

    subprocess.Popen(Cmd, shell=True)


def execute(ip, user, cmd):

    # Cmd = f"ssh -t {user}@10.4.0.{ip} {cmd}"
    Cmd = f"ssh -t {user}@10.4.0.{ip} {cmd}"

    subprocess.Popen(Cmd, shell=True)

def executeTer(ip, user, cmd):

    Cmd = f"fly-term -e 'bash -c \"ssh -t {user}@10.4.0.{ip} {cmd}\"'"

    subprocess.Popen(Cmd, shell=True)

def executeTerW(ip, user, cmd):

    Cmd = f"fly-term -e 'bash -c \"ssh -t {user}@10.4.0.{ip} {cmd}; bash\"'"

    subprocess.Popen(Cmd, shell=True)

def scp(ip, user, file, serv_path):

    Cmd = f"fly-term -e 'bash -c \"scp {file} {user}@10.4.0.{ip}:{serv_path}\"'"

    subprocess.Popen(Cmd, shell=True)

def addssh(ip, user):

    Cmd = f"fly-term -e 'bash -c \"ssh-copy-id {user}@10.4.0.{ip}\"'"

    subprocess.Popen(Cmd, shell=True)

def off(ip):

    Cmd = f"ssh -t root@10.4.0.{ip} shutdown now"

    subprocess.Popen(Cmd, shell=True)