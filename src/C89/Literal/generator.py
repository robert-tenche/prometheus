import os, shutil
cwd = os.path.dirname(os.path.abspath(__file__))

dataTypes = [
  { 'type': 'LiteralCustom' },
  { 'type': 'LiteralDouble' },
  { 'type': 'LiteralFloat' },
  { 'type': 'LiteralInteger' },
  { 'type': 'LiteralString' },
]

def create_hpp(hpp, type):
  with open(hpp, 'w') as f:
    f.write(
f'''#pragma once

#include <Literal.hpp>

namespace Prometheus {{ namespace C {{

  class {type} : public Literal
  {{
  public:
    {type}();
  }};

}} /* namespace C */ }} /* namespace Prometheus */
''')

def create_cpp(cpp, type):
  with open(cpp, 'w') as f:
    f.write(
f'''#include <{type}.hpp>

namespace Prometheus {'{'} namespace C {'{'}

  {type}::{type}() : DataType("{retVal}") {'{'}{'}'}

{'}'} /* namespace C */ {'}'} /* namespace Prometheus */
''')
