
# A/B Testing for Marketing Campaign Optimization

## Overview

In this project we evaluate the effectiveness of two marketing strategies (A and B) using A/B testing. We use statistical analysis to determine whether there is a significant difference in conversion rates between the two groups. Python is used for data analysis, and SQL is used to extract the necessary data from the database. Note that since I couldn't find a relevant database from Kaggle, I wrote a script (insert_data.py) to insert synthetic data (randomly generated) to the database. But usually if the data is already available in the company database we can easily load it to the database using python and then extract it to a csv file, and vice versa. We can then do the ab testing and hypothesis testing on the data in the csv file.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, SciPy, Matplotlib
- **Database**: SQLite
- **Version Control**: Git & GitHub

## Project Structure

```
ABTestingCampaignOptimization/
├── data/
│   └── marketing_data.csv                  # Marketing data from SQL
├── scripts/
│   ├── ab_test_setup.py                    # Python script to perform A/B test setup and analysis
│   ├── hypothesis_testing.py               # Python script to perform hypothesis testing
│   └── insert_data.py			             # Inserts data into the data into the database
│   └── extract_data_to_csv.py              # Script to extract data to CSV
├── visualizations/                         # Directory to save the generated plots
│   └── ab_test_results.png                 # Example visualization
├── README.md                               # Documentation
└── requirements.txt                        # Python dependencies
```

## Setup Instructions

### 1. Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Extract the data using Python:

Run the extract_data_to_csv.py to extract data from the database and save it as `marketing_data.csv` in the `data/` directory.

### 3. Perform A/B test setup and analysis:

```bash
python3 scripts/ab_test_setup.py
```

This will display the conversion rates and generate a visualization (`ab_test_results.png`).

### 4. Perform hypothesis testing:

```bash
python3 scripts/hypothesis_testing.py
```

This will perform a t-test to check for statistical significance between the conversion rates of groups A and B.

## Results and Visualizations

The conversion rate comparison between groups A and B is visualized using a bar chart.

## Statistical Analysis

A hypothesis test (t-test) is conducted to determine if the difference between conversion rates is statistically significant.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the code of conduct when contributing.