#!/bin/bash
while true
    do
    ping -c 4 www.baidu.com
    sleep $((60*20))
done
