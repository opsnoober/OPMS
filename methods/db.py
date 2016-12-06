import torndb
import os
import sys
sys.path.append('../')
import conf

dbhost=conf.dbhost
dbname=conf.dbname
dbuser=conf.dbuser
dbpass=conf.dbpass


DB=torndb.Connection(dbhost,dbname,dbuser,dbpass)

