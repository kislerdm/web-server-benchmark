library(plumber)
plumb("endpoints.R")$run(port=4500, host="0.0.0.0")
