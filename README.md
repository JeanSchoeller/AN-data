# AN-data
**Data from the French National Assembly**

Welcome to the AN-data repository, where we collect and organize data from the French National Assembly (FNA). This project aims to create a comprehensive database of parliamentary interventions along with detailed information about the speakers.

[Google Drive](https://drive.google.com/drive/folders/1AdHZsDcZonHHy60vERBwGUkjh2PYINH0?usp=sharing) containing most of the data gathered so far.


## Objectives

- **Database Creation**: Compile a database containing the majority of interventions from the FNA.
- **Speaker Information**: Associate each intervention with the respective speaker and gather additional relevant information about them.

## Table of Contents

- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

## Data Structure

The database is structured to ensure ease of access and analysis. Here’s an overview of the main columns:

### Database Table

- `id`: Unique identifier for the speaker.
- `txt`: Unique identifier for the speaker.
- `legislatureLast`: Last legislature term.
- `civ`: Civil title of the speaker.
- `nom`: Last name of the speaker.
- `prenom`: First name of the speaker.
- `villeNaissance`: Birth city of the speaker.
- `naissance`: Date of birth of the speaker.
- `age`: Age of the speaker.
- `groupe`: Political group affiliation.
- `groupeAbrev`: Abbreviation of the political group.
- `departementNom`: Name of the department represented.
- `departementCode`: Code of the department represented.
- `circo`: Constituency represented.
- `datePriseFonction`: Date the speaker took office.
- `job`: Job title of the speaker.
- `mail`: Email address of the speaker.
- `twitter`: Twitter handle of the speaker.
- `facebook`: Facebook profile of the speaker.
- `website`: Personal or official website of the speaker.
- `nombreMandats`: Number of mandates served.
- `experienceDepute`: Experience as a deputy.
- `scoreParticipation`: Participation score.
- `scoreParticipationSpecialite`: Specialized participation score.
- `scoreLoyaute`: Loyalty score.
- `scoreMajorite`: Majority score.
- `active`: Active status of the speaker.
- `dateMaj`: Date of the last update.

*N.B: A lot of this data is missing for the datasets from 2007 to 2017 - it is being added*

## Sources

The data and code in this repository are sourced from the following:

- [French National Assembly Website](http://www2.assemblee-nationale.fr/](https://data.assemblee-nationale.fr/))
- [NosDéputés.fr API](https://www.nosdeputes.fr/api)


## Contributing

We welcome contributions from the community! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
   
