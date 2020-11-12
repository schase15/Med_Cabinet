## Med Cabinet
#### Heroku and Flask application that uses NLP and KNN to provide Cannabis strain recommendations based on what the user specifies.

This application recieves user input from either a drop down menu or via a text box. The KNN model then returns the 5 most similar cannabis strains from the PostgreSQL database and displays the strain profiles with:
- Strain name
- Strain type
- Strain effects
- Strain flavor
- Overall rating
- Short Description

The original training data used for this KNN model can be found on [Kaggle](https://www.kaggle.com/kingburrito666/cannabis-strains).

The notebook used to build the KNN model can be [here](notebooks/Med_Cabinet_Final.ipynb).

Visit the deployed application [here](https://sc-med-cabinet.herokuapp.com/).

Read more on the accompanying blog post [Med Cabinet: Find Your Strain of Cannabis!](https://steventchase.com/2020-11-12-2020-11-12-med-cabinet/).
