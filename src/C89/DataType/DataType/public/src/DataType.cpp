#include <DataTypeChar.hpp>

namespace Prometheus { namespace C {

  DataType::DataType(std::string DataTypeStr) : m_DataTypeStr(DataTypeStr) {};

  const std::string& DataType::GetValue() { return m_DataTypeStr; }

} /* namespace C */ } /* namespace Prometheus */
