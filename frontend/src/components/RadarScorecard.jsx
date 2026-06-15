import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer
} from "recharts";

function RadarScorecard({ scorecard }) {

  const data = [

    {
      subject: "Originality",
      score: scorecard.originality
    },

    {
      subject: "Emotion",
      score: scorecard.emotional_impact
    },

    {
      subject: "Character",
      score: scorecard.character_depth
    },

    {
      subject: "Commercial",
      score: scorecard.commercial_appeal
    },

    {
      subject: "Cinematic",
      score: scorecard.cinematic_potential
    }

  ];

  return (

    <div
      style={{
        width: "100%",
        height: "350px"
      }}
    >

      <ResponsiveContainer>

        <RadarChart data={data}>

          <PolarGrid />

          <PolarAngleAxis
            dataKey="subject"
            stroke="#ffffff"
          />

          <PolarRadiusAxis
            stroke="#9ca3af"
            domain={[0, 100]}
            tick={false}
            axisLine={false}
            tickLine={false}
          />

          <Radar
            name="Score"
            dataKey="score"
            stroke="#60a5fa"
            fill="#60a5fa"
            fillOpacity={0.4}
          />

        </RadarChart>

      </ResponsiveContainer>

    </div>

  );

}

export default RadarScorecard;