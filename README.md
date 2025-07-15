# reddit-user-persona

Reddit User Persona Generator
📌 Project Overview
This project scrapes posts and comments from any Reddit user profile and generates a User Persona summarizing their interests, behavior, and activity.
Assignment Goal: Build a system that takes a Reddit user profile and outputs a structured persona based on their Reddit activity.

🖥️ Folder Structure
graphql
Copy
Edit
reddit-user-persona/
├── persona_scraper.py          # Script to scrape Reddit posts & comments
├── persona_output.txt          # Sample Reddit data scraped
├── persona_generator.py        # (Optional) Script to generate persona using OpenAI API (requires API key)
├── requirements.txt            # List of dependencies
├── .gitignore                  # Files to ignore in git
└── README.md                   # This file
✅ Features
Scrape Reddit posts & comments using Reddit API.

Generate a User Persona from the scraped data.

(Optional) Use OpenAI GPT to automatically generate persona summaries (requires API key).
