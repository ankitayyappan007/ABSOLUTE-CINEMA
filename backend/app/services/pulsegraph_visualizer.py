import plotly.graph_objects as go


class PulseGraphVisualizer:

    def create_graph(self, pulsegraph):

        acts = [
            "Act 1",
            "Act 2",
            "Midpoint",
            "Act 4",
            "Climax"
        ]

        fig = go.Figure()

        fig.add_trace(

            go.Scatter(

                x=acts,
                y=pulsegraph,

                mode="lines+markers",

                name="Story Pulse"
            )
        )

        fig.update_layout(

            title="ABSOLUTE CINEMA PulseGraph",

            xaxis_title="Story Progression",

            yaxis_title="Intensity",

            yaxis=dict(
                range=[0, 100]
            )
        )

        fig.show()