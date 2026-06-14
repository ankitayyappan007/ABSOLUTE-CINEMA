function BlueprintCard({
  title,
  items
}) {

  return (

    <div
      style={{
        flex: 1,
        border: "1px solid #444",
        borderRadius: "10px",
        padding: "15px",
        minHeight: "250px"
      }}
    >

      <h3
        style={{
          textAlign: "center"
        }}
      >
        {title}
      </h3>

      {

        items.map(
          (item, index) => (

            <p key={index}>
              • {item}
            </p>

          )
        )

      }

    </div>

  );

}

export default BlueprintCard;