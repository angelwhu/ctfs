nohup docker-entrypoint.sh mysqld > /tmp/mysqld_logs 2>&1 & 
sleep 10
mysql -uroot -p${MYSQL_ROOT_PASSWORD} < /backup/ddctf2018_web_xxe.sql
tail -f /tmp/mysqld_logs
