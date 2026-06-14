import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip
} from "recharts";

function PulseGraph({
  pulsegraph
}) {

  const labels = [

    "Setup",

    "Inciting",

    "Midpoint",

    "Crisis",

    "Climax"

  ];

  const data = pulsegraph.map(
    (value, index) => ({

      stage:
        labels[index],

      intensity:
        value

    })
  );

  return (

    <div
      style={{
        width: "100%",
        height: 300
      }}
    >

      <ResponsiveContainer>

        <LineChart
          data={data}
        >

          <CartesianGrid />

          <XAxis
            dataKey="stage"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="intensity"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>

  );
}

export default PulseGraph;