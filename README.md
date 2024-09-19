# VakilDesk Technical Assessment Solution

## Overview

This repository contains a solution for the VakilDesk Technical Assessment. 

## Getting Started

To get started with this project, follow the instructions below:

### Clone the Repository

First, clone the repository using the following command:

```bash
git clone https://github.com/Shivamchaubey14/Vakildesk_Technical_Assessment_Solution.git
```
### 1. Web Scraping Latest Articles
### Navigate to the Project Directory

Change your directory to the `Web Scraping Latest Articles` folder:

```bash
cd Vakildesk_Technical_Assessment_Solution/Web Scraping Latest Articles
```

### Install Dependencies

Before running the `scraper.py` file, you need to install the required Python libraries. Use the following command to install them:

```bash
pip install requests beautifulsoup4
```

### Running the Web Scraping Script

You can now run the `scraper.py` script using the following command:

```bash
python scraper.py
```

This will execute the web scraping script and fetch the latest articles as defined in the `scraper.py` file.
### 2. Clean CSV User Data
### Navigate to the Clean CSV User Data Directory

Change your directory to the `Clean CSV User Data` folder:

```bash
cd ../Clean CSV User Data
```

### Install Dependencies for CSV Cleaning

Ensure you have the required Python libraries for CSV processing. These libraries should be included with Python, so no additional installation is usually necessary.

### Running the CSV Cleaning Script

To clean the CSV user data, run the `clean_csv_user_data.py` script using the following command:

```bash
python clean_csv_user_data.py
```

This script will read `user.csv`, filter out invalid emails and duplicate `user_id`s, and write the cleaned data to `cleaned_users.csv`.

### 3. Django Query for Top 5 Customers

#### Navigate to the Django Query Directory

Change your directory to the `Django Query for Top 5 Customers` folder:

```bash
cd ../Django Query for Top 5 Customers
```

#### Install Dependencies

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

> **Note:** A virtual environment was not created for this lightweight project, so installation happens directly.

#### Running the Django Server

To start the Django server, run the following command:

```bash
python manage.py runserver
```

Once the server is running, visit [http://127.0.0.1:8000/orders/top-customers/](http://127.0.0.1:8000/orders/top-customers/) in your browser to view the list of the top 5 customers who have spent the most in the last 6 months.

### 4. Rate Limiter

#### Navigate to the Rate Limiter Directory

Change your directory to the `Rate Limiter` folder:

```bash
cd ../Rate Limiter
```

#### Running the Rate Limiter Script

To run the rate limiter script, use the following command:

```bash
python rateLimiter.py
```

This will execute the `rateLimiter.py` script, which demonstrates the functionality of the rate limiter implementation.

---

### 5. Aggregate Dictionary Data

#### Navigate to the Aggregate Dictionary Data Directory

Change your directory to the `Aggregate Dictionary Data` folder:

```bash
cd ../Aggregate Dictionary Data
```

#### Running the Aggregation Script

To run the aggregation script, use the following command:

```bash
python aggregate.py
```

This will execute the `aggregate.py` script, and the result of the data aggregation will be displayed in the console.

---

### 6. Finding Duplicacy

#### Navigate to the Finding Duplicacy Directory

Change your directory to the `FindingDuplicacy` folder:

```bash
cd ../FindingDuplicacy
```

#### Running the Duplicacy Finder Script

To run the script that finds duplicates in an array, use the following command:

```bash
python find_duplicacy.py
```

This will execute the `find_duplicacy.py` script, and the result will be displayed in the console.

---

## Contact

For any questions or comments, please contact me at [shivamchaubey1412@gmail.com](mailto:shivamchaubey1412@gmail.com).
```
