# Testing
The site was tested manually by walking through the features from the perspective of the two targeted user groups: Pitchers (social movements) and Catchers (software developers).

### Registration and Profile
The following process was used to test the **Registration Form** feature for Pitchers, Catchers, Pitches:

##### i. input new and <u>valid entry</u> into the database and check if the following verification indicators occur:
- a **flash message** <em>"Welcome to pitchCatch"</em> (Pitchers and Catchers) or <em>"Your pitch is registered with pitchCatch!"</em> (Pitches) 
- the **PSQL database** (local PSQL in development and Heroku Postgres post-deployment) contains the **new entry** in full
- a **new Profile Page** for the entry exists containing the data entered into the form
- if a new Pitch is registered, the **name of the Pitch appears on the Profile page of the Pitcher** who proposed it
- the total in the title which is rendered on the relevant **'Search'** page is updated, for example <em>"**4 catchers** are registered with pitchCatch"</em> is updated to <em>"**5 catchers** are registered with pitchCatch"</em>

##### ii. input an <u>entry which leaves a field incomplete</u> and check the following: 
- the **form does not submit** and an **error message** appears over the field qhich requires valid data
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no new Profile Page** exists

##### iii. input <u>an invalid entry</u> which uses invalid characters/does not use required characters (e.g. not inputting an email address in the email field) and check the following:
- the **form does not submit** and an **error message** appears over the field qhich requires valid data
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no new Profile page** exists

##### iv. input a <u>duplicate entry</u> and check the following:
- a **flash message** appears <em>"Your movement name is already registered with pitchCatch!"</em> (Pitchers), <em>"Your username is already registered with pitchCatch!"</em> (Catchers), or <em>"This pitch name is already registered with pitchCatch!"</em> (Pitches)
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no new Profile page** exists

### Catching a Pitch
The application includes a feature, accessible on the relevant Pitch Profile page, which enables Catchers to express an interest in the proposal - or Catch the Pitch. The following process was used to test the **Catch Form**:

##### i. a Catcher is selected from the dropdown list and expresses and interest in the Pitch (which they have not expressed an interest in yet):
- a flash message appears <em>"Pitch caught!"</em>
- the **PSQL database** (local in development and Heroku Postgres post-deployment) contains the **new entry** to the 'caught' helper table
- the **Catcher's username appears on the Pitch Profile page** as being interested in the proposal
- the **Pitch name appears on the Catcher's Profile page** as being proposal s/he is interested in

##### ii. a Catcher expresses interest in a Pitch they have already expressed an interest in (duplicate):
- a **flash message** appears <em>"You've already caught this pitch!"</em>. The user is **not redirected** to any other page.
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is not updated, particularly no new entries are made to the caught helper table
- the **Catcher's username <u>does not</u> appear on the Pitch Profile page** as being interested in the proposal
- the **Pitch name <u>does not</u> appear on the Catcher's Profile page** as being proposal s/he is interested in

### Searching
All of the Pitcher, Catcher and Pitch records are accessible through the **search feature** which use different and appropriate fields to filter responses. **Sample data** was entered for each of the models to ensure that search feature could be tested robustly using different criteria, but also a small enough sample to be able to measure search outcomes against known entries. The following process was used to test the **Search Form** and features:

##### i. searching for an existing record criteria that is known to exist:
- the **list of Catchers, Pitchers or Pitches maching the search criteria** appear in a table
- the **total in the title is updated** to reflect the search results, e.g. <em>"2 catchers are registered with pitchCatch"</em> and the **search criteria stays visible** and the user can further filter their search

##### ii. searching for a record that does not exist
- **no results are returned** and the **total in the title is updated** to reflect the results, for e.g. <em>"0 catchers are registered with pitchCatch"</em>

##### iii. searching with <u>empty fields/no criteria specified</u>
- **returns the entire list** of Pitchers/Catchers/Pitches and the **total in the title remains unaltered**

### Editing
As the existing application is not authenticated, every entry is editable by users. The **edit feature** is accessible from the relevant Profile page and users are **redirected** to an **Edit Form** which is auto-filled with existing data from the database. The following process was used to test the **Edit Form** and features:

##### i. the auto-filled data on the Edit Form is correct
- the auto-filled data is checked against the data in the **PSQL database** to ensure the details are complete and accurate

##### ii. record is updated using duplicate data
- if duplicate data is entered into a field on the Edit Form which requires a unique entry, the form is not saved and the edit profile page is still displayed
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no updates to the Profile Page** are made

##### iii. invalid data is entered
- the **form does not submit** and an **error message** appears over the field qhich requires valid data
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no updates to the Profile Page** are made

##### iv. required fields are left empty
- the **form does not submit** and an **error message** appears over the field which requires valid data
- the **PSQL database** (local in development and Heroku Postgres post-deployment) is **not updated**
- **no updates to the Profile Page** are made

##### v. correct data is entered
- a **flash message** <em>"Changes Saved!"</em> appears on the Profile page the user is **redirected** to 
- the **PSQL database** (local in development and Heroku Postgres post-deployment) contains the **updated entry**
- a **new Profile Page** for the entry exists containing the updated data entered into the form

### Deleting
As the existing application is not authenticated, every Pitcher, Catcher or Pitch entry can be deleted by users. The **delete feature** is accessible from the relevant Profile page (rubbish bin icon). The following process was used to test the **Delete Feature**:

##### i. successful deletion
- the rubbish bin icon is clicked and the user is redirected to the Pitcher/Catcher/Pitch serach page with a falsh message rendered saying, for e.g. <em>"Pitcher deleted!"</em>
- the **PSQL database** (local in development and Heroku Postgres post-deployment) no longer contains the deleted record
- the **Profile Page** for the deleted entry no longer exists

##### ii. successful persistence of Pitches
- if a Catcher or a Pitcher is deleted, **any Pitches which they are associated with persist** - the Pitch Profile page and the Pitch record in the PSQL database remain

### Links and routes
The links and routes in the application were tested through user stories to ensure that the site navigation worked, often following similar paths to the testing above - for example:

    - I am a software developer/we are a social movement wanting to register on pitchCatch
    - I am a software developer/we are a social movement wanting to leave pitchCatch
    - We are a social movement looking for an experienced developer interested in social and economic rights
    - I am a software developer looking for projects which focus on the right to privacy
    - I am a software developer looking to work with social movements based in Aisa
    - We are a social movement looking for other organisations working on similar topics
    - We are a social movement looking to see if any proposals exist which are similar to our idea
    - I am a software developer interested in contributing to the 'snAPP' proposal

These stories were pursued until their objective was met.

### JQuery
All of the JQuery used to style the site was customised by Materialize CSS to enable their components to work. This code was tested by triggering the event, refreshing the page, trigerring it again and ensuring it worked.


### Broswer compatibility 
The application was tested in each of the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox
  - Safari
 
All of the browsers were compatible except **Opera** which displayed an occasional and inconsistent bug. On any of the profile pages (Pitcher/Catcher/Pitch), when the card was opened to reveal further details, the card element would 'shake' for a second before stopping. This also happened intermittently when selecting the dropdown menu.  