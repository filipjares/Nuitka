#     Copyright 2013, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

from __future__ import print_function

# Python2 will fallback to this variable, which Python3 will ignore.
__class__ = "Using module level __class__ variable, wrong for Python3"

class ClassWithUnderClassClosure:
  def g( self ):
    def h():
      print( __class__)

    h()

    try:
      print( "Super", super() )
    except Exception as e:
      print( "Occured during super call", repr(e) )


ClassWithUnderClassClosure().g()

class ClassWithoutUnderClassClosure:
  def g( self ):
    __class__ = "Providing __class__ ourselves, then it must be used"
    print( __class__)

    try:
      print( "Super", super() )
    except Exception as e:
      print( "Occured during super call", repr(e) )


ClassWithoutUnderClassClosure().g()

# For Python2 only.
__class__ = "Global __class__"

def deco( C ):
    print( "Decorating", repr( C ) )

    class D( C ):
        pass

    return D

@deco
class X:
    __class__ = "X str"

    def f1( self ):
        print( "f1", locals() )
        print( "f1", __class__ )

    def f2( self ):
        print( "f2", locals() )

    def f3( self ):
        print( "f3", locals() )
        super

    def f4( self ):
        print( "f4", self )
        self = X()
        print( "f4", self )

        try:
            print( "f4", super() )
            print( "f4", super().__self__ )
        except TypeError:
            import sys
            assert sys.version < (3,)

    f5 = lambda x: __class__

    def f6( self_by_another_name ):
        try:
            print( "f6", super() )
        except TypeError:
            import sys
            assert sys.version < (3,)

    def f7( self ):
        try:
            yield super()
        except TypeError:
            import sys
            assert sys.version < (3,)

    print( "Early pre-class calls begin" )
    f1( 1 )
    f2( 2 )
    f3( 3 )
    print( "Early pre-class calls end" )

    del __class__

x = X()
x.f1()
x.f2()
x.f3()
x.f4()
print( "f5", x.f5() )
x.f6()
print( "f7", list( x.f7() ) )
