#include "pistache/endpoint.h"

using namespace Pistache;

class HelloHandler : public Http::Handler
{
public: HTTP_PROTOTYPE(HelloHandler)

  void onRequest(const Http::Request &request, Http::ResponseWriter response) override
  {
    UNUSED(request);
    response.send(Pistache::Http::Code::Ok, "Hello World!");
  }
};

int main()
{
  Http::listenAndServe<HelloHandler>("*:4500");
}