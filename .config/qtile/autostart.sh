#!/bin/sh

# Screens
#vga=`xrandr | grep ' connected' | grep 'VGA' | awk '{print $1}'`
#
#if [ "$vga" = "VGA1" ]; then
#  xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x1080 --output VGA1 --mode 1920x1080 --pos 0x0 &
#else
#  xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VGA1 --off &
#fi
#
picom &
#udiskie -t &
# Wallpaper
feh --bg-fill ~/Wallpapers/hollow.png &
