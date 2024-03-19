
# Student Accommodation Clustering Project

This project aims to help students find the best accommodation by clustering accommodations based on their amenities, budget, and proximity to preferred locations.

## Overview

In this project, we utilize data analysis and machine learning techniques to classify accommodations and suggest suitable options for students based on their preferences. The project involves data collection, preprocessing, clustering, and visualization.

## Project Structure
```
project_name/
│
├── data/ # Folder for storing raw and processed data
│ ├── raw/ # Raw data files
│ ├── processed/ # Processed data files
│
├── notebooks/ # Jupyter notebooks for data analysis and visualization
│ ├── 1_preprocessing.ipynb
│ ├── 2_clustering_population.ipynb
│ ├── 3_fetch_location_data.ipynb
│ ├── 4_clustering_locations.ipynb
│ └── 5_plot_map.ipynb
│
├── src/ # Source code for data processing, clustering, and visualization
│ ├── api/ # Modules for interacting with APIs
│ │ └── foursquare.py # Module for Foursquare API interaction
│ ├── visualization/ # Modules for creating visualizations
│ │ ├── map_plotter.py # Module for plotting maps
│ │ └── map.html # HTML file for viewing maps
│
├── venv/ # Python virtual environment
├── .gitignore # Specify files and directories to be ignored by version control
├── .env # File containing API keys (e.g., FOURSQUARE_API_KEY)
├── .env.sample # Sample file for .env, should be renamed and filled with actual FOURSQUARE API key
└── README.md # Project documentation

```

## Installation

1. Clone the repository:
```
git clone https://github.com/BlcMed/student-housing-clustering.git
```

1. Navigate to the project directory:
```
cd student-housing-clustering
```

3. Set up a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. **Setup API Keys:**
- Rename `.env.sample` to `.env`.
- Add your FOURSQUARE_API_KEY to the `.env` file.

2. **Run Jupyter notebooks:**

- Execute the notebooks in the `notebooks` directory in sequential order.

- Follow the instructions in each notebook to perform data analysis, clustering, and visualization.

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
