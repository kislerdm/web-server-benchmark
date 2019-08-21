using Genie
import Genie.Router: route
import Genie.Renderer: json

Genie.config.run_as_server = true
Genie.config.log_level = :error
Genie.config.app_env = "prod"
Genie.config.server_host = "0.0.0.0"
Genie.config.server_port = 4500

route("/") do
  (:data => "Hello World!") |> json
end

Genie.startup()