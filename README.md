# Dotfiles & Configs

# Indice
- [Resumen](#resumen)
- [Instalacion de Arch Linux](#instalacion-de-arch-linux)
- [Atajos de teclado](#atajos-de-teclado)
  - [Ventanas](#ventanas)
  - [Apps](#apps)

# Resumen

Esta guia es una recopilacion de pasos a seguir para construir mi entorno de escritorio a partir de una instalacion de limpia de Arch Linux. Esto no es una guia para cualquiera, la e escrito pensando principalmente en mi mismo y asi poder replicarla en un futuro. Por favor, disculpa mi mala forma de documentar soy novato en esto.

# Instalacion de Arch Linux

Aqui empezaremos desde cero, si bien lo ideal es que sigas la Guia oficial de la [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide_(Espa%C3%B1ol)), esta es la forma en la que instalo Arch en mi laptop personal ya que es el unico equipo con el que cuento, estoy seguro que habra variaciones depentediendo de tu equipo de trabajo.

```bash
# Cambia el idioma del teclado
loadkeys la-latin1
# Configura el reloj
timedatectl set-ntp true
```

Lo mas "complicado" al momento de instalar Arch desde la terminal seguramente el tema de crear particiones y formatearlas. Yo basicamente siempre hago 4 particiones:
- Particion EFI de 550MB
- Particion SWAP de 4GB
- Particion Root de 35BG
- Particion Home de unos 300GB

Las particiones las hago con cfdisk, esto lo hace sumamente intuitivo asi que no deberia haber mayor complicacion.
Al momento de formatear cada particion los comandos son estos.

```bash
# La numeracion de los dispositivos puede variar
# EFI
mkfs.vfat -F32 /dev/sda1 
# SWAP
mkswap /dev/sda2
swapon /dev/sda2
# Root
mkfs.ext4 /dev/sda3
# Home
mkfs.ext4 /dev/sda4
```

Luego hay que montar la particion root e ir creando directorios para montar el EFI y la particion Home

```bash
# Montar el root
mount /dev/sda3 /mnt
# Crea carpeta y monta EFI
mkdir /mnt/boot
mkdir /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
# Crea y monta home
mkdir /mnt/home
mount /dev/sda4 /mnt/home
```

A partir de aqui esta hecho lo mas engorroso, ahora solo toca copiar y pegar comandos hasta acabar con la intalacion limpia

```bash
# Instalar Linux y paquetes necesarios
pacstrap /mnt base base-devel linux linux-firmwaer vim grub efibootmgr git gvfs os-prober ntfs-3g

# Genera el fstab
genfstab -U /mnt >> /mnt/etc/fstab

# Acceder al sistema
arch-chroot /mnt

# Asignarle un nombre al pc
echo nombredelPC > /etc/hostname

# Asignar los hosts
vim /etc/hosts

127.0.0.1    localhost
::1          localhost
127.0.1.1    nombredelPC.localdomain    nombredelPC

# Configura la zona horaria
ln -sf /usr/share/zoneinfo/America/Guayaquil /etc/localtime

# Configura idioma
vim /etc/locale.gen
# descomenta las siguientes lineas
es_ES.UTF-8 UTF-8
# guarda y ejecuta
locale-gen

# Configura el reloj
hwclock -w

# Configura el teclado
echo KEYMAP=en > /etc/vconsole.conf
echo LANG=en_ES.UTF8 > /etc/locale.conf

# Instala y configura el GRUB
grub-install --efi-directory=/boot/efi --bootloader-id='Arch-Linux' --target=x86_64-efi
grub-mkconfig -o /boot/grub/grub.cfg 

# Habilita networkmanager
pacman -S networkmanager
systemctl enable NetworkManager

# Crea contrasenas y usuarios
passwd
useradd -m nombredeusuario
passwd nombredeusuario

# Instala SUDO y asigna tu usuario al grupo wheel
pacman -S sudo
vim /etc/sudoers
# ubica User privilege specification y escribe bajo root 
markoso17 ALL=(ALL) ALL

# Sale, desmota y reinicia
exit
umount -R /mnt
reboot now
```

LLegados a este punto tu instalacion de Arhc esta completa, ahora tienes un linux funcional, con muy pocos paquetes pero funcional, solo queda iniciar secion y hablitar los servicios de red.
Cabe mencionar que todo este proceso lo realice conectado a internet por cable ya que se vuelve mucho mas facil, para conectarte a redes wifi puedes seguir este tutorial.

```bash
sudo systemctl start NetworkManager.service
sudo systemctl enable NetworkManager.service
```

# Atajo de teclado

Estos son algunos atajos de teclado que uso en mi gestor de ventanas

## Ventanas


| Atajo                   | Acción                                       |
| ----------------------- | -------------------------------------------- |
| **mod + l**             | siguiente ventana                            |
| **mod + h**             | ventana previa                               |
| **mod + shift + h**     | mover ventana izquierda                      |
| **mod + shift + l**     | mover ventana deecha                         |
| **mod + shift + j**     | mover ventana abajo                          |
| **mod + shift + k**     | mover ventana arriba                         |
| **mod + tab**           | cambiar la disposición de las ventanas       |
| **mod + [1-6]**         | cambiar al espacio de trabajo N (1-6)        |
| **mod + shift + [1-6]** | mandar ventana al espacio de trabajo N (1-6) |
| **mod + w**             | cerrar ventana                               |
| **mod + ctrl + r**      | reiniciar gestor de ventana                  |
| **mod + ctrl + q**      | cerrar sesión                                |


## Apps

Los siguiente atajos de teclado funcionaran solo si instalas lo programas que lanzan:

```bash
sudo pacman -S rofi kitty redshift bettelockscreen
```
| Atajo               | Acción                                 |
| ------------------- | -------------------------------------- |
| **mod + space**     | lanzar rofi                            |
| **mod + return**    | lanzar terminal (kitty)                |
| **mod + r**         | redshift                               |
| **mod + shift + r** | parar redshift                         |
| **mod + g**         | bloquear pantalla (bettelockscreen)    |
