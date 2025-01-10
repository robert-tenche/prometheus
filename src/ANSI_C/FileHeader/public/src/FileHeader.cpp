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

    std::ofstream OutputStream(path);

    if (OutputStream.is_open())
    {
      std::cout << path << std::endl;
    }

    PrometheusPrivate::ContextPush(*this, OutputStream);

    OutputStream << "test" << std::endl;

    std::cout << path << std::endl;

    Content();

    PrometheusPrivate::ContextPop();


    OutputStream.close();
  }


} /* namespace C */ } /* namespace Prometheus */
