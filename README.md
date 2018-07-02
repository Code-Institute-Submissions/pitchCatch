Data
1) outline development phase
2) developed mysql command line protoype
3) translated into psql to host from heroku postgres
4) reverse engineered using sqlacodegen==1.1.6 to create Classes and run code in python


Database Schema:
1) show orignial concept (take from paper)
2) show mysql construct
3) show creation of four tables


One-to_many - 3 foreign keys:
1) A Pitcher can have many Pitches
2) A Pitch can have one Pitcher (Pitch.origin_pitch)

1) A Catcher can have many Catches
2) A Catch can have one Catcher (Catch.catch_origin)

1) A Pitch can have many Catches
2) A Catch can have one Pitch (Catch.pitch_origin)


Many to many?
