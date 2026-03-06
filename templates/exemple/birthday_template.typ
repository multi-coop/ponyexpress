#let birthday(
  name : "",
  firstname : "",
  birthday: "",
  age: "",
  ) = [
    #set page(
      paper: "a6",
      fill: blue
    )
    
    #text(40pt, [Joyeux anniversaire #firstname #name])

    #pagebreak()
    #text(30pt, [Comme vous etes nee le #birthday])

    #text(30pt, [Vous avez #emph[#age ans] cette annee])

  ]