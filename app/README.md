# Lyric Bot

The Lyric Bot is a dockerized Python3 application that can be run interactively, taking an artist and song parameter to retrieve remote lyrics data. 

When the user manually inputs a Discord API key URL in the console, the chosen song's lyrics will be posted into the channel corresponding to the key.

At the end of the run, no data is saved, which ensures that the security of the discord channel is maintained. 

The API used is [Lyrics.ovh](https://lyrics.ovh/), and the API documentation is available on [Apiary.io](http://docs.lyricsovh.apiary.io/.)


## How to start

Install with `pip` or your favorite PyPi package manager.

```
pip install rich
```

Run the following to test Rich output on your terminal:

```
python -m rich
```