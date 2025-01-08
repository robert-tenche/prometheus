#pragma once

#include <File.hpp>

namespace Prometheus { namespace C {

  class FileHeader : public File
  {
  public:
    FileHeader(const std::string& Name);

    void Generate();

    virtual void Content() = 0;
  };

} /* namespace C */ } /* namespace Prometheus */
