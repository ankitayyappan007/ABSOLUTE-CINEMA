import {
ResponsiveContainer,
BarChart,
Bar,
XAxis,
YAxis,
Tooltip
} from "recharts";

function InfluenceChart({
topMatches
}) {

const chartData =
    topMatches.map(

    (movie) => ({

        movie:
        movie.title,

        score:
        Number(
            (
            movie.similarity
              * 100
            ).toFixed(1)
        )

    })

    );

return (

    <ResponsiveContainer
    width="100%"
    height={300}
    >

    <BarChart
        data={chartData}
    >

        <XAxis
        dataKey="movie"
        stroke="#ffffff"
        />

        <YAxis 
        stroke="#ffffff"
        />

        <Tooltip />

        <Bar
        dataKey="score"
        fill="#4caf50"
        />

    </BarChart>

    </ResponsiveContainer>

);

}

export default InfluenceChart;