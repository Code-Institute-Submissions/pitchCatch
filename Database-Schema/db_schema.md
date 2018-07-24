# pitchCatch Database Schema


## Entity-Relationship Model
### Entities:
1. Movement (Pitcher)
2. Developer (Catcher)
3. Proposal (Pitch)


### Relationships between entitites:
* A **Movement** *makes* a **Proposal**
* A **Developer** *expresses interest* in a **Proposal**
* A **Developer** *works with* a **Movement** on a **Proposal**
* A **Developer** *works with* other **Developers** on a **Proposal**

### Cardinality of relationships
#### One-to-Many
A Movement can have many Proposals 
A Proposal can only have one Movement


#### Many-to-Many
A Proposal can have many Developers
A Developer can support many Proposals


## User Stories
* As a **developer**, I want to *find* interesting **projects** which match my skill set
* As a **developer**, I want to *participate* in interesting **projects**
* As a **movement**, we want to *propose* **projects**  
* As a **movement**, we want to *find* experienced **developers** to work on our **projects**


## Entity Attributes
(work back)

## CRUD operations 


## SQLAlchemy models
|Pitchers               | Catchers              | Pitches               |     
|       ---             |   ---                 | ---                   |
| `id`                  | `id`                  | id                    |
| movement_name         | `developer_name`      | proposal_name         |
| movement_description  | developer_description | proposal_outline      |
| interests             | interests             | interests             |
| region                | frontend-interest     | launch_date           |
| movement_url          | backend-interest      | pitcher_id            |
| email                 | frontend-experience   |                       |
|                       | backend_experience    | *pitcher(relationship)* |
|                       | prog_languages        |
|                       | email                 |
|                       | region                |
|                       | pitches_caught        |    
                        
                        