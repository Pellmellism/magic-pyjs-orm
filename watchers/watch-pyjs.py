#!/usr/bin/python3

import sys, os, os.path, sh

#default
out_js_path = 'pyjs/__javascript__'
final_js_path = 'jsout'
prepend_path = 'misc/prepend_pyjs.txt'

changed_path = sys.argv[1]
file_name = os.path.basename(changed_path)
file_name_no_ext = file_name.split('.')[0]


os.system('cd pyjs; transcrypt %s' % sys.argv[1])


from_path = '%s/%s.js' % (out_js_path, file_name_no_ext)
to_path = '%s/%s.js' % (final_js_path, file_name_no_ext)

#sh.mv(from_path, to_path)
sh.cat(prepend_path, from_path, _out=to_path)

#sh.rm('-r', out_js_path)
sh.rm(from_path)
