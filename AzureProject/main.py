import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import os

# OpenAI Azure Configuration
openai.api_type = "azure"
openai.api_base = "https://da-openai-pretamoira.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "df8e0d08474149098e310ec714f7f805"

# Extract transcript from a YouTube video
def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

# Summarize text using Azure OpenAI
def summarize_text(text):
    response = openai.Completion.create(
        engine="GPT35TURBO",
        prompt=f"Summarize, explain keypoints: {text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    root = ThemedTk(theme="arc")  # Setting a modern theme using ttkthemes
    root.title("YouTube Video Summarizer")
    root.geometry("800x600")

    def summarize():
        try:
            video_url = video_input.get()
            if "youtube.com" in video_url:
                video_id = video_url.split("v=")[1].split("&")[0]
            else:
                video_id = video_url

            transcript = get_transcript(video_id)
            full_text = " ".join([entry["text"] for entry in transcript])
            summary = summarize_text(full_text)

            output.delete(1.0, tk.END)
            output.insert(tk.END, summary)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # UI Components
    label = ttk.Label(root, text="Enter YouTube Video URL or ID:", font=('Arial', 14))
    label.pack(pady=20)
    video_input = ttk.Entry(root, font=('Arial', 12), width=60)
    video_input.pack(pady=20)
    summarize_btn = ttk.Button(root, text="Summarize", command=summarize)

    summarize_btn.pack(pady=40)
    label_output = ttk.Label(root, text="Summary:", font=('Arial', 14))
    label_output.pack(pady=20)
    output = tk.Text(root, font=('Arial', 12), width=70, height=10, bg='#f5f5f5', fg='#333')
    output.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()