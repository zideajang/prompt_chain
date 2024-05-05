import random
import json

from rich.console import Console
from local_model import build_ollama_model as ask

console = Console()

def run():

    mock_live_feed = [
        "Our revenue exceeded expectations this quarter, driven by strong sales in our core product lines.",
        "We experienced some supply chain disruptions that impacted our ability to meet customer demand in certain regions.",
        "Our new product launch has been well-received by customers and is contributing significantly to our growth.",
        "We incurred higher than expected costs related to our expansion efforts, which put pressure on our margins.",
        "We are seeing positive trends in customer retention and loyalty, with many customers increasing their spend with us.",
        "The competitive landscape remains challenging, with some competitors engaging in aggressive pricing strategies.",
        "We made significant progress on our sustainability initiatives this quarter, reducing our carbon footprint and waste.",
        "We had to write off some inventory due to changing consumer preferences, which negatively impacted our bottom line.",
    ]

    live_feed = random.choice(mock_live_feed)
    console.print(f"Analyzing Sentiment Of Latest Audio Clip: '{live_feed}'")

    sentiment_analysis_prompt_response = ask("llama3",f"Analyze the sentiment of the following text as either positive or negative: '{live_feed}'. Respond in JSON format {{sentiment: 'positive' | 'negative'}}.")
    sentiment = json.loads(sentiment_analysis_prompt_response.text())["sentiment"]

    def positive_sentiment_action(live_feed):
        positive_sentiment_thesis_prompt_response = ask("llama3",
            f"The following text has a positive sentiment: '{live_feed}'. Generate a short thesis statement about why the sentiment is positive."
        )
        console.print(
            f"\n\nPositive Sentiment Thesis: {positive_sentiment_thesis_prompt_response.text()}"
        )

    def negative_sentiment_action(live_feed):
        negative_sentiment_thesis_prompt_response = ask("llama3",
            f"The following text has a negative sentiment: '{live_feed}'. Generate a short thesis statement about why the sentiment is negative."
        )
        console.print(
            f"\n\nNegative Sentiment Thesis: {negative_sentiment_thesis_prompt_response.text()}\n\n"
        )


    def unknown_sentiment_action(_):
        console.print(
            f"Could not determine sentiment. Raw response: {sentiment_analysis_prompt_response.text()}"
        )

    sentiment_actions = {
        "positive": positive_sentiment_action,
        "negative": negative_sentiment_action,
    }

    sentiment_action = sentiment_actions.get(sentiment, unknown_sentiment_action)

    sentiment_action(live_feed)

if __name__ == "__main__":
    run()