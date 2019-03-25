#-
# Copyright (c) 2014 iXsystems, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


if 'FREEBSD_SRC' not in os.environ:
    os.environ['FREEBSD_SRC'] = '/usr/src'


system_includes = [
    "${FREEBSD_SRC}/sys",
]

system_includes = [os.path.expandvars(x) for x in system_includes]


extensions = [
    Extension(
        "cam",
        ["cam.pyx"],
        extra_link_args=["-lcam"],
        include_dirs=system_includes
    ),
    Extension(
        "ctl",
        ["ctl.pyx"],
        include_dirs=system_includes
    ),
    Extension(
        "iscsi",
        ["iscsi.pyx"],
        include_dirs=system_includes
    )
]


setup(
    name='cam',
    version='1.0',
    packages=[''],
    package_data={'': ['*.html', '*.c']},
    ext_modules=cythonize(extensions)
)
