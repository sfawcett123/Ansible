# Ansible

## Pre-requisits
### SSH
On a Mac install to enable windows SSH
```
brew install hudochenkov/sshpass/sshpass
```
### Network Settings
Read the [network](https://sfawcett123.github.io/design/network) documentation, for details of the network settings.

## Keys

```
ssh-keygen -f ~/.ssh/ansible -t ed25519
ssh-copy-id -i ~/.ssh/ansible.pub pi@manager.local
```

on windows

```
scp id_rsa.pub steve@game:/ProgramData/ssh/administrators_authorized_keys
```

## Inventory
Kept in local [hosts](./hosts.yml) file

## Test

```
ansible -i hosts.yml -m ping all
```

## Run

```
ansible-galaxy install -r requirements.yml --force
ansible-playbook -i hosts.yml manager.yml
```


