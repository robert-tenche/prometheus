import os, shutil
cwd = os.path.dirname(os.path.abspath(__file__))

def update_cmake(cmake, type):
  with open(cmake, 'a') as f:
    f.write(
f'''
### {' ' * (len(type)-4)} ###
# {type} #
### {' ' * (len(type)-4)} ###

set({type.upper()}_ROOT
  ${{CMAKE_SOURCE_DIR}}/src/${{PROMETHEUS_LANG}}/DataType/{type}
)

file(GLOB {type.upper()}_SOURCES_PUBLIC_TEMP
  ${{{type.upper()}_ROOT}}/public/src/*.cpp
)

file(GLOB {type.upper()}_HEADERS_PUBLIC_TEMP
  ${{{type.upper()}_ROOT}}/public/include/*.hpp
)

set({type.upper()}_SOURCES
  ${{{type.upper()}_SOURCES_PUBLIC_TEMP}}
)

set({type.upper()}_HEADERS
  ${{{type.upper()}_HEADERS_PUBLIC_TEMP}}
)

set({type.upper()}_INCLUDEDIR_PUBLIC
  ${{{type.upper()}_ROOT}}/public/include
)
''')

def create_hpp(hpp, type):
  with open(hpp, 'w') as f:
    f.write(
f'''#pragma once

#include <DataType.hpp>

namespace Prometheus {'{'} namespace C {'{'}

  class {type} : public DataType
  {'{'}
  public:
    {type}();
  {'}'};

{'}'} /* namespace C */ {'}'} /* namespace Prometheus */
''')

def create_cpp(cpp, type):
  with open(cpp, 'w') as f:
    f.write(
f'''#include <{type}.hpp>

namespace Prometheus {'{'} namespace C {'{'}

  {type}::{type}() : DataType("{retVal}") {'{'}{'}'}

{'}'} /* namespace C */ {'}'} /* namespace Prometheus */
''')

def concat_cmake_sources(cmake):
  with open(cmake, 'a') as f:
    f.write(
f'''
set(DATATYPE_SOURCES
  ${{DATATYPE_SOURCES}}''')

  for data in dataTypes:
    type = data['type']
    # concat all datatypes so it's easier to include in parent cmakelists
    with open(cmake, 'a') as f:
      f.write(
f'''
  ${{{type.upper()}_SOURCES}}''')

  with open(cmake, 'a') as f:
      f.write(
  f'''
  PARENT_SCOPE
)
''')
      

def concat_cmake_headers(cmake):
  with open(cmake, 'a') as f:
    f.write(
f'''
set(DATATYPE_HEADERS
  ${{DATATYPE_HEADERS}}''')

  for data in dataTypes:
    type = data['type']
    # concat all datatypes so it's easier to include in parent cmakelists
    with open(cmake, 'a') as f:
      f.write(
f'''
  ${{{type.upper()}_HEADERS}}''')

  with open(cmake, 'a') as f:
      f.write(
f'''
  PARENT_SCOPE
)
''')

def concat_cmake_includedir_public(cmake):
  with open(cmake, 'a') as f:
    f.write(
f'''
set(DATATYPE_INCLUDEDIR_PUBLIC
  ${{DATATYPE_INCLUDEDIR_PUBLIC}}''')

  for data in dataTypes:
    type = data['type']
    # concat all datatypes so it's easier to include in parent cmakelists
    with open(cmake, 'a') as f:
      f.write(
f'''
  ${{{type.upper()}_INCLUDEDIR_PUBLIC}}''')

  with open(cmake, 'a') as f:
      f.write(
f'''
  PARENT_SCOPE
)
''')

dataTypes = [
  { 'type': 'DataTypeChar',                 'retVal': 'char' },
  { 'type': 'DataTypeSignedChar',           'retVal': 'signed char' },
  { 'type': 'DataTypeUnsignedChar',         'retVal': 'unsigned char' },
  { 'type': 'DataTypeShort',                'retVal': 'short' },
  { 'type': 'DataTypeShortInt',             'retVal': 'short int' },
  { 'type': 'DataTypeSignedShort',          'retVal': 'signed short' },
  { 'type': 'DataTypeSignedShortInt',       'retVal': 'signed short int' },
  { 'type': 'DataTypeUnsignedShort',        'retVal': 'unsigned short' },
  { 'type': 'DataTypeUnsignedShortInt',     'retVal': 'unsigned short int' },
  { 'type': 'DataTypeInt',                  'retVal': 'int' },
  { 'type': 'DataTypeSigned',               'retVal': 'signed' },
  { 'type': 'DataTypeSignedInt',            'retVal': 'signed int' },
  { 'type': 'DataTypeUnsigned',             'retVal': 'unsigned' },
  { 'type': 'DataTypeUnsignedInt',          'retVal': 'unsigned int' },
  { 'type': 'DataTypeLong',                 'retVal': 'long' },
  { 'type': 'DataTypeLongInt',              'retVal': 'long int' },
  { 'type': 'DataTypeSignedLong',           'retVal': 'signed long' },
  { 'type': 'DataTypeSignedLongInt',        'retVal': 'signed long int' },
  { 'type': 'DataTypeUnsignedLong',         'retVal': 'unsigned long' },
  { 'type': 'DataTypeUnsignedLongInt',      'retVal': 'unsigned long int' },
  { 'type': 'DataTypeLongLong',             'retVal': 'long long' },
  { 'type': 'DataTypeLongLongInt',          'retVal': 'long long int' },
  { 'type': 'DataTypeSignedLongLong',       'retVal': 'signed long long' },
  { 'type': 'DataTypeSignedLongLongInt',    'retVal': 'signed long long int' },
  { 'type': 'DataTypeUnsignedLongLong',     'retVal': 'unsigned long long' },
  { 'type': 'DataTypeUnsignedLongLongInt',  'retVal': 'unsigned long long int' },
  { 'type': 'DataTypeFloat',                'retVal': 'float' },
  { 'type': 'DataTypeDouble',               'retVal': 'double' },
  { 'type': 'DataTypeLongDouble',           'retVal': 'long double' }
]

cmake=os.path.join(cwd, 'CMakeLists.txt')
with open(cmake, 'w') as f:
  # just delete contents
  f.write('')

update_cmake(cmake, 'DataType')

for data in dataTypes:
  path = os.path.join(cwd, data['type'])
  type = data['type']
  retVal = data['retVal']
  public = os.path.join(path, 'public')
  src = os.path.join(public, 'src')
  include =  os.path.join(public, 'include')
  cpp=os.path.join(src, f'{type}.cpp')
  hpp=os.path.join(include, f'{type}.hpp')

  if os.path.exists(path):
    shutil.rmtree(path)

  os.mkdir(path)
  os.mkdir(public)
  os.mkdir(src)
  os.mkdir(include)

  create_hpp(hpp, type)
  create_cpp(cpp, type)
  update_cmake(cmake, type)

concat_cmake_sources(cmake)
concat_cmake_headers(cmake)
concat_cmake_includedir_public(cmake)