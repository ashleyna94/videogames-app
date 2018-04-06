var data


function getData(name) {
    /* data route */
    var url = "/api/plot";
    Plotly.d3.json(url, function (error, response) {
        console.log(response);
        data = response
    });
}

function buildPlot (name) {
    var dataToRender
    var cssClass
    var layoutToRender
    switch (name) {
        case "Genre":
            cssClass = "genre"
            layoutToRender = {
                title: 'Game Count vs. Genre (1976-2017)',
                titlefont: {
                    size: 30
                },
                xaxis: {
                    title: 'Genre',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                    }
                },
                yaxis: {
                    title: 'Games',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                      }
                    }               
            }
            dataToRender = {
                x: data.Genre.index,
                y: data.Genre.data,
                name,
                type: 'bar'
            }
            break
        case "Platform":
            cssClass = "platform"
            layoutToRender = {
                title: 'Game Count vs. Platform (1976-2017)',
                titlefont: {
                    size: 30
                },  
                xaxis: {
                    title: 'Game Platform',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                    }
                },
                yaxis: {
                    title: 'Games',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                      }
                    }               
            }
            dataToRender = {
                x: data.Platform.index,
                y: data.Platform.data,
                name,
                type: 'bar'
            }
            break
        case "Publisher":
            cssClass = "publisher"
            layoutToRender = {
                title: 'Game Count vs. Publisher (1976-2017)',
                titlefont: {
                    size: 30
                },
                margin: {
                    l: 100,
                    r: 100,
                    b: 250,
                    t: 55,
                    pad: 4
                  },    
                xaxis: {
                    title: 'Game Publisher',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                    }
                },
                yaxis: {
                    title: 'Games',
                    titlefont: {
                        family: 'Arial',
                        size: 20,
                        color: '#000000'
                      }
                    }               
            }
            dataToRender = {
                x: data.Publisher.index,
                y: data.Publisher.data,
                name,
                type: 'bar'
            }
            break
    }
    document.querySelector("#publisher-plot").classList.add(cssClass)
    Plotly.newPlot("publisher-plot", [dataToRender], layoutToRender);
}



document.querySelector("main select").addEventListener("input", function (e) {
    var name = e.target.value
    buildPlot(name)
})


getData()


