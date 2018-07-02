# models
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy_utils import URLType, EmailType
from sqlalchemy.orm import sessionmaker, relationship
from wtforms_alchemy import ModelForm





# Models
engine = create_engine('postgresql://ubuntu:pw123@localhost:5432/pitch_catch_caught')
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()



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
        URLType(), nullable=False,
        info={
            'label': 'Show us what you do',
            'description': 'Provide a website link'}
    )
    movement_description = sa.Column(
        Text, nullable=False,
        info={'label': 'Describe what you do'}
    )
    interests = sa.Column(
        Text, nullable=False,
        info={
            'label': 'What is your main interest...',
            'choices': [
                'promoting social and economic equality',
                'protecting the right to privacy',
                'exposing corruption and maladministration', 
                'challenging discrimination',
                'enhancing communication and collaboration between activists', 
                'creating and sustaining alternative platforms/institutions'
            ]
        }
    )
    email = sa.Column(
        EmailType, nullable=False, unique=True,
        info={'label': 'Contact email'}
    )
    region = sa.Column(
        String(40), nullable=False,
        info={'label': 'Where are you based?',
            'choices': [
                'Asia',
                'Africa',
                'Europe',
                'North America',
                'South America',
                'Australia'
            ]
        }
    )


"""Pitcher form"""
class PitcherForm(ModelForm):
    class Meta:
        model = Pitcher



"""
Pitch model
"""
class Pitch(Base):
    __tablename__ = 'pitches'
    
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    proposal_name = sa.Column(
        String(200), nullable=False, unique=True,
        info={'label': 'Name of your proposal'}
    )
    proposal_outline = sa.Column(
        Text, nullable=False,
        info={'label': 'Details of your proposal'}
    )
    interests = sa.Column(
        Text, nullable=False,
        info={
            'label': 'What is your main interest...',
            'choices': [
                'promoting social and economic equality',
                'protecting the right to privacy',
                'exposing corruption and maladministration', 
                'challenging discrimination',
                'enhancing communication and collaboration between activists', 
                'creating and sustaining alternative platforms/institutions'
            ]    
        }
    )
    launch_date = sa.Column(
        Date,
        info={'label': 'Ideal launch date'}
    )
    pitch_url = sa.Column(
        URLType(),
        info={
            'label': 'Show us the need for your proposal',
            'description': 'Provide a website link'})
    pitcher_id = sa.Column(sa.Integer, sa.ForeignKey('pitchers.id'), nullable=False)
    pitcher = sa.orm.relationship('Pitcher', backref=sa.orm.backref('throw', lazy=True))


"""PitchForm"""
class PitchForm(ModelForm):
    class Meta:
        model = Pitch



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
            'label': 'Show us what you do',
            'description': 'Provide a website link'}
    )
    developer_description = sa.Column(
        Text,
        info={'label': 'Tell us about yourself'}
    )
    interests = sa.Column(
        Text, nullable=False,
        info={
            'label': 'What is your main interest...',
            'choices': [
                'promoting social and economic equality',
                'protecting the right to privacy',
                'exposing corruption and maladministration', 
                'challenging discrimination',
                'enhancing communication and collaboration between activists', 
                'creating and sustaining alternative platforms/institutions'
            ]    
        }
    )
    frontend_interest = sa.Column(
        String(10), nullable=False,
        info={
            'label': 'Interested in Front-end development?',
            'choices': [
                'Yes',
                'No',
            ]
        }
    )
    backend_interest = sa.Column(
        String(10), nullable=False,
        info={
            'label': 'Interested in Back-end development?',
            'choices': [
                'Yes',
                'No',
            ]
        }
    )
    frontend_experience = sa.Column(
        String(50), nullable=False,
        info={
            'label': 'Your Front-end experience:',
            'choices': [
                'Beginner',
                'Intermediate',
                'Expert'
            ]
        }
    )
    backend_experience = sa.Column(
        String(50), nullable=False,
        info={
            'label': 'Your Back-end experience:',
            'choices': [
                'Beginner',
                'Intermediate',
                'Expert'
            ]
        }
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
        String(40),
        info={'label': 'Where are you based?',
            'choices': [
                'Asia',
                'Africa',
                'Europe',
                'North America',
                'South America',
                'Australia'
            ]
        }
    )
    pitches_caught = sa.orm.relationship('Pitch', secondary=caught, backref=sa.orm.backref('pitch_catch', lazy='dynamic'))

"""CatcherForm"""
class CatcherForm(ModelForm):
    class Meta:
        model = Catcher

# if __name__ == "__main__":
#     Base.metadata.create_all(engine, checkfirst=True)