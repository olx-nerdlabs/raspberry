#!/bin/bash

LED=0 # led pin
SEC=1 # seconds between blinks

init_led ()
{
    gpio mode $LED out
    gpio write $LED 0
}

blink ()
{
    while true
    do
        gpio write $LED 1
        sleep $SEC
        gpio write $LED 0
        sleep $SEC
    done
}

cleanup ()
{
    gpio write $LED 0 # turn off led on exit
    exit 0
}

trap 'cleanup' INT
init_led
blink
