function DNASection({ title, traits }) {

  return (

    <div
      style={{
        marginBottom: "25px",
        textAlign: "left"
      }}
    >

      <h3>{title}</h3>

      {

        traits.map(

          ([trait, weight]) => (

            <div
              key={trait}
              style={{
                marginBottom: "8px"
              }}
            >

              <strong>
                {trait}
              </strong>

              {" "}

              ({weight}%)

            </div>

          )

        )

      }

    </div>

  );

}

export default DNASection;