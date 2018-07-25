# pitchCatch Database Schema


## Entity-Relationship Model

### Entities
> user inputted data stored in the database will concern the below entities:

1. **Movement (Pitcher)**. A social movement or campaign.
2. **Developer (Catcher)**. A software developer.
3. **Proposal (Pitch)**. A project proposed by a social movement or campaign.


### Relationships
> the relationships between the different entitites are:
* A **Movement** *makes* a **Proposal**
* A **Developer** *expresses interest* in a **Proposal**
* A **Developer** *works with* a **Movement** on a **Proposal**
* A **Developer** *works with* other **Developers** on a **Proposal**

##### One-to-Many
    A Movement can have MANY Proposals 
    A Proposal can only have ONE Movement

##### Many-to-Many
    A Proposal can have MANY Developers
    A Developer can support MANY Proposals


### Attributes:

#### User Stories
> anticipating what users will do when using the application, what their motivations are and how they will fulfill their motivations. Nouns (e.g. **developer**) represent entities. Verbs (e.g. *find*) help to express relationships and how the user will interact with the data. Adjectives (e.g. `interesting`) suggest the attributes that entities must possess to meet users' browsing and functionality expectations  
* As a **developer**, I want to *find* `interesting` **proposals** which match my skill set
* As a **developer**, I want to *participate* in `interesting` **proposals**
* As a **developer**, I want to *find* (and *contact*) `interesting` **movements** 
* As a **movement**, we want to *make* `interesting` **proposals**  
* As a **movement**, we want to *find* (and *contact*) `experienced` and `interested` **developers** to work on our **proposals**


#### Entity Attributes
> using the adjectives identified in the user stories to identify the attributes which the entitites must have to carry out the interactions in the user stories

**Pitchers:** name, activity, mission, location, url, email, proposals

**Catchers:** name, personal details, activist interests, location, programming interests, programming experience, email, proposals interested in

**Pitches:** title, description, theme of proposal, launch date, proposer, interested developers

#### CRUD operations 
> mapping the various user inputs into and interactions with the database


    Pitchers [CREATE] records
    Catchers [CREATE] records
    Pitchers [CREATE] Pitches 
    Catchers browse [READ] Pitches and express interest in [UPDATE] the proposals 
    Pitchers browse Catcher profiles [READ] to find developers with matching interests
    Catchers browse Pitcher profiles [READ] to find social movements/campaigns with matching interests
    Pitchers can remove their records [DELETE]
    Catchers can remove their records [DELETE]
    Proposals cannot be removed (ideas can evolve)

## SQLAlchemy models
> The application's models were designed based on the ERM above and using **SQLAlchemy** column types and Utils-types.<br><br>The columns correspond to the entity attributes identified above. There is a **foreign key** (pitcher_id) in the Pitch table pointing to its parent (id) in the **Pitcher** table. <br><br>To capture the many-to-many relationship between **Catchers** and **Pitches**, a **helper table** (**'caught'**) was created consisting of two **foreign keys** ('catcher_id', 'pitch_id') pointing towards their respective parents in the **Pitch** (id) and **Catcher** (id) tables.

|Pitchers|Catchers|Pitches|caught|     
| --- | --- | --- | --- |
| `id` | `id` | `id` | `catcher_id (fk)` |
| `movement_name`| `developer_name`| `proposal_name`| `pitch_id (fk)`|
| `movement_description`| `developer_description` | `proposal_outline`|
| `interests` | `interests` | `interests` |
| `region` | `frontend_interest`| `launch_date` |
| `movement_url` | `backend_interest` | `pitcher_id (fk)` |
| `email` | `frontend_experience`|  |
|       | `backend_experience`    | `pitcher(relationship)` |
|        | `prog_languages`   |
|        | `email`   |
|        | `region`   |
|     | `pitches_caught (relationship)` |    

See final models (with datatypes) [HERE](/models.py)

                        
                        