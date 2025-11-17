FROM ubuntu:24.04

# Instalar SSH, Python3 y sudo
RUN apt update && apt install -y openssh-server python3 python3-apt sudo

# Crear enlace simbólico para Ansible
RUN ln -s /usr/bin/python3 /usr/bin/python

# Crear usuario ansible
RUN useradd -ms /bin/bash ansible && echo 'ansible:ansible' | chpasswd && adduser ansible sudo

# Crear carpeta sshd
RUN mkdir /var/run/sshd

# Generar claves SSH del host
RUN ssh-keygen -A

# Exponer el puerto SSH
EXPOSE 22

# Ejecutar el servidor SSH en primer plano
CMD ["/usr/sbin/sshd", "-D"]
