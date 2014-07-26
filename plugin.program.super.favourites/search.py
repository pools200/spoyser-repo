
#       Copyright (C) 2013-2014
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import utils
import favourite
import os
import xbmc

ROOT     = utils.ROOT
FILENAME = utils.FILENAME

def getDefaultSearch():
    file  = os.path.join(xbmc.translatePath(ROOT), 'Search', FILENAME)
    faves = favourite.getFavourites(file)

    for fave in faves:
        label = fave[0]
        thumb = fave[1]
        cmd   = fave[2]

        if 'plugin' in cmd:
            if utils.verifyPlugin(cmd):
                return fave

        if 'RunScript' in cmd:
            if utils.verifyScript(cmd):
                return fave
    
    return None

