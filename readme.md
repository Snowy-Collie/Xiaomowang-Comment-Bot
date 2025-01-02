# Xiaomawang Comment Bot

This project is a web automation tool that uses Selenium to interact with a website, perform login operations, and send messages to specified project pages.

## Project Structure

```
.gitignore

main.py
```

- `.gitignore`: Specifies files to be ignored by git.
- `main.py`: Main script to perform login and send messages using Selenium.

## Prerequisites

- Python 3.x
- Microsoft Edge browser
- Edge WebDriver (msedgedriver.exe) placed in the same directory as the Python scripts.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Snowy-Collie/Xiaomowang-Comment-Bot.git
    cd Xiaomowang-Comment-Bot
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium requests
    ```

3. Download webdriver:
    Go to website https://developer.microsoft.com/microsoft-edge/tools/webdriver/ and download.

## Usage

1. Run the main.py script:
    ```sh
    python main.py
    ```

2. Follow the prompts to enter your login credentials, message content, and other details.

## Functions

### login()
Performs the login operation and saves cookies to cookies.json

### load_cookies_and_navigate()
Loads cookies from cookies.json and navigates to the target page.

### send_message(content, project_id)
Sends a message to the specified project page.

## Disclaimer

This tool is for educational and communication purposes only. Do not use it for illegal activities. The author is not responsible for any issues arising from the use of this tool.

## License

This project is licensed under the MIT License.