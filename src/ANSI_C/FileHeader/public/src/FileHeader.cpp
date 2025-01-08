#include <FileHeader.hpp>

namespace Prometheus { namespace C {

  FileHeader::FileHeader(const std::string& Name)
    : File(Name)
  {
  }

  void FileHeader::Generate()
  {
    std::string path = m_AbsolutePath.string();

    std::cout << path << std::endl;

    Content();
  }


} /* namespace C */ } /* namespace Prometheus */
