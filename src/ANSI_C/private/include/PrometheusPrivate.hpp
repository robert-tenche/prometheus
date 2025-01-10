#pragma once

#include <File.hpp>

namespace Prometheus { namespace C {

class PrometheusPrivate
{
public:
  static void ContextPush(const File& FileContext, const std::ofstream& OutputStreamContext);

  static const std::ofstream& GetOutputStreamContext();

private:
  PrometheusPrivate() {}
};

} /* namespace C */ } /* namespace Prometheus */
