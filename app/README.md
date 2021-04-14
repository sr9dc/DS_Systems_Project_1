# Dockerized Discord Lyric Bot
<!--
*** Thanks for checking out my Discord Lyric bot. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
-->

### Built With

* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)

* Python Packages- see requirements.txt in ./app/ Folder.

* The API used is [Lyrics.ovh](https://lyrics.ovh/), and the API documentation is freely available on [Apiary.io](http://docs.lyricsovh.apiary.io/). 

<!-- GETTING STARTED -->
## About

The Lyric Bot is a dockerized Python3 application that can be run interactively, taking an artist and song parameter to retrieve remote lyrics data. 

When the user manually inputs a Discord API key URL in the console, the chosen song's lyrics will be posted into the channel corresponding to the key. The output to the Discord channel is a success message, a text file with the lyrics, and an embed figure with the artist and song name requested. 

There are 5 options for the user to choose, which have corresponding error checks to ensure input validation.
(1) View the README.
(2) Submit a Lyric Request. 
(3) View your Lyric Requests. 
(help) See this screen again. 
(exit) Exit the app. 

If (1) is chosen, this current README page will be printed out using the Python rich package print() method. 

If (2) is chosen, an input prompt will be generated, with the Discord Webhook URL, Artist, and Song name inputs. The URL will be error checked for link syntax, which uses the open-source Django regular expressions in url_validator.py to ensure the formatting is correct. Additionally, the Webhook must have a Discord.com hostname. If the incorrect Webhook is provided, it will be error checked on response errors. If the response status is not 200, then an error message will be displayed, causing the input prompt to restart. Upon a successful run, the Lyric, Artist and Song data will sent to the Discord channel, and will be stored in a rich table, viewable via option (3). Once user exits the program, all the data inputted is cleared. 

If (3) is chosen, all successful Artist and Song requests will be tabulated corresponding to the time, using the python time package. Therefore, the 3 columns are Time, Artist, and Song. With no requests, an empty table will be generated. 

If (help) is chosen, the options list will be shown once again after the initial run. 

If (exit) is chosen , the kernel application will exit. 


As mentioned in the third option (3), at the end of the run no data is saved, which ensures that the security of the Discord channel is maintained. 


<!-- GETTING STARTED -->
## Getting Started

You can use the pull command to install the Docker image from Docker Hub. 
```
docker pull sairajulad/python-lyricbot
```

Use the images command to list all your local images. Here you should see the pulled docker repository. 
```
docker images
```

Run the command below to get the Discord Lyric Bot working correctly. Make sure to specify the keyword '-it' to ensure that the code runs interactively. 
```
docker run -it sairajulad/python-lyricbot
```

From here, you will be guided to a prompt where you can submit lyric requests and view any successful requests.

Make sure to have your Discord API Key URL on hand- it is an important input for submitting a Lyric Request!

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Sai Rajuladevi: https://www.linkedin.com/in/sai-rajuladevi/

Project Link: [https://github.com/sr9dc/DS_Systems_Project_1](https://github.com/sr9dc/DS_KNN_Lab_Group_6)
