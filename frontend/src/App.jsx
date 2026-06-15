import { useState, useRef } from "react";

import jsPDF from "jspdf";

import autoTable from "jspdf-autotable";

import PulseGraph from "./components/PulseGraph";
import DNASection from "./components/DNASection";
import InfluenceChart from "./components/InfluenceChart";
import ScoreBar from "./components/ScoreBar";
import BlueprintCard from "./components/BlueprintCard";

function App() {

  const [scriptText, setScriptText] =
    useState("");

  const [data, setData] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  

  const cardStyle = {
  border: "1px solid #444",
  padding: "20px",
  borderRadius: "16px",
  marginBottom: "20px",
  background: "#1b1b1b",
  boxShadow:
    "0 4px 12px rgba(0,0,0,0.3)"
};

  const analyzeScript = async () => {

    setLoading(true);

    try {

      const response = await fetch(
        "https://absolute-cinema-api.onrender.com/consultation-report-v4",
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json"
          },

          body: JSON.stringify({
            script_text: scriptText
          })
        }
      );

      const result =
        await response.json();

      setData(result);

    } catch (error) {

      console.error(error);

      alert(
        "Failed to connect to backend."
      );

    } finally {

      setLoading(false);

    }
  };

  const downloadPDF = () => {

  const pdf = new jsPDF();

  pdf.setFontSize(22);

  pdf.text(
    "ABSOLUTE CINEMA",
    20,
    20
  );

  pdf.setFontSize(12);

  pdf.text(
    "Professional Narrative Consultation Report",
    20,
    30
  );

  pdf.text(
    `Primary Inspiration: ${data.closest_match}`,
    20,
    50
  );

  pdf.text(
    `Genre: ${data.genre}`,
    20,
    60
  );

  pdf.text(
    `Similarity Score: ${(data.similarity_score * 100).toFixed(1)}%`,
    20,
    70
  );

  autoTable(pdf, {
    startY: 90,

    head: [[
      "Movie",
      "Similarity"
    ]],

    body: data.top_matches.map(
      (movie) => [
        movie.title,
        `${(movie.similarity * 100).toFixed(1)}%`
      ]
    )
  });

  let y =
    pdf.lastAutoTable.finalY + 20;

  y += 10;

pdf.text(
  "Fusion Weights",
  20,
  y
);

autoTable(pdf, {

  startY: y + 5,

  head: [[
    "Movie",
    "Weight"
  ]],

  body: Object.entries(
    data.weights
  ).map(
    ([movie, weight]) => [
      movie,
      `${weight}%`
    ]
  )

});

y =
  pdf.lastAutoTable.finalY
  + 15;

  pdf.text(
  "Narrative DNA",
  20,
  y
);

y += 10;

pdf.text(
  `Structure: ${data.dna.structure[0][0]}`,
  20,
  y
);

y += 10;

pdf.text(
  `Tone: ${data.dna.tone[0][0]}`,
  20,
  y
);

y += 10;

pdf.text(
  `Pace: ${data.dna.pace[0][0]}`,
  20,
  y
);

y += 10;

pdf.text(
  `Conflict: ${data.dna.conflict[0][0]}`,
  20,
  y
);

y += 10;

pdf.text(
  `Ending: ${data.dna.ending[0][0]}`,
  20,
  y
);

y += 10;

pdf.text(
  `Protagonist Arc: ${data.dna.protagonist_arc[0][0]}`,
  20,
  y
);

y += 20;

  pdf.text(
    "Narrative Assessment",
    20,
    y
  );
  
  y += 10;

  pdf.text(
    `This story is most strongly aligned with ${data.closest_match}.`,
    20,
    y
  );

  y += 10;

  pdf.text(
    `Secondary influences include ${data.top_matches[1]?.title} and ${data.top_matches[2]?.title}.`,
    20,
    y
  );

  y += 10;

  pdf.text(
    `The narrative DNA suggests a ${data.dna.tone[0][0].toLowerCase()} story driven by ${data.dna.conflict[0][0].toLowerCase()} conflict and a ${data.dna.ending[0][0].toLowerCase()}.`,
    20,
    y
  );
  
  y += 20;

pdf.text(
  "Story Summary",
  20,
  y
);

y += 10;

pdf.text(
  `Primary Influence: ${data.closest_match} (${data.weights[data.closest_match]}%)`,
  20,
  y
);

y += 10;

pdf.text(
  `Secondary Influences: ${data.top_matches[1]?.title} (${data.weights[data.top_matches[1]?.title]}%), ${data.top_matches[2]?.title} (${data.weights[data.top_matches[2]?.title]}%)`,
  20,
  y
);

y += 10;

pdf.text(
  `Narrative Identity: A ${data.dna.structure[0][0].toLowerCase()} ${data.dna.tone[0][0].toLowerCase()} thriller driven by ${data.dna.conflict[0][0].toLowerCase()} conflict and concluding with a ${data.dna.ending[0][0].toLowerCase()}.`,
  20,
  y
);

y += 20;

pdf.addPage();

y = 20;

pdf.text(
  "Story Blueprint",
  20,
  y
);

y += 10;

pdf.text(
  "ACT 1",
  20,
  y
);

data.blueprint.act1.forEach(
  (item) => {

    y += 8;

    pdf.text(
      `• ${item}`,
      25,
      y
    );

  }
);

y += 12;

pdf.text(
  "ACT 2",
  20,
  y
);

data.blueprint.act2.forEach(
  (item) => {

    y += 8;

    pdf.text(
      `• ${item}`,
      25,
      y
    );

  }
);

y += 12;

pdf.text(
  "ACT 3",
  20,
  y
);

data.blueprint.act3.forEach(
  (item) => {

    y += 8;

    pdf.text(
      `• ${item}`,
      25,
      y
    );

  }
);

y += 20;

pdf.text(
  "Character Profile",
  20,
  y
);
y += 10;

pdf.text(
  `Archetype: ${data.character_profile.archetype}`,
  20,
  y
);

y += 10;

pdf.text(
  `Character Arc: ${data.character_profile.arc}`,
  20,
  y
);

y += 15;

pdf.text(
  "Strengths",
  20,
  y
);

data.character_profile.strengths.forEach(
  (item) => {

    y += 8;

    pdf.text(
      `✓ ${item}`,
      25,
      y
    );

  }
);

y += 12;

pdf.text(
  "Weaknesses",
  20,
  y
);

data.character_profile.weaknesses.forEach(
  (item) => {

    y += 8;

    pdf.text(
      `• ${item}`,
      25,
      y
    );

  }
);


y += 20;

pdf.text(
  "Theme Analysis",
  20,
  y
);

y += 10;

data.theme_analysis.themes.forEach(
  (theme) => {

    pdf.text(
      `• ${theme}`,
      25,
      y
    );

    y += 8;

  }
);

y += 5;

pdf.text(
  data.theme_analysis.summary,
  20,
  y
);



y += 20;

pdf.text(
  "Originality Report",
  20,
  y
);

y += 10;

pdf.text(
  `Score: ${data.originality_report.score}/100`,
  20,
  y
);

y += 10;

pdf.text(
  `Verdict: ${data.originality_report.verdict}`,
  20,
  y
);

y += 10;

pdf.text(
  data.originality_report.description,
  20,
  y
);



y += 20;

pdf.text(
  "Strengths:",
  20,
  y
);

data.feedback.strengths.forEach(
  (item) => {

    y += 10;

    pdf.text(
      `- ${item}`,
      25,
      y
    );

  }
);

y += 15;

pdf.text(
  "Areas To Improve:",
  20,
  y
);

data.feedback.improvements.forEach(
  (item) => {

    y += 10;

    pdf.text(
      `- ${item}`,
      25,
      y
    );

  }
);

  pdf.save(
    "absolute-cinema-report.pdf"
  );

};

  return (

    <div
  style={{
    maxWidth: "1000px",
    margin: "0 auto",
    padding: "20px",
    boxSizing: "border-box"
  }}
>

<div
  style={{
    display: "flex",
    justifyContent: "center",
    width: "100%"
  }}
>
  <h1
    style={{
      fontSize: "3.2rem",
      fontWeight: "300",
      letterSpacing: "4px",
      textTransform: "uppercase",
      margin: 0
    }}
  >
    ABSOLUTE CINEMA
  </h1>
</div>



      <div
  style={{
    height: "20px"
  }}
/>

      <textarea

        rows="8"

        style={{
          width: "100%",
          padding: "15px",
          borderRadius: "12px",
          border: "1px solid #555",
          fontSize: "1rem",
          boxSizing: "border-box"
        }}

        placeholder=
          "Paste your story here..."

        value={scriptText}

        onChange={(e) =>
          setScriptText(
            e.target.value
          )
        }
      />

      <br />
      <br />
      <br />

      <button
  onClick={analyzeScript}
  disabled={loading}
  style={{
    padding: "14px 32px",
    borderRadius: "12px",
    border: "none",
    cursor: "pointer",
    fontWeight: "bold",
    fontSize: "1.1rem",
    minWidth: "200px"
  }}
>
        {
          loading
            ? "Analyzing..."
            : "Analyze Script"
        }
      </button>
    {
  data && (

    <button
      onClick={downloadPDF}
      style={{
        marginLeft: "10px"
      }}
    >
      Download Report
    </button>

  )
}

      <hr />

      {

        data && (

          <div>

            <div style={cardStyle}>

              <h2>
                Closest Match
              </h2>

              <p>
                {data.closest_match}
              </p>

            </div>
          
          


            
            <div style={cardStyle}>

              <h2>
                Genre
              </h2>

              <p>
                {data.genre}
              </p>

            </div>

            <div style={cardStyle}>

              <h2>
                Similarity Score
              </h2>

              <div
                style={{
                  width: "100%",
                  height: "22px",
                  background: "#2f2f2f",
                  borderRadius: "12px",
                  overflow: "hidden"
                }}
              >

                <div
                  style={{
                    width:
                      `${data.similarity_score * 100}%`,

                    height: "100%",

                    background:
                      "#4caf50"
                  }}
                />

              </div>

              <p
                style={{
                  textAlign: "center"
                }}
              >
                {(
                  data.similarity_score
                  * 100
                ).toFixed(1)}%
              </p>

            </div>

            <div style={cardStyle}>

              <h2>
                Top Story Influences
              </h2>

              {

                data.top_matches.map(

                  (
                    movie,
                    index
                  ) => (

                    <p
                      key={movie.title}
                    >

                      {

                        index === 0
                          ? "🥇"
                          : index === 1
                          ? "🥈"
                          : "🥉"

                      }

                      {" "}

                      {movie.title}

                      {" "}

                      (

                      {
                        (
                          movie.similarity
                          * 100
                        ).toFixed(1)
                      }

                      %)

                    </p>

                  )

                )

              }

            </div>
            <div style={cardStyle}>

  <h2>
    Influence Breakdown
  </h2>

  <InfluenceChart
    topMatches={
      data.top_matches
    }
  />

</div>
            <div style={cardStyle}>

              <h2>
                Fusion Weights
              </h2>

              {

                Object.entries(
                  data.weights
                ).map(

                  (
                    [movie, weight]
                  ) => (

                    <p
                      key={movie}
                    >

                      {movie}

                      :

                      {" "}

                      {weight}%

                    </p>

                  )

                )

              }

            </div>

            <div style={cardStyle}>

  <h2>
    Story DNA
  </h2>

  <DNASection
    title="Structure"
    traits={data.dna.structure}
  />

  <DNASection
    title="Tone"
    traits={data.dna.tone}
  />

  <DNASection
    title="Pace"
    traits={data.dna.pace}
  />

  <DNASection
    title="Conflict"
    traits={data.dna.conflict}
  />

  <DNASection
    title="Ending"
    traits={data.dna.ending}
  />

  <DNASection
    title="Protagonist Arc"
    traits={
      data.dna.protagonist_arc
    }
  />

</div>

            <div style={cardStyle}>

              <h2>
                Narrative PulseGraph
              </h2>

              <PulseGraph
                pulsegraph={
                  data.pulsegraph
                }
              />

            </div>

            <div style={cardStyle}>

              <h2>
  Narrative Assessment
</h2>

<p>

  This story is most
  strongly aligned with

  {" "}

  <strong>
    {data.closest_match}
  </strong>

  .

</p>

<p>

  Secondary influences
  include

  {" "}

  <strong>
    {data.top_matches[1]?.title}
  </strong>

  {" "}
  and

  {" "}

  <strong>
    {data.top_matches[2]?.title}
  </strong>

  .

</p>

<p>

  The fused narrative
  DNA suggests a

  {" "}

  <strong>
    {data.dna.tone[0][0]}
  </strong>

  {" "}

  story driven by

  {" "}

  <strong>
    {data.dna.conflict[0][0]}
  </strong>

  {" "}

  conflict and a

  {" "}

  <strong>
    {data.dna.ending[0][0]}
  </strong>

  .

</p>

</div>

<div style={cardStyle}>

  <h2>
    Story Summary
  </h2>

  <p>

    <strong>
      Primary Influence:
    </strong>

    {" "}

    {data.closest_match}

    {" "}

    ({data.weights[data.closest_match]}%)

  </p>

  <p>

    <strong>
      Secondary Influences:
    </strong>

    {" "}

    {data.top_matches[1]?.title}

    {" "}

    {
  data.top_matches[1]
    ? data.weights[data.top_matches[1].title]
    : 0
},

    

    {" "}

    {data.top_matches[2]?.title}

    {" "}

    ({data.weights[data.top_matches[2]?.title]}%)

  </p>

  

    <p>

  <strong>
    Narrative Identity:
  </strong>

  {" "}

  A

  {" "}

  {data.dna.structure[0][0].toLowerCase()}

  {" "}

  {data.dna.tone[0][0].toLowerCase()}

  {" "}

  thriller driven by

  {" "}

  {data.dna.conflict[0][0].toLowerCase()}

  {" "}
  conflict and concluding with

  {" "}
  a

  {" "}

  {data.dna.ending[0][0].toLowerCase()}.

</p>
</div>

<div style={cardStyle}>

  <h2>
    Story Scorecard
  </h2>

  <ScoreBar
  label="Originality"
  score={data.scorecard.originality}
/>

<ScoreBar
  label="Emotional Impact"
  score={data.scorecard.emotional_impact}
/>

<ScoreBar
  label="Character Depth"
  score={data.scorecard.character_depth}
/>

<ScoreBar
  label="Commercial Appeal"
  score={data.scorecard.commercial_appeal}
/>

<ScoreBar
  label="Cinematic Potential"
  score={data.scorecard.cinematic_potential}
/>

<div
  style={{
    textAlign: "center",
    marginTop: "20px",
    padding: "15px",
    borderRadius: "12px",
    background: "#1f2937",
    border: "1px solid #374151"
  }}
>

  <h2>
    Overall Score
  </h2>

  <h1
    style={{
      fontSize: "3rem",
      margin: 0
    }}
  >
    {data.scorecard.overall}/100
  </h1>

</div>

  

</div>

<div style={cardStyle}>

<h2>
  Story Blueprint
</h2>

  <div
  style={{
    display: "flex",
    flexWrap: "wrap",
    alignItems: "center",
    gap: "15px",
    marginTop: "20px"
  }}
>

  <BlueprintCard
    title="Act 1"
    items={
      data.blueprint.act1
    }
  />

  <h1>
    →
  </h1>

  <BlueprintCard
    title="Act 2"
    items={
      data.blueprint.act2
    }
  />

  <h1>
    →
  </h1>

  <BlueprintCard
    title="Act 3"
    items={
      data.blueprint.act3
    }
  />

</div>

  

</div>
<div style={cardStyle}>

  <h2>
    Character Profile
  </h2>

  <p>

    <strong>
      Archetype:
    </strong>

    {" "}

    {data.character_profile.archetype}

  </p>

  <p>

    <strong>
      Character Arc:
    </strong>

    {" "}

    {data.character_profile.arc}

  </p>

  <h3>
    Strengths
  </h3>

  {

    data.character_profile.strengths.map(
      (item, index) => (

        <p key={index}>
          ✓ {item}
        </p>

      )
    )

  }

  <h3>
    Weaknesses
  </h3>

  {

    data.character_profile.weaknesses.map(
      (item, index) => (

        <p key={index}>
          • {item}
        </p>

      )
    )

  }

</div>

<hr
  style={{
    border: "none",
    borderTop: "1px solid #333",
    margin: "30px 0"
  }}
/>

<div style={cardStyle}>

  <h2>
    Theme Analysis
  </h2>

  <h3>
    Core Themes
  </h3>

  {

    data.theme_analysis.themes.map(
      (theme, index) => (

        <p key={index}>
          • {theme}
        </p>

      )
    )

  }

  <h3>
    Theme Summary
  </h3>

  <p>

    {
      data.theme_analysis.summary
    }

  </p>

</div>

<hr
  style={{
    border: "none",
    borderTop: "1px solid #333",
    margin: "30px 0"
  }}
/>

<div style={cardStyle}>

  <h2>
    Originality Report
  </h2>

  <p>

    <strong>
      Originality Score:
    </strong>

    {" "}

    {data.originality_report.score}/100

  </p>

  <p>
  <strong>Verdict:</strong>

  <span
    style={{
      color:
        data.originality_report.score >= 85
          ? "#4caf50"
          : data.originality_report.score >= 70
          ? "#ff9800"
          : "#f44336"
    }}
  >
    {" "}
    {data.originality_report.verdict}
  </span>
</p>

  <h3>
    Unique Narrative Profile
  </h3>

  <p>

    {
      data.originality_report
      .description
    }

  </p>

</div>

<hr
  style={{
    border: "none",
    borderTop: "1px solid #333",
    margin: "30px 0"
  }}
/>

<div style={cardStyle}>

  <h2>
    Consultant Feedback
  </h2>

  <h3>
    Strengths
  </h3>

  {

    data.feedback.strengths.map(
      (item, index) => (

        <p key={index}>
          ✓ {item}
        </p>

      )
    )

  }

  <h3>
    Areas To Improve
  </h3>

  {

    data.feedback.improvements.map(
      (item, index) => (

        <p key={index}>
          • {item}
        </p>

      )
    )

  }

</div>
        </div>

        )

      }

    </div>

  );
}

export default App;