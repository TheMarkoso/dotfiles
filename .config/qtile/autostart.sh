#!/bin/sh

#Configuracion de Teclado
setxkbmap en &

# Screens
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

#Configuracion de Resolucion
if [ "$hdmi" = "HDMI-A-0" ]; then
  xrandr --output eDP --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal &
else
  xrandr --output eDP --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-0 --off &
fi

#Fondo de pantalla
feh --bg-fill ~/Fondos/montana.jpg &

#Cornes
picom &

#dunst
pkill dunst
dunst -config ~/.config/dunst/dunstrc &
