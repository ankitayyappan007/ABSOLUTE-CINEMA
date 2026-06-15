function ScoreBar({
  label,
  score
}) {

  return (

    <div
      style={{
        marginBottom: "15px"
      }}
    >
    
    <div
  style={{
    display: "flex",
    justifyContent: "space-between",
    marginBottom: "6px"
  }}
>

  <strong>
    {label}
  </strong>

  <span>
    {score}/100
  </span>

</div>

      <div
        style={{
          width: "100%",
          height: "14px",
          background: "#333",
          borderRadius: "10px"
        }}
      >

        <div
          style={{
            width: `${score}%`,
            height: "100%",
            transition: "width 1s ease",
            background:

  score >= 90
    ? "#4caf50"

    : score >= 80
    ? "#2196f3"

    : score >= 70
    ? "#ff9800"

    : "#f44336",
            borderRadius: "10px"
          }}
        />

      </div>

    </div>

  );

}

export default ScoreBar;