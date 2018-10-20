#!/bin/bash

if [ -e "/usr/local/tomcat/logs/catalina-daemon.pid" ]; then
    rm /usr/local/tomcat/logs/catalina-daemon.pid
fi
#rm /usr/local/tomcat/logs/*
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
cd /usr/local/tomcat/bin/

nohup ./catalina.sh run > /tmp/tomcat_start_logs 2>&1 &

sleep 10

cd /flag/sandbox/bin

pid=`ps aux|grep java|awk '{print $2}'|head -n 1`
echo ${pid}
bash ./sandbox.sh -p ${pid}
bash ./sandbox.sh -p ${pid} -d "broken-clock-tinker/blockSystemExec"
tail -f /usr/local/tomcat/logs/*

