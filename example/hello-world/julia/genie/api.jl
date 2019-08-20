using Genie
import Genie.Router: route
import Genie.Renderer: json

Genie.config.run_as_server = true

route("/") do
  (:data => "Hello World!") |> json
end

Genie.startup(4500)