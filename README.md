# VideoSummary

In response to the Corona Virus Outbreak, we realized that there is a lot of information available on the internet and many of which are available in a video format but little to no ways of comiling all this information without having to watch all these videos which can both be time-consuming and mentally-straining. To solve this problem, we came up with 'Recap This Vid For Me' which takes a YouTube video link and utilizes Google's video intelligence API to transcribe the video into text and implements a unsupervised natural language processing algorithm, text rank, to summarize the key elements in the video by recognizing the most common sentences/ words.

# How we built it?

We built this project using HTML, CSS and vanilla JS for the front-end with a python3 backend consisting of aiohttp for the async API calls, numpy and the Natural Language ToolKit (NLTK) for the natural language processing, and Networkx for graphical computation combined with pytube and the Google Cloud Video Intelligence API for transcribing the videos. Our backend is currently hosted in a completely serverless environment using Google Cloud - namely, using cloud functions, pub/sub and cloud storage.

# What's next?

In the future, we hope to add a feature using Pandas where we can parse different sources for videos just from a key-word and rather than having the users enter an URL, they can enter a keyword and we can summarize the data from all these sources. 

# Try it Out
[CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426)
You can try out our project on here: http://www.recapthisvid.tech/. To compile our backend and experiment with our API, clone our project and follow the following steps:

## Installation Instructions
```
1) Open your command prompt
2) Install python by following the instructions on [here](https://wiki.python.org/moin/BeginnersGuide/Download) and install a virtual environment
3) Open your command prompt 
4) Navigate into our project by using cd RecapThisVideo
5) Type 'cd Backend'
6) Type 'pip install -r requirements.txt'
7) Create a [google cloud service key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-gcloud) and set it in your environment 
```

## Build and Run
```
1) Type 'python AsyncSetUp.py' by navigating to the backend of our project in your command prompt to run our API 
2) To only run the Video Transcriptions and Natural Language Processing scripts, type 'python VideoIntelligence.py' 
3) To only run the SendGrid script for sending out the results, type 'python SendResults.py' 
```
To find our serverless implementation, you can navigate to the following forked repository: https://github.com/StanfordLin/RecapThisVid.
