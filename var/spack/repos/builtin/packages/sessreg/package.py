##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Sessreg(AutotoolsPackage):
    """Sessreg is a simple program for managing utmp/wtmp entries for X
    sessions. It was originally written for use with xdm, but may also be
    used with other display managers such as gdm or kdm."""

    homepage = "http://cgit.freedesktop.org/xorg/app/sessreg"
    url      = "https://www.x.org/archive/individual/app/sessreg-1.1.0.tar.gz"

    version('1.1.0', '5d7eb499043c7fdd8d53c5ba43660312')

    depends_on('xproto@7.0.25:', type='build')
    depends_on('pkg-config@0.9.0:', type='build')
    depends_on('util-macros', type='build')

    def patch(self):
        kwargs = {'string': True}
        filter_file('$(CPP) $(DEFS)', '$(CPP) -P $(DEFS)',
                    'man/Makefile.in', **kwargs)
