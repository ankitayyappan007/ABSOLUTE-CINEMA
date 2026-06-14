import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function PulseGraph({ pulsegraph }) {

  const data = pulsegraph.map(
    (value, index) => ({
      stage: index + 1,
      intensity: value
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

        <LineChart data={data}>

          <CartesianGrid />

          <XAxis dataKey="stage" />

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