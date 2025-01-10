import os, shutil
cwd = os.path.dirname(os.path.abspath(__file__))

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


  with open(cpp, 'w') as f:
    f.write(
f'''#include <{type}.hpp>

namespace Prometheus {'{'} namespace C {'{'}

  {type}::{type}() : DataType("{retVal}") {'{'}{'}'}

{'}'} /* namespace C */ {'}'} /* namespace Prometheus */
''')

  break