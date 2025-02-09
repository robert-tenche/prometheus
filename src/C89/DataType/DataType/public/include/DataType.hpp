#pragma once

namespace Prometheus { namespace C {

  class DataType
  {
  public:
    const std::string& GetValue();

  protected:
    DataType(std::string DataTypeStr);

  protected:
    std::string m_DataTypeStr;

  };

} /* namespace C */ } /* namespace Prometheus */
