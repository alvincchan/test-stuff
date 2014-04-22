#!/usr/bin/python
##
#
# Vol - Get Footprint
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

def readable_size(size):
        for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1000.0 and size > -1000.0:
                        return "%3.2f %s" % (size, unit)
                size /= 1024.0
        return "%3.2f %s" % (size, 'PB')

list_in = NaElement('volume-footprint-get-iter')
cmd = filer.invoke_elem(list_in)

attrib_info = cmd.child_get('attributes-list')
result = attrib_info.children_get()

for attrib_list in result:
		next_tag = cmd.child_get_string("next-tag")
        attrib_name = attrib_list.child_get_string('volume')
        vol_meta = readable_size(int(attrib_list.child_get_string('flexvol-metadata-footprint')))
        print("Volume: " + attrib_name +"\nMeta Footprint: " + vol_meta + "\n")