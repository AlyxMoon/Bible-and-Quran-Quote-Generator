# Bible and Quran Verse Generator
This program will pick a random verse from the Bible and Quran and generate an image with the text from both on it, side by side.  
The actual Twitter bot can be found [here](https://twitter.com/SBS_QuranBible).

## Running the program:
1. Ensure that you have some version of Python3 installed (I'm using 3.4.2)
2. Clone the repository to your computer
3. Open the file `env` and fill in the API tokens, then rename the file to `.env`
3. Open a terminal and navigate to where you installed the repository
4. Run `pip install -r requirements.txt`
5. Now run `python bot.py`

If you just want to print to the terminal, run the `example.py` script.

## Why
I'll be honest, I hardly know what's in either one of these texts and I've heard a lot of opinions from people who I don't think have read either one thoroughly either. I want to put them side by side and see if maybe they're not so different from each other after all.

I was inspired by watching the YouTube video [The Holy Quran Experiment](https://youtu.be/zEnWw_lH4tQ)

## Data Sources
The data for the Bible was downloaded from [here](https://github.com/honza/bibles). It is the English Standard Version.

The data for the Quran was downloaded from [here](http://destroyblackmagic.com/quran-data-in-different-languages-json/). It is the English translation by A.J. Arberry.

The font used is Antonio, downloaded from [FontSquirrel](https://www.fontsquirrel.com/).

The background image was made by E. van Zummeren, downloaded from [Toptal](https://www.toptal.com/designers/subtlepatterns/black-felt).