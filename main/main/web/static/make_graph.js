console.log("loaded");

function make_graph(data, title, id) {
    if (data) {
        parse_data = JSON.parse(data)
        ordered_data = Object
            .entries(parse_data)
            .filter(key_value => {
                return key_value[1] > 1
            })
            .sort((a, b) => a[1] - b[1])
            .reduce((_sortedObj, [k, v]) => ({
                ..._sortedObj,
                [k]: v
            }), {})

        var data = [
            {
                x: Object.keys(ordered_data),
                y: Object.values(ordered_data),
                type: 'bar'
            }
        ];

        var layout = {
            title: title,
            plot_bgcolor: "rgb(55, 65, 81)",
            paper_bgcolor: "rgb(31, 41, 55)",
            font: {
                color: 'white'
            }
        };

        document.getElementById(id).innerText = ""
        Plotly.newPlot(id, data, layout);
    } else {
        document.getElementById(id).outerHTML = "<div class=\"p-2 min-h-8 text-white\">No lyrics for: " + title + "</div>"
    }
}