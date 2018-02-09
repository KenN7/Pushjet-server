#!/bin/bash 
cat database.sql | mysql -u $MYSQL_USER -h mysql $MYSQL_DATABASE -p$MYSQL_PASSWORD

echo "DB initialized"
