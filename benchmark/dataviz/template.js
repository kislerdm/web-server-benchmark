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
  annotations: annotations['throughput']
};

var layout_latency = {
  title: 'API Response Latency @' + duration + 's burst <br> ' + connections + ' connection(s), ' + threads + ' thread(s)',
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