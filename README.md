# Jami Chat Bot

A Telegram chatbot powered by OpenAI's GPT model. This bot allows users to have conversational interactions with an AI assistant directly through Telegram.

## Features

- **AI-Powered Conversations**: Utilizes OpenAI's GPT model for intelligent responses.
- **Conversation Memory**: Maintains context within a conversation session.
- **Easy Commands**: Simple commands to control the bot interaction.
- **Privacy Focused**: Uses environment variables to secure API keys.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Telegram Bot Token (from [BotFather](https://t.me/BotFather))
- OpenAI API Key (from [OpenAI Platform](https://platform.openai.com))

### Installation

1. Clone or download this repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory with your API keys:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

## Usage

### Available Commands

- `/start` - Initialize the bot and receive a welcome message
- `/help` - Display help information and available commands
- `/clear` - Clear the conversation history and context
- Send any text message to chat with the AI assistant

### How It Works

1. The bot maintains conversation context using a reference class
2. Each message you send is processed by OpenAI's GPT model
3. Responses are sent back to you in the Telegram chat
4. Use `/clear` to reset the conversation when needed

## Configuration

The bot currently uses the GPT-5 model (as specified in the code). You can modify the `model_name` variable to use different OpenAI models if needed.

## Note

This bot was created for learning purpose. Make sure to comply with both Telegram's and OpenAI's terms of service when using this application.

## Troubleshooting

- Ensure all environment variables are properly set in the `.env` file.
- Verify that both API keys are valid and have sufficient credits.
- Check that your Python environment has all required dependencies installed.

## License

This project is for demonstration purposes. Please ensure proper usage of both Telegram and OpenAI APIs according to their respective terms of service.