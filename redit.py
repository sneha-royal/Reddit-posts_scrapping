import praw
import pandas as pd
from datetime import datetime
# Initialize Reddit instance
reddit = praw.Reddit(
    client_id='Ge1wVw_HubOz6qcq0kZ2CA',
    client_secret='XEEH7KJ9bR55ET_qt1CPEUjugkNEMA',
    user_agent='MyScraper'
)
# Function to convert Unix timestamp to a human-readable format
def convert_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
# Specify the subreddit and the number of posts to scrape
subreddit_name = input("Enter the name of the subreddit: ")
try:
    subreddit = reddit.subreddit(subreddit_name)
    post_limit = int(input("Number of posts to scrape: "))
    if post_limit <= 0:
        raise ValueError("Number of posts must be greater than zero.")
    # Scrape data from the subreddit
    posts = subreddit.top(limit=post_limit)
    # Create a list to store the data
    data = []
    # Fetch the top posts dynamically
    for i, submission in enumerate(posts, start=1):
        data.append({
            "Title": submission.title,
            "Score": submission.score,
            "ID": submission.id,
            "URL": submission.url,
            "Comments Count": submission.num_comments,
            "Created": convert_time(submission.created_utc),
            "Description": submission.selftext
        })
        # Print progress every 10 posts
        if i % 10 == 0:
            print(f"{i} posts processed...")
    # Convert the list of data into a DataFrame after all posts are processed
    df = pd.DataFrame(data)
    # Save the DataFrame to an Excel file
    excel_filename = f"{subreddit_name}.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Data saved to {excel_filename}")
except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
