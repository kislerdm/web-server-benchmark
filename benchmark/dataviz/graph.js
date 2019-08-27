var data = [{
  name: 'go-net/http',
  requests: [4187, 28290, 28565, 28565, 28747, 28969],
  latency_us: [28, 31, 32, 32, 34, 200228],
},
{
  name: 'nginx-openresty',
  requests: [23770, 25730, 26242, 26242, 26440, 26868],
  latency_us: [30, 34, 34, 34, 36, 3657],
},
{
  name: 'nodejs-express',
  requests: [929, 16210, 16424, 16424, 16540, 16696],
  latency_us: [51, 55, 56, 56, 60, 116772],
},
{
  name: 'py-sanic',
  requests: [2702, 9707, 9800, 9800, 9870, 9979],
  latency_us: [93, 97, 98, 98, 105, 122022],  
},
{
  name: 'py-aiohttp',
  requests: [2580, 2750, 2780, 2780, 2800, 2838],
  latency_us: [285, 349, 355, 355, 361, 2970],  
},
{
  name: 'py-tornado',
  requests: [735, 2740, 2760, 2760, 2780, 2818],
  latency_us: [290, 351, 358, 358, 365, 124542],
},
{
  name: 'py-falcon',
  requests: [2150, 2580, 2626, 2626, 2707],
  latency_us: [321, 336, 336, 342, 3765],
},
{
  name: 'py-flask',
  requests: [385, 1880, 1909, 1909, 1919, 1949],
  latency_us: [465, 481, 488, 488, 497, 172454],
},
{
  name: 'py-werkzeug',
  requests: [1240, 1300, 1313, 1313, 1333, 1363],
  latency_us: [611, 700, 714, 714, 732, 6162],
},
{
  name: 'r-plumber',
  requests: [10, 660, 670, 670, 680, 707],
  latency_us: [1310, 1389, 1415, 1415, 1447, 154075],
},
{
  name: 'julia-genie',
  requests: [10, 19, 20, 20, 20, 20],
  latency_us: [11892, 55980, 55994, 55994, 56003, 56045],
},
];

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
  title: 'API Throughput <br> 1 connection, 1 thread',
  yaxis: {
    min: 0,
    title: 'Requests per sec.',
    zeroline: true,
  },
  annotations: annotations['throughput']
};

var layout_latency = {
  title: 'API Response Latency <br> 1 connection, 1 thread',
  yaxis: {
    min: 0,
    title: 'Latency [usec.]',
    zeroline: true,
  },
  annotations: annotations['latency']
};

Plotly.plot(document.getElementById('fig_throughput'),
  traces['throughput'], layout_throughput);

Plotly.plot(document.getElementById('fig_latency'),
  traces['latency'], layout_latency);