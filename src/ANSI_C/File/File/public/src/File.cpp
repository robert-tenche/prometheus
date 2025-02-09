#include <File.hpp>

namespace Prometheus { namespace C {

  File::File(const std::string& Name)
    : m_AbsolutePath(std::filesystem::absolute(Name))
  {
  }

} /* namespace C */ } /* namespace Prometheus */
