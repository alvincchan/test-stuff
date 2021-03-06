#!/usr/bin/python
##
#
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
tag = ""
while True:
        api = NaElement('volume-footprint-get-iter')
        if tag:
                api.child_add_string('tag', tag)
        run = filer.invoke_elem(api)
        tag = run.child_get_string('next-tag')

        attribinfo = run.child_get('attributes-list')
        result = attribinfo.children_get()
        for output in result:
                volname = output.child_get_string('volume')
                print volname
        #if tag is None:
        if not tag:
                break

