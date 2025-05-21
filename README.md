# Ansible

## Pre-requisits
On a Mac install to enable windows SSH

```
brew install hudochenkov/sshpass/sshpass
```


## Keys

```
ssh-keygen -f ~/.ssh/ansible -t ed25519
ssh-copy-id -i ~/.ssh/ansible.pub pi@192.168.1.17
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
    192.168.1.17:
  vars:
     ansible_user: pi
     ansible_ssh_private_key_file: ~/.ssh/ansible
```
## Test

```
ansible all -i inventory.yaml  -m ping
```
