#* @get /
handler <- function(res) {
  res$status <- 200  
  list(
    data = "Hello World!"
  )
}
