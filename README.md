# ZafBot

A generic price monitoring application built with Python. ZafBot allows users to monitor product prices from websites using customizable URLs and CSS selectors.

## Features

- Automatic product price monitoring.
- Custom CSS selectors for price extraction.
- Command-line interface (CLI).
- Graphical user interface (GUI).
- SQLite database for product storage.
- Discord webhook notifications.
- Chrome and Microsoft Edge support.

## Downloads

Precompiled executables are available in [GitHub Releases](https://github.com/zlxz-ok/ZafBot/releases).

ZafBot provides two application versions:

- **v0.x.x — CLI:** Command-line interface.
- **v1.x.x — GUI:** Graphical desktop interface.

Choose the version that suits your needs. Each release provides the available executables for Linux and Windows.

## Technologies

- Python
- Selenium
- BeautifulSoup4
- CustomTkinter
- SQLite
- Discord Webhooks

## Requirements

- Python 3.10 or newer
- Google Chrome or Microsoft Edge
- Internet connection

## Installation from source

Clone the repository:

```bash
git clone https://github.com/zlxz-ok/ZafBot.git
cd ZafBot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Configuration

ZafBot allows users to configure:

- Product URLs.
- CSS selectors used to locate prices.
- Discord webhook notifications.
- Monitoring intervals.

Users are responsible for providing valid URLs and CSS selectors.
## Contact

Have questions, suggestions, or feedback about ZafBot?

Discord: zlxz__

For bug reports or feature requests, feel free to open a GitHub Issue.

## Disclaimer

ZafBot is an independent, generic price monitoring tool.

Users are responsible for ensuring that their use of the software complies with applicable laws and the terms of service of the websites they access.

The developers do not endorse or guarantee compatibility with any particular website.

ZafBot does not guarantee uninterrupted access to third-party websites or accurate price extraction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
