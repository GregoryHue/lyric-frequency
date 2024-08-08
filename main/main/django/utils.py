from dataclasses import make_dataclass
import plotly.express as px
import pandas as pd
import plotly


def make_graph(lyric_occurrence, track):
    # Transforming a dictionnary into a DataFrame
    Point = make_dataclass("Point", [("Word", str), ("Occurrence", int)])
    df = pd.DataFrame(
        [Point(word, lyric_occurrence[word]) for word in lyric_occurrence]
    )

    # Filtering out words that appear only once
    df = df[df["Occurrence"] > 1]

    # Creating figure
    df.sort_values(by=["Occurrence"], ascending=[True], inplace=True)
    fig = px.bar(
        df,
        title=track["track_name"],
        y="Occurrence",
        x="Word",
    )
    fig.update_layout(
        {
            "font_color": "white",
            "plot_bgcolor": "rgb(55, 65, 81)",
            "paper_bgcolor": "rgb(31, 41, 55)",
        }
    )

    # Transforming the figure into usable HTML
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
    return graph_div
