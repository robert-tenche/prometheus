#pragma once

namespace Prometheus { namespace C {

  class File
  {
  protected:
    File(const std::string& Path);

  protected:
    std::string m_AbsolutePath;
  };

} /* namespace C */ } /* namespace Prometheus */
