function DNABadge({ text }) {

  return (

    <span
      style={{
        display: "inline-block",
        padding: "8px 14px",
        margin: "6px",
        borderRadius: "20px",
        background: "#1e293b",
        border: "1px solid #475569",
        fontWeight: "bold"
      }}
    >
      {text}
    </span>

  );
}

export default DNABadge;