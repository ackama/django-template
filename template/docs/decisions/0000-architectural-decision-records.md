# 0000 Architectural Decision Records

- Date: 2023-03-31
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Context

We want to ensure we start this project right. We need a way to ensure that potentially
costly on contentious decisions that are made along the way are properly recorded.

## Decision

We adopt a light weight log of architectural decision records of the important
decisions made along the way. Each log entry is kept fairly simple, with 3 key headings:

- **Context**: The background information relevant to the decision being
  recorded
- **Decision**: The actual decision made
- **Implications**: The intended outcomes and implications for the project, and
  in particular an up-front or ongoing work that needs to be done to adopt the
  decision made.

The record should also provide basic metadata about itself:

- The _date_ at which it was written
- The _author(s)_ of the record
- The _status_ of the record:
    - `draft`, still in progress and not yet formally adopted
    - `active`, formally adopted
    - `supersede`, has been replaced by a newer ADR (include a reference it)
    - `obsolete`, not longer relevant but not directly superseded

Not every feature or pull request needs an accompanying ADR, just those which have
either a significant future impact or represent significant effort to arrive at.

## Implications

Code, even commented code, does not usually reflect the decisions made during
its production. The decisions often represent either a significant investment in
time or may reflect a series of known compromises. Without a mechanism for
recording these decisions it is easy for future developers (including those who
made the decision in the first place) to misunderstand decisions that have been
made or the implications of changing them.

Ensuring these records are made and each new decision of significance is added
does have a overhead - but likely considerably less than making future choices without
the benefits of the historic decision records. Adopting a light weight approach to
recording our decision making process also actively encourage a degree of forward think,
emphasising the importance of a design phase for the more major undertakings.

<!-- Links -->
[jmoss]: mailto:jmoss@commoncode.io

<!-- Abbreviations -->
*[ADR]: Architectural Decisions Record
