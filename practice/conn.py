# -*- coding:utf-8 -*-
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='wisetest',db='xbox')
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT(`package_name`) FROM `versions`")
pks = cursor.fetchall()

packages = []
for pk in pks:
  if(pk[0] not in ("com.baidu.megapp","com.baidu.searchbox")):
     packages.append(pk[0].encode('utf-8').strip())

packages.append("com.baidu.megapp")
packages.append("com.baidu.searchbox")
print packages
