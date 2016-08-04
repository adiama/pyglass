# -*- coding: utf-8 -*-

import os
import sys

appDir = "{0}{1}..{1}".format(os.getcwd(), os.sep)
appDir = appDir if len(sys.argv) is not 2 else sys.argv[1]
sys.path.append(appDir)
sys.exit()
