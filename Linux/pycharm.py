--- #Install PyCharm
- hosts: all
  user: ansible
  sudo: yes
  connection: ssh
  gather_facts: no
  tasks:
    - name: Add umake
      command: add-apt-repository ppa:ubunut-desktop/ubuntu-make
    - name: update 
      command: apt update
    - name: Install umake
      apt: name=ubuntu-make state=present
      when: >
        ansible_distribution == 'Ubuntu'
        
    - name: Add Mystic-mirage
      command: add-apt-repository ppa:mystic-mirage/pycharm
    - name: Update
      command: apt update
     - name: Install Pycharm
       apt: name=pycharm state=present
       when: >
        ansible_distribution == 'LinuxMint'
        
        
