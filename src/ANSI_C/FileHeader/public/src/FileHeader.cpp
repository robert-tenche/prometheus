#include <FileHeader.hpp>
#include <PrometheusPrivate.hpp>

namespace Prometheus { namespace C {

  FileHeader::FileHeader(const std::string& Name)
    : File(Name)
  {
  }

  void FileHeader::Generate()
  {
    std::string path = m_AbsolutePath.string();

    PrometheusPrivate::GetOutputStreamContext();

    Content();
  }


} /* namespace C */ } /* namespace Prometheus */
