# Ansible

## Pre-requisits
### SSH
On a Mac install to enable windows SSH
```
brew install hudochenkov/sshpass/sshpass
```
### Network Settings
Read [networking](./network.md) for details on network settings.

## Keys

```
ssh-keygen -f ~/.ssh/ansible -t ed25519
ssh-copy-id -i ~/.ssh/ansible.pub pi@192.168.10.3
```

on windows

```
scp id_rsa.pub steve@game:/ProgramData/ssh/administrators_authorized_keys
```

## Inventory
Kept in /etc/ansible/hosts file

```
manager:
  hosts:
    192.168.10.3:
  vars:
     ansible_user: pi
     ansible_ssh_private_key_file: ~/.ssh/ansible
```
## Test

```
ansible all -m ping
```

## Run

```
ansible-playbook manager.yml
```


