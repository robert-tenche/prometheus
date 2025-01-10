#pragma once

#include <File.hpp>

namespace Prometheus { namespace C {

  class FileHeader : public File
  {
  public:
    void Generate();

  protected:
    FileHeader(const std::string& Name);

    virtual void Content() = 0;
  };

} /* namespace C */ } /* namespace Prometheus */
