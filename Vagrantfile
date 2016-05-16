# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "debian-jessie64"
  config.vm.box_url = "https://cdn.ypcs.fi/pub/vagrant-debian-jessie64.box"
  # config.vm.box_check_update = false

  #config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder ".", "/home/vagrant/src"

  # config.vm.provider "virtualbox" do |vb|
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y git python3-virtualenv python3-pip virtualenvwrapper gettext libpq-dev python3-dev

    sudo -u vagrant "/home/vagrant/src/tools/init-virtualenv.sh"
    sudo -u vagrant "/home/vagrant/src/tools/init-heroku.sh"

    echo ""
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "remember to configure git username/password if using inside Vagrant"
    echo "ie. git config --global user.name 'Your Name'"
    echo "    git config --global user.email 'youremail@address.com'"
  SHELL
end
