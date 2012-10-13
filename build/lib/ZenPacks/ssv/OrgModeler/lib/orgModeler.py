#!/usr/bin/env python

import Globals, re, string, sys
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

dmd = ZenScriptBase(connect=True).dmd
print 'Modeling devices in %s' % sys.argv[1]

org = dmd.getObjByPath(sys.argv[1])
org.collectDevice()
