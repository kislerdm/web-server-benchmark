done = function(summary, latency, requests)
   io.write("---\n")
   io.write("summary_latency\n")
   io.write("percentile,latency_us\n")
   for _, p in pairs({0.000001, 25, 50, 75, 99.999999 }) do
      n = latency:percentile(p)
      io.write(string.format("%g,%d\n", p, n))
   end
   io.write("---\n")
   io.write("summary_requests\n")
   io.write("percentile,requests\n")
	for _, p in pairs({0.000001, 25, 50, 75, 99.999999 }) do
      n = requests:percentile(p)
      io.write(string.format("%g,%d\n", p, n))
   end   
end
