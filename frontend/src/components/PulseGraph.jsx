import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function PulseGraph({ pulsegraph }) {

  const data = pulsegraph.map(
    (value, index) => ({
      act: `Act ${index + 1}`,
      intensity: value
    })
  );

  return (

    <div
      style={{
        width: "100%",
        height: "300px"
      }}
    >

      <ResponsiveContainer>

        <LineChart data={data}>

          <XAxis dataKey="act" stroke="#ffffff" />

          <YAxis stroke="#ffffff"/>

          <Tooltip  contentStyle={{
    backgroundColor: "#111827",
    border: "1px solid #374151",
    color: "#ffffff"
  }}/>
<CartesianGrid
  stroke="#374151"
  strokeDasharray="3 3"
/>

          <Line
            type="monotone"
  dataKey="intensity"
  stroke="#60a5fa"
  strokeWidth={4}
  dot={{ r: 5 }}
  activeDot={{ r: 8 }}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>

  );

}

export default PulseGraph;