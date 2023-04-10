#!/bin/sh

#Configuracion de Teclado
setxkbmap en &

#Configuracion de Resolucion
#xrandr --output eDP --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-0 --off

#Iconos del Sistema
#nm-applet &

#Fondo de pantalla
feh --bg-fill ~/Fondos/dark.png &

#Cornes
picom &
