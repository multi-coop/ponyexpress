#let legal_title(content) = align(center,
  box(inset: (y:20pt),strong(smallcaps(content)))
)

#let article_count = counter("article")
#let mention_count = counter("mention")

#let article(it) = block[
  #article_count.step()
  #mention_count.update(0)
  #smallcaps(strong(
    text(
      13pt,
      [Article #context article_count.display() : #it]
    )
  ))
  #line(length: 100%)
]

#let mention(it) = block(breakable: false,[
  #mention_count.step()
  #text(
    11pt,
    {
      let width = 1em
      grid(
        columns: (1em, 1fr),
        gutter: 1em,
        [#context article_count.display().#context mention_count.display() ],
        [#it] 
      )
    }
  )
]
)



