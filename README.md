# pitchCatch
A platform matching social movements with software developers to create innovative and effective applications.

## Overview
 
### What is this application for?
Social movements often lack the resources, expertise or time needed to benefit from the advantages technology can bring to their campaigns. 

On the other hand, socially conscious software developers often find themselves without the connections required to engage in meanginful projects that will be of practical use to people advancing progressive causes.

pitchCatch is a platform to bring these two worlds together in order to create effective technological tools for change.

### What does it do?
Users sign-up to pitchCatch under two categories:
* **Pitchers** are social movements or campaigns
* **Catchers** are software developers

Once a **pitcher** has registered their profile details, they are able to make a **Pitch**. **Pitches** are ideas for software projects that have been proposed by **pitchers**.

All **Pitches** on the pitchCatch platform are searchable, and if a software developer, or **catcher**, is interested in participating in a particular project, they can choose to **catch** the **pitch**.   

**Catchers** and **pitchers** have profile pages outlining their interests, skills, etc and these can also be searched to find potential partners and contacted using the contact information provided. 


### How does it work
 
pitchCatch is built using the python-based **Flask** micro-framework and is written in **python 3.4.3**. 

**SQLAlchemy** is used to map the application's classes to a **PSQL** database. User data is handled using **WTForms-Alchemy**

The site is styled using the **Materialize CSS** front-end framework and **JQuery** code for enhancing user-experience. 

The database and the entire application is hosted on the **Heroku** platform **nb. to be deployed** 

The site is designed using a **mobile-first** design and can be viewed [HERE](insert link following deployment). 


## Features
Find below the features provided in the pitchCatch application. 
### Existing Features

> please note that pitchCatch does not yet include authentication

#### Registration
* Campaigns and social movements can register as **Pitchers** providing profile details 
* Software developers can register as **Catchers** providing profile details
* **Pitchers** can register **Pitches** by providing details of their proposal

#### Profile
* the details inputed during registration for each **pitcher**, **catcher** and **pitch** are presented on individual profile pages 
* existing profiles can be **edited** or **deleted**

#### Pitches and Catches
* the titles of all the **pitches** which have been made by a campaign or social movement are listed on their pitcher profile page 
* a **catcher** expresses an interest in a particular project (**pitch**) by **catching** it. This feature is available on the pitch profile page. The titles of the projects which the developer is interested in are listed on the catcher profile page
* the list of developers who are interested in a particular project are, in turn, listed on the pitch profile pages
* projects, or **pitches**, remain on pitchCatch regardless of whether a **Pitcher** is deleted and leaves the pitchCatch network. This persistence recognises that **ownership** is distributed among all of the participants in the project, not simply the campaign or social movement who had the origninal idea

#### Search
* all of the pitchers, catchers and pitches on the pitchCatch platform can be searched by using filters. Records matching the user's search criteria are diplsayed in a table  


### Features Left to Implement
- user authentication
- testing


## Database Schema
Share details of how you created your database schema in your README. Consider sharing working drafts or finalised versions of your database schema in a 'Database Schema' folder in your repo. Provide a link to this folder in your README.


- User Stories
- - Entity-Relationship Model
- Cardinality of Relationships 1-1, etc
- CRUD Operations mapped
- Database Scheme FK & helper table (final)


## Tech Used

### Specific technology used on the application includes:

### Code
- **HTML**, **CSS**, **JQuery** and **Python**
  - Base languages used to create website
- [Flask 1.0](http://flask.pocoo.org/docs/1.0/)
    - **Flask** is used as a basic python framework to create the application
- [SQLA-Alchemy 1.2.9](https://www.sqlalchemy.org/)
    - **SQLA-Alchemy** is an extension applied to Flask to provide an Object Relational Mapper to create models which map the application's classes to the postgreSQL database 
- [WTForms-Alchemy 0.16.7](https://www.djangoproject.com/)
    - **WTForms-Alchemy** generates forms from the SQLAlchemy models
- [Materialize 1.0.0-rc.2](https://materializecss.com/)
    - **Materialize** is used to render a responsive layout and create modals and tooltips to enable quicker, selective browsing
- [JQuery 3.3.1](https://jquery.com)
    - **JQuery** adds animation styling to the site to enhance user experience.
- [Sass](https://sass-lang.com/)
    - **Sass/scss** CSS extension is used to code and organise CSS stylesheets

### Hosting
- [Heroku-Postres](https://www.heroku.com/postgres)
    - During development mode, models were migrated to the a psql database. In production mode, data is stored in a postgreSQL database using **Heroku-Postres**.
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the pitchCatch application.


## Contributing
 
### Getting the code up and running

1. Create a virtual environment running python 3.4.3 as the default in your IDE
2. Clone this repository by running the ```git clone https://github.com/Deasun/pitchCatch.git``` command
3. python manage.py make migrations etc.
4. pip install requirements
5. The project will now run on [localhost](http://127.0.0.1:8080)
6. We welcome all contributions to improving our code, so make changes you think are needed/desired and submit a pull request

## Credits

### Media
- Background image to the site was produced by Nathalie Caleyron [Nathalie Caleyron](https://www.instagram.com/nathaliecaleyron/)

### Profile Details
- the profile details provided for 'pitchers' have been copied from the particular social movement or campaign's website 
- all of the profile details provided to register pitches and catchers are fictitious




