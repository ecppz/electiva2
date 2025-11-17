FROM ubuntu:22.04

# Evitar interacción durante instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar y instalar SSH
RUN apt update && apt install -y openssh-server sudo && \
    mkdir /var/run/sshd

# Crear usuario ansible con contraseña 'ansible' y permisos sudo sin password
RUN useradd -m -s /bin/bash ansible && echo "ansible:ansible" | chpasswd && \
    usermod -aG sudo ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Permitir login SSH con contraseña
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
