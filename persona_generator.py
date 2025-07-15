import openai

# ✅ Set your OpenAI API key
client = openai.OpenAI(api_key="OPENAI_API_KEY")

# ✅ Read data
with open("persona_output.txt", "r", encoding="utf-8") as file:
    reddit_data = file.read()

prompt = f"""You are a helpful AI assistant.
Given the following Reddit posts and comments from a user, analyze and generate a detailed user persona with proper formatting.
For each personality trait, interest, or behavioral pattern you detect, provide a brief explanation and cite the exact post or comment that supports it.

Reddit Data:
{reddit_data}

Output Format:
User Persona:
- Interests: (Explain and cite examples)
- Tone/Writing Style:
- Favorite Subreddits:
- Other Observations:
"""

# ✅ Call OpenAI API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert Reddit user persona analyst."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

persona_summary = response.choices[0].message.content

# ✅ Save result
with open("persona_summary.txt", "w", encoding="utf-8") as output_file:
    output_file.write(persona_summary)

print("✅ User Persona summary saved to persona_summary.txt")
