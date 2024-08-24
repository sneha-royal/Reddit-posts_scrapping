# Reddit Subreddit Scraper

This Python script allows you to scrape the top posts from a specified subreddit using the Reddit API via the `praw` library. The collected data includes the post title, score, ID, URL, number of comments, creation date, and description. The data is then saved to an Excel file for further analysis.

## Features

- Scrape top posts from any subreddit.
- Collect post details including title, score, comments count, and more.
- Save the scraped data into an Excel file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `praw` library
- `pandas` library
- `openpyxl` library

You can install the required Python packages using pip:

```bash
pip install praw pandas openpyxl


Setup
1.Clone the Repository

git clone https://github.com/sneha-royal/Reddit-posts_scrapping.git
cd Reddit-posts_scrapping

2.Configure Reddit API Credentials

You need to have a Reddit account and create a Reddit app to get your client_id, client_secret, and user_agent. Set these in the script as follows:

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)

3.Run the Script

Execute the script by running:

python redit.py
You will be prompted to enter the subreddit name and the number of top posts you wish to scrape.

4.Usage
Enter the Subreddit Name: Input the name of the subreddit from which you want to scrape posts (e.g., python, technology).

Specify the Number of Posts: Enter the number of top posts you want to scrape. Ensure the number is greater than zero.

View Progress: The script will show progress every 10 posts processed.

Output: The scraped data will be saved in an Excel file named after the subreddit (e.g., python.xlsx).

Example
For example, if you want to scrape the top 50 posts from the python subreddit, you would input:
Enter the name of the subreddit: python
Number of posts to scrape: 50
After running the script, you will find a file named python.xlsx in the script's directory containing the scraped data.

Error Handling
The script includes basic error handling:

If you enter an invalid number of posts (e.g., a negative number or zero), the script will raise a ValueError.
If any other error occurs during execution, the script will display an error message.
