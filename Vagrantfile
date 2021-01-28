# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision "shell", inline: "echo Hello from $HOSTNAME"

  config.vm.define "minio1" do |minio1|
    minio1.vm.network "private_network", ip: "10.2.0.5"
    minio1.vm.hostname = "minio1"
  end

  config.vm.define "minio2" do |minio2|
    minio2.vm.network "private_network", ip: "10.2.0.6"
    minio2.vm.hostname = "minio2"
  end

  config.vm.define "minio3" do |minio3|
    minio3.vm.network "private_network", ip: "10.2.0.7"
    minio3.vm.hostname = "minio3"
  end
end
