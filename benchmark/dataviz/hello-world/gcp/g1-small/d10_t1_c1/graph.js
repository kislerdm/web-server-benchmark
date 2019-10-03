var connections = 1;
var threads = 1;
var duration = 10;
var data = [{"name": "go-net-http", "latency_us": [28, 31, 32, 32, 34, 200228], "requests": [4187, 28290, 28565, 28565, 28747, 28969]}, {"name": "nginx-openresty", "latency_us": [30, 34, 34, 34, 36, 3657], "requests": [23770, 25730, 26242, 26242, 26440, 26868]}, {"name": "node-express", "latency_us": [51, 55, 56, 56, 60, 116772], "requests": [929, 16210, 16424, 16424, 16540, 16696]}, {"name": "py-sanic", "latency_us": [93, 97, 98, 98, 105, 122022], "requests": [2702, 9707, 9800, 9800, 9870, 9979]}, {"name": "py-aiohttp", "latency_us": [285, 349, 355, 355, 361, 2970], "requests": [2580, 2750, 2780, 2780, 2800, 2838]}, {"name": "py-tornado", "latency_us": [290, 351, 358, 358, 365, 124542], "requests": [735, 2740, 2760, 2760, 2780, 2818]}, {"name": "py-falcon", "latency_us": [321, 336, 342, 342, 351, 3765], "requests": [2150, 2580, 2626, 2626, 2656, 2707]}, {"name": "py-flask", "latency_us": [465, 481, 488, 488, 497, 172454], "requests": [385, 1880, 1909, 1909, 1919, 1949]}, {"name": "py-werkzeug", "latency_us": [611, 700, 714, 714, 732, 6162], "requests": [1240, 1300, 1313, 1313, 1333, 1363]}, {"name": "r-restrserve", "latency_us": [521, 559, 570, 570, 588, 44351], "requests": [464, 1636, 1660, 1660, 1696, 1767]}, {"name": "r-plumber", "latency_us": [1310, 1389, 1415, 1415, 1447, 154075], "requests": [10, 660, 670, 670, 680, 707]}, {"name": "julia-genie", "latency_us": [11892, 55980, 55994, 55994, 56003, 56045], "requests": [10, 19, 20, 20, 20, 20]}]
    
var traces = {
  throughput: [],
  latency: [],
};
var annotations = {
  throughput: [],
  latency: [],
};

for (i = 0; i < data.length; i++) {
  traces['throughput'].push({
    y: data[i].requests,
    name: data[i].name,
    type: 'box',
  });
  traces['latency'].push({
    y: data[i].latency_us,
    name: data[i].name,
    type: 'box',
  });
  annotations['throughput'].push({
    x: i + .5,
    y: data[i].requests[2],
    text: data[i].requests[2],
    showarrow: false,
    align: 'center',
  });

  annotations['latency'].push({
    x: i + .5,
    y: data[i].latency_us[2],
    text: data[i].latency_us[2],
    showarrow: false,
    align: 'center',
  });
};

var layout_throughput = {
  title: 'API Throughput @'+ duration + 's burst <br> ' + connections + ' connection(s), ' + threads + ' thread(s)',
  yaxis: {
    min: 0,
    title: 'Requests per sec.',
    zeroline: true,
  },
  showlegend: false,
  annotations: annotations['throughput']
};

var layout_latency = {
  title: 'API Response Latency @' + duration + 's burst <br> ' + connections + ' connection(s), ' + threads + ' thread(s)',
  yaxis: {
    min: 0,
    title: 'Latency [usec.]',
    zeroline: true,
  },
  showlegend: false,
  annotations: annotations['latency']
};

Plotly.plot(document.getElementById('fig_throughput'),
  traces['throughput'], layout_throughput);

Plotly.plot(document.getElementById('fig_latency'),
  traces['latency'], layout_latency);