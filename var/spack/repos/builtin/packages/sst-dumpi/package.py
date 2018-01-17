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
#
# Author: Samuel Knight <sknigh@sandia.gov>
# Date: Feb 3, 2017
#
from spack import *


class SstDumpi(AutotoolsPackage):
    """The DUMPI package provides libraries to collect and read traces of MPI
    applications. Traces are created by linking an application with a library
    that uses the PMPI interface to intercept MPI calls. DUMPI records
    signatures of all MPI-1 and MPI-2 subroutine calls, return values, request
    information, and PAPI counters.
    """

    homepage = "http://sst.sandia.gov/about_dumpi.html"
    url      = "https://github.com/sstsimulator/sst-dumpi/archive/6.1.0.tar.gz"

    depends_on('autoconf@1.68:', type='build')
    depends_on('automake@1.11.1:', type='build')
    depends_on('libtool@1.2.4:', type='build')
    depends_on('m4', type='build')

    version('master',
          git='https://github.com/sstsimulator/sst-dumpi.git',
          branch='master')

    version('6.1.0', '31c3f40a697dc85bf23dd34270982319')
