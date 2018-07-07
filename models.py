# models
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy_utils import URLType, EmailType, ChoiceType
from sqlalchemy.orm import sessionmaker, relationship
from choices import INTERESTS, REGIONS, YN, EXPERIENCE
from database import Base


  


"""
Helper table used for many to many relationship for Caught pitches
"""
caught = sa.Table('caught',
    Base.metadata,
    sa.Column('catcher_id', sa.Integer, sa.ForeignKey('catchers.id')),
    sa.Column('pitch_id', sa.Integer, sa.ForeignKey('pitches.id'))
    )


"""
Pitcher model
"""
class Pitcher(Base):
    __tablename__ = 'pitchers'
    
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    movement_name = sa.Column(
        String(100), nullable=False, unique=True,
        info={'label': 'Movement name'}
    )
    movement_url = sa.Column(
        URLType(),
        info={'label': 'Provide a link to your work'}
    )
    movement_description = sa.Column(
        Text, nullable=False,
        info={'label': 'Describe what you do'}
    )
    interests = sa.Column(
        ChoiceType(INTERESTS), nullable=False,
        info={'label': 'What is your main interest?'}        
    )

    email = sa.Column(
        EmailType, nullable=False, unique=True,
        info={'label': 'Contact email'}
    )
    region = sa.Column(
        ChoiceType(REGIONS), nullable=False,
        info={'label': 'Where are you based?'},        
    )

    def __init__(self, movement_name=None, movement_url=None, movement_description=None,
        interests=None, email=None, region=None):
        self.movement_name = movement_name
        self.movement_url = movement_url
        self.movement_description = movement_description
        self.interests = interests
        self.email = email
        self.region = region
    
    def __repr__(self):
        return '<Pitcher %r>' % (self.movement_name)


"""
Pitch model
"""
class Pitch(Base):
    __tablename__ = 'pitches'
    
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    proposal_name = sa.Column(
        String(200), nullable=False, unique=True,
        info={'label': 'Name of proposal'}
    )
    proposal_outline = sa.Column(
        Text, nullable=False,
        info={'label': 'Details of your proposal'}
    )
    interests = sa.Column(
        ChoiceType(INTERESTS), nullable=False,
        info={'label': 'What is your main interest?',}
    )
    launch_date = sa.Column(
        Date,
        info={'label': 'Ideal launch date'}
    )
    pitcher_id = sa.Column(sa.Integer, sa.ForeignKey('pitchers.id'), nullable=False)
    pitcher = sa.orm.relationship('Pitcher', backref=sa.orm.backref('throw', lazy=True))

    
    def __init__(self, proposal_name=None, proposal_outline=None,
        interests=None, launch_date=None, pitcher_id=None):
        self.proposal_name = proposal_name
        self.proposal_outline = proposal_outline
        self.interests = interests
        self.launch_date = launch_date
        self.pitcher_id = pitcher_id
    
    def __repr__(self):
        return '<Pitch %r>' % (self.proposal_name)


"""
Catcher model
"""
class Catcher(Base):
    __tablename__ = 'catchers'
    
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    developer_name = sa.Column(
        String(150), nullable=False, unique=True,
        info={'label': 'Pick a username'}
    )
    developer_url = sa.Column(
        URLType(),
        info={
            'label': 'Provide a link to some of your code'}
    )
    developer_description = sa.Column(
        Text,
        info={'label': 'Tell us about yourself'}
    )
    interests = sa.Column(
        ChoiceType(INTERESTS), nullable=False,
        info={'label': 'What is your main interest?'}        
    )
    frontend_interest = sa.Column(
        ChoiceType(YN), nullable=False,
        info={'label': 'Interested in Front-end development?'}
    )
    backend_interest = sa.Column(
        ChoiceType(YN), nullable=False,
        info={'label': 'Interested in Front-end development?'}
    )
    frontend_experience = sa.Column(
        ChoiceType(EXPERIENCE), nullable=False,
        info={'label': 'Your Front-end experience:'}
    )
    backend_experience = sa.Column(
        ChoiceType(EXPERIENCE), nullable=False,
        info={'label': 'Your Back-end experience:'}
    )
    prog_languages = sa.Column(
        Text, nullable=False,
        info={'label': 'What languages have you coded in?'}
    )
    email = sa.Column(
        EmailType, nullable=False, unique=True,
        info={'label': 'Contact email'}
    )
    region = sa.Column(
        ChoiceType(REGIONS), nullable=False,
        info={'label': 'Where are you based?'}
    )
    pitches_caught = sa.orm.relationship('Pitch', secondary=caught, backref=sa.orm.backref('pitch_catch', lazy='dynamic'))

    def __init__(self, developer_name=None, developer_url=None, developer_description=None,
        interests=None, frontend_interest=None, backend_interest=None, frontend_experience=None,
        backend_experience=None, prog_languages=None, email=None, region=None):
        self.developer_name = developer_name
        self.developer_url = developer_url
        self.developer_description = developer_description
        self.interests = interests
        self.frontend_interest = frontend_interest
        self.backend_interest = backend_interest
        self.frontend_experience = frontend_experience
        self.backend_experience = backend_experience
        self.prog_languages = prog_languages
        self.email = email
        self.region = region
    
    def __repr__(self):
        return '<Pitcher %r>' % (self.movement_name)