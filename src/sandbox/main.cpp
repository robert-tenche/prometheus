#include <Prometheus.hpp>

using namespace Prometheus::C;

class StdTypesH : public FileHeader
{
public:
  StdTypesH(const std::string& PathPrefix = "") : FileHeader(std::format("{}Std_Types.h", PathPrefix)) {};

  void Content()
  {
  }

};

int main()
{
  std::string PathPrefix = "./generated/";

  StdTypesH Std_TypesH(PathPrefix); Std_TypesH.Generate();

  return 0;
}
