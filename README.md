```markdown
# VakilDesk Technical Assessment Solution

## Overview

This repository contains a solution for the VakilDesk Technical Assessment. It includes a web scraping script to fetch the latest articles and a script for cleaning user data from a CSV file.

## Getting Started

To get started with this project, follow the instructions below:

### Clone the Repository

First, clone the repository using the following command:

```bash
git clone https://github.com/Shivamchaubey14/Vakildesk_Technical_Assessment_Solution.git
```

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or comments, please contact me at [shivamchaubey1412@gmail.com](mailto:shivamchaubey1412@gmail.com).
```