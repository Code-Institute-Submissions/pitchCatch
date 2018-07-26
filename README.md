![alt text](Database-Schema/FullSizeRender.jpggit )

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

Once a **Pitcher** has registered their profile details, they are able to make a **Pitch**. 

**Pitches** are ideas for software projects that have been proposed by **pitchers**.

All **Pitches** on the pitchCatch platform are searchable, and if a software developer, or **Catcher**, is interested in participating in a particular project, they can choose to **Catch** the **Pitch**.   

**Catchers** and **Pitchers** have profile pages outlining their interests, skills, etc and these can also be searched to find potential partners, contactable through the email information provided. 


### How does it work
 
pitchCatch is built using the python-based **Flask** micro-framework and is written in **python 3.4.3**. 

**SQLAlchemy** is used to map the application's Python classes to a **PSQL** database. User data is handled using **WTForms-Alchemy**

The site is styled using the **Materialize CSS** front-end framework and **JQuery** code for enhancing user-experience. 

The database and the entire application is hosted on the **Heroku** platform **nb. to be deployed** 

The site is designed using a **mobile-first** approach and can be viewed [HERE](https://pitchcatch.herokuapp.com/). 


## Features
Find below the features provided in the pitchCatch application. 

### Existing Features

> please note that pitchCatch does not yet include authentication

#### Registration
* Campaigns and social movements can register as **Pitchers** providing profile details 
* Software developers can register as **Catchers** providing profile details
* **Pitchers** can register **Pitches** by providing details of their proposal

#### Profile
* the details inputed during registration for each **Pitcher**, **Catcher** and **Pitch** are presented on individual profile pages 
* all existing profiles can be **edited** or **deleted**

#### Pitches and Catches
* the titles of every **Pitch** made by a campaign or social movement are listed on their Pitcher profile page 
* a **Catcher** expresses an interest in a particular project (**Pitch**) by **Catching** it. This feature is available on each Pitch profile page. The titles of the projects which the developer is interested in are listed on the Catcher profile page
* the list of developers who are interested in a particular project are, in turn, listed on the Pitch profile pages
* projects, or **Pitches**, remain on pitchCatch regardless of whether a **Pitcher** is deleted and leaves the pitchCatch network. This persistence recognises that **ownership** is distributed among all of the participants in the project, not simply the campaign or social movement who had the origninal seed idea

#### Search
All of the **Pitchers**, **Catchers** and **Pitches** on the pitchCatch platform can be searched by using filters. Records matching the user's search criteria are diplsayed in a table  


### Features Left to Implement
- user authentication
- testing


## Database Schema
The pitchCatch database schema was developed by progessing through the following steps:
- defining the Entity-Relationship Model (ERM) and the cardinality of relationships to articulate the basic relations and constraints between the python classes as represented in a database
- from the relationships defined in the ERM, deciding to use a relational database (PSQL) to store the data
- developing user stories to draw out why and how users would interact with the data in the application
- establishing the entity attributes that are required to meet the expectations outlined in the user stories 
- using the ERM to determine the Create, Read, Update, Delete (CRUD) functions relative to each entity
- developing the python classes based on above

Examples of outputs from each of the above steps are provided in the [Database Schema sub-directory](Database-Schema/db_schema.md)

## Tech Used

### Specific technology used on the application includes:

### Code
- **HTML**, **CSS**, **JQuery** and **Python**
  - Base languages used to create application
- [Flask 1.0](http://flask.pocoo.org/docs/1.0/)
    - **Flask** is used as micro-framework to create the application
- [SQLA-Alchemy 1.2.9](https://www.sqlalchemy.org/)
    - **SQLA-Alchemy** is an extension applied to Flask providing an Object Relational Mapper to create models which map the application's classes to the postgreSQL database 
- [WTForms-Alchemy 0.16.7](https://www.djangoproject.com/)
    - **WTForms-Alchemy** generates forms from the SQLAlchemy models
- [Materialize 1.0.0-rc.2](https://materializecss.com/)
    - **Materialize** is used to render a responsive layout and create modals and tooltips to enable quicker, selective browsing
- [JQuery 3.3.1](https://jquery.com)
    - **JQuery** adds animation styling to the site to enhance user experience.
- [Sass](https://sass-lang.com/)
    - **Sass/scss** CSS extension is used to code and organise stylesheets

### Hosting
- [Heroku-Postres](https://www.heroku.com/postgres)
    - During development mode, models were migrated to the a psql database. In production mode, data is stored in a postgreSQL database using **Heroku-Postres**.
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the pitchCatch application.


## Contributing
 
### Getting the code up and running

1. Create a virtual environment running python 3.4.3 as the default in your IDE
2. Clone this repository by running the ```git clone https://github.com/Deasun/pitchCatch.git``` command
3. pip install requirements
4. Set up a psql database and connect the application to it
5. Paste your psql database details in the config.py file:
> `engine = create_engine('postgresql://<username>:<password>@localhost:5432/<database name>', convert_unicode=True)`
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. We welcome all contributions to improving our code and encourage pull requests. Please see **Features To Be Implemented** for particular features we are eager to progress.

## Credits

### Media
- Background image to the site was produced by Nathalie Caleyron [Nathalie Caleyron](https://www.instagram.com/nathaliecaleyron/)

### Profile Details
- the profile details provided for **Pitchers** have been copied from the particular social movement or campaign's website 
- all of the profile details provided to register pitches and catchers are fictitious




