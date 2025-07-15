import praw

# Replace with your own Reddit API credentials
client_id = "fKrKCu_LIUNgeUpPHeZC7w"
client_secret = "opQGPUE0OX6khCnQrEu4Gn4gS0NmmA"
user_agent = "MyPersonaScript/0.1 by u/Character_Isopod1190"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

username = "kojied"  # Reddit user to scrape
redditor = reddit.redditor(username)

# Open file to write output
with open("persona_output.txt", "w", encoding="utf-8") as file:
    file.write(f"Reddit User Persona: u/{username}\n\n")

    file.write("Recent Posts:\n")
    for post in redditor.submissions.new(limit=5):
        file.write(f"Title: {post.title}\n")
        file.write(f"Subreddit: {post.subreddit}\n")
        file.write(f"URL: {post.url}\n\n")

    file.write("Recent Comments:\n")
    for comment in redditor.comments.new(limit=5):
        file.write(f"Comment: {comment.body}\n")
        file.write(f"Subreddit: {comment.subreddit}\n\n")

print("✅ Data saved to persona_output.txt")
