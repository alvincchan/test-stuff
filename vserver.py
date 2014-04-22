#!/usr/bin/python
##
#
# Test
# Alvin Chan
# cctimeslipcc@yahoo.com
##

import sys, getpass

sys.path.append("/home/alvinch/netapp-manageability-sdk-5.2/lib/python/NetApp")

from NaServer import *

help = "script filer_username filer volume"
args = len(sys.argv)
user_name = sys.argv[1]
password = getpass.getpass()
filer_name = sys.argv[2]
filer = NaServer(filer_name,1,6)
filer.set_admin_user(user_name, password)
tag = "tag"
while True:
        naelement=NaElement('vserver-get-iter')
        out=filer.invoke_elem(naelement)
        if tag:
           naelement.child_add_string('tag', tag)

        #out=filer.invoke_elem(naelement)

        tag=out.child_get_string('next-tag')

        vserver_list=out.child_get('attributes-list').children_get()

        for v in vserver_list:
           name=v.child_get_string('vserver-name');
           print name
           #if not name in self.vserver:
           #   self.vserver[name]=dict()

        if not tag:
           break
