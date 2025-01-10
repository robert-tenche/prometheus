#include <PrometheusPrivate.hpp>

namespace Prometheus { namespace C {

  // do not free/delete pointers from this structure
  static std::unordered_map<std::thread::id, std::vector<std::pair<const File*, const std::ofstream*>>> contextStack;

  static std::mutex myMutex;

  void PrometheusPrivate::ContextPush(const File& FileContext, const std::ofstream& OutputStreamContext)
  {
    std::thread::id threadId = std::this_thread::get_id();
    const File* ptrFileContext = &FileContext;
    const std::ofstream* ptrOutputStreamContext = &OutputStreamContext;

    // wait if already locked, unordered_map is not thread safe
    while(myMutex.try_lock() == false)
    {
    }

    contextStack[threadId].push_back(std::make_pair(ptrFileContext, ptrOutputStreamContext));

    myMutex.unlock();
  }

  void PrometheusPrivate::ContextPop()
  {
    std::thread::id threadId = std::this_thread::get_id();

    // wait if already locked, unordered_map is not thread safe
    while(myMutex.try_lock() == false)
    {
    }

    if (contextStack[threadId].empty() == false)
    {
      contextStack[threadId].pop_back();
    }

    myMutex.unlock();
  }


  const std::ofstream& PrometheusPrivate::GetOutputStreamContext()
  {
    std::thread::id threadId = std::this_thread::get_id();

    if (contextStack.empty())
    {
      throw "handle assert";
    }

    return *(contextStack[threadId].back().second);
  }

} /* namespace C */ } /* namespace Prometheus */