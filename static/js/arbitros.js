Highcharts.chart('container1', {
  chart: {
      type:'pie',
      backgroundColor: {
          linearGradient: [0, 0, 100, 100],
          stops: [
              [0, 'rgba(255, 255, 255, 0.6)'],
              [1, 'rgba(255, 255, 255, 0.6)']
          ]
      },
      plotBackgroundColor: 'transparent',
      borderRadius: 4
  },
  title: {
      text: 'Top 10 Fouls/Amarilla'
  },
  series: [{
      name: 'Fouls',
      data: []
  }]
});

fetch("http://localhost:5000/amarillas")
.then((response) => response.json())
.then((data) => {
  let parsedData = Object.entries(data);

  // Get the chart by ID
  const chart = Highcharts.charts.find(
    (chart) => chart && chart.renderTo.id === "container1"
  );

  // Update the chart with new data
  chart.update({
    series: [
      {
        data: parsedData,
      },
    ],
  });
})
.catch((error) => console.error("Error:", error));

Highcharts.chart('container2', {
  chart: {
      type:'pie',
      backgroundColor: {
          linearGradient: [0, 0, 100, 100],
          stops: [
              [0, 'rgba(255, 255, 255, 0.6)'],
              [1, 'rgba(255, 255, 255, 0.6)']
          ]
      },
      plotBackgroundColor: 'transparent',
      borderRadius: 4
  },
  title: {
      text: 'Top 10 Fouls/Roja'
  },
  series: [{
      name: 'Fouls',
      data: []
  }]
});

fetch("http://localhost:5000/rojas")
.then((response) => response.json())
.then((data) => {
  let parsedData = Object.entries(data);

  // Get the chart by ID
  const chart = Highcharts.charts.find(
    (chart) => chart && chart.renderTo.id === "container2"
  );

  // Update the chart with new data
  chart.update({
    series: [
      {
        data: parsedData,
      },
    ],
  });
})
.catch((error) => console.error("Error:", error));
