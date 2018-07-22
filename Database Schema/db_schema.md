# Database Schema

## User Stories
As a developer, I want to find interesting projects which match my skill set
As a developer, I want to participate in interesting projects
As a movement, we want to propose projects  
As a movement, we want to find experienced developers to work on our projects







One-to_many - 3 foreign keys:
1) A Pitcher can have many Pitches
2) A Pitch can have one Pitcher (Pitch.origin_pitch)

1) A Catcher can have many Catches
2) A Catch can have one Catcher (Catch.catch_origin)

1) A Pitch can have many Catches
2) A Catch can have one Pitch (Catch.pitch_origin)


Many to many?