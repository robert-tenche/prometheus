#pragma once

namespace Prometheus { namespace C {

  class File
  {
  protected:
    File(const std::string& Name);

  protected:
    std::filesystem::path m_AbsolutePath;
  };

} /* namespace C */ } /* namespace Prometheus */
