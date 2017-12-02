# Bet365 Odds Parser
## Usage
- Navigate to https://mobile.bet365.com on a desktop web browser
- Set odds to your preference (Fractional, Decimal, American) by scrolling to the bottom of the page and clicking preferences, for programmatic use decimal probably makes more sense
- Click on Soccer
- Click on a category/league you want to get odds for (eg. Elite Euro List, English Premier League etc.)
- Wait until page fully loads
- Right click anywhere, click inspect, right click the top most html tag, click copy outer html
- Open a text editor, paste in the html and save this file
- Run `parser.py` and pass in the html file as an argument
- `python parser.py elite_euro_list.html`
- A `.json` file will be output in the same directory as the html file

## Example data
- See `example_data` folder

## Limitations
- This script is not able to automatically scrape html from Bet365, I have tried this briefly using PhantomJS, CasperJS and Bet365 caught on and temporarily blocked my IP address from accessing their site.
So this is not something I will spend time looking into. If you find a way to do it without getting blocked out let me know :P
- Currently only compatible with Python 2
- Currently only parsing football odds is supported
- This script is easily extensible to other sports (Tennis, Horse racing, etc.) and if/when I have time I will update it

## Contributions
- Feel free to fork this and fix issues, add support for other sports, if you do open a PR and I'll check it out
