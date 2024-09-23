# AN-data
**Data from the French National Assembly**

Welcome to the AN-data repository, where we collect and organize data from the French National Assembly (FNA). This project aims to create a comprehensive database of parliamentary interventions along with detailed information about the speakers.

A [Google Drive](https://drive.google.com/drive/folders/1AdHZsDcZonHHy60vERBwGUkjh2PYINH0?usp=sharing) was setup, containing most of the data gathered so far.


## Objectives

- **Database Creation**: Compile a database containing the majority of interventions from the FNA.
- **Speaker Information**: Associate each intervention with the respective speaker and gather additional relevant information about them.

## To-do list

- [x] Build the database from 2007 to 2024 using the SQL dumps from [Nos Députés](nosdeputes.fr).
- [ ] Use OCR to access all the Journal Officiels interventions per deputy from 1958
   - [x] Open Google [Collaboratory Notebook](https://colab.research.google.com/drive/1t1ia3nibrQXhjkCTbnd2KkCL-P1i-kG5?usp=sharing) to work on
   - [x] Use Tesseract to read the documents
   - [ ] Identify a starting point from which the OCR can begin from
   - [ ] Identify an end point from which to stop it
   - [ ] Try on a single document
   - [ ] See if we can build the database from there and what troubleshooting is needed

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

SQL prompts:

SELECT parlementaire_id, fonction, date, type, intervention FROM intervention WHERE parlementaire_id IS NOT NULL INTO OUTFILE '/var/export.csv' FIELDS TERMINATED BY '~' LINES TERMINATED BY '\n';
SELECT id, id_an FROM parlementaire INTO OUTFILE '/var/export_2017_2022_parl.csv' FIELDS TERMINATED BY '~' LINES TERMINATED BY '\n';

## Contributing

We welcome contributions from the community! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

