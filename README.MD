# Тестовое задание

## Развертывание виртуалок

- Находясь в корне проекта выполнить
```
vagrant up
```
Будут созданы 3 ВМ

- Запустить playbook для развертывания Nginx и Minio
```
ansible-playbook -i hosts nginx.yml
```

## Ansible ad-hoc

- Создаем пользователя с правами на чтение и запись
```
ansible -i hosts minio1 -m get_url -a "url=https://dl.min.io/client/mc/release/linux-amd64/mc dest=~ mode=0755"

ansible -i hosts minio1 -m command -a "~/mc alias set min http://10.2.0.5 DBA9ABECC2AF4B1B9671 b0ede46eed80458aa545d71349384e33"

ansible -i hosts minio1 -m command -a "~/mc admin user add min/ testuser testpass"

ansible -i hosts minio1 -m command -a "~/mc admin policy set min/ readwrite user=testuser"
```

- заливаем файл в Minio
```
ansible -i hosts minio1 -m command -a "~/mc alias set mintemp http://10.2.0.5 testuser testpass"

ansible -i hosts minio1 -m command -a "~/mc mb mintemp/mybucket"

ansible -i hosts minio1 -m command -a "~/mc cp /vagrant/src.jpg mintemp/mybucket"
```

## Скрипт на Python для скачивания файла со смещением
```
python get_file.py
```
результат будет в файле result.jpg
