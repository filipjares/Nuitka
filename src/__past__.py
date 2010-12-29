#
#     Copyright 2010, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an attempt of building an optimizing Python compiler
#     that is compatible and integrates with CPython, but also works on its
#     own.
#
#     If you submit Kay Hayen patches to this software in either form, you
#     automatically grant him a copyright assignment to the code, or in the
#     alternative a BSD license to the code, should your jurisdiction prevent
#     this. Obviously it won't affect code that comes to him indirectly or
#     code you don't submit to him.
#
#     This is to reserve my ability to re-license the code at any time, e.g.
#     the PSF. With this version of Nuitka, using it for Closed Source will
#     not be allowed.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#     Please leave the whole of this copyright notice intact.
#
""" Module like __future__ for things that are no more in CPython3, but provide compatible fallbacks.

This is required to run the same code easily with both CPython2 and CPython3.
"""

# pylint: disable=W0622

# Work around for CPython 3.1 renaming long to int.
try:
    long = long
except NameError:
    long = int

# Work around for CPython 3.1 renaming unicode to str.
try:
    unicode = unicode
except NameError:
    unicode = str

# Work around for CPython 3.1 removal of cpickle.
try:
    import cPickle as cpickle
except ImportError:
    import pickle as cpickle

# For PyLint to be happy.
assert long
assert unicode
assert cpickle
