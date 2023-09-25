# **Telegram ChatGPT Bot**
By Grigorian's Tech Academy

📺 **Grigorian's Tech Academy** is a YouTube channel dedicated to educating aspiring developers in full-stack Python, Django, JavaScript, React, and more! For comprehensive tutorials on the latest technologies, don't forget to [subscribe](https://www.youtube.com/@GrigoriansTechAcademy)!

## **Description**:
This project integrates ChatGPT with Telegram to create a powerful AI chatbot. Using Python, you can seamlessly communicate with the ChatGPT model and obtain intelligent, context-aware responses to your queries on Telegram.

[View tutorial](https://youtu.be/JBlc7qQUHuw)

## **Pre-requisites**:
1. Python 3.x
2. An OpenAI account to get the API key
3. A Telegram account and the BotFather to generate a bot token

## **Setup & Installation**:

1. **Clone the repository**:
    ```
    git clone https://github.com/Grigorian-s-Tech-Academy/python-telegram-chatgpt-bot.git
    ```

2. **Navigate to the project directory**:
    ```
    cd python-telegram-chatgpt-bot
    ```

3. **Install required dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    You will need to set up two environment variables: `OPENAI_API_KEY` and `TELEGRAM_BOT_KEY`.
    - `OPENAI_API_KEY`: Your OpenAI GPT-4 API Key.
    - `TELEGRAM_BOT_KEY`: The token for your Telegram bot.

    You can set these using:
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export TELEGRAM_BOT_KEY='your_telegram_bot_key'
    ```

    For a more permanent solution, you can also add these lines to your `.bashrc` or `.zshrc` file.

5. **Run the bot**:
    ```
    python main.py
    ```

## **Usage**:
After setting up, just start a conversation with your Telegram bot. Type in a message, and wait for the bot to reply using the intelligence of ChatGPT!

## **Contribution**:
Feel free to fork the repository and submit pull requests! If you find any issues, please open an issue in the repository.

## **Support**:
For detailed tutorials on the implementation and other tech topics, visit [Grigorian's Tech Academy](https://www.youtube.com/@GrigoriansTechAcademy) on YouTube!
