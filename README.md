## Rap City
Real time rap lyric generator  (*based on the original "rap-app"*) 


##### How it works
1. Receives rap lyric input from the user using speech recognition
2. Analyzes the input and searches for a word that rhymes with the previous line
3. Outputs lyric that rhymes with the user's input to mimic intelligent "freestyle"


##### Word bank, Rhymes, and Lyrics
The primary word bank was compiled from [The Moby Project](https://en.wikipedia.org/wiki/Moby_Project), a phonetic database of 177,267 words and their corresponding IPA notations. The word bank was first filtered using a comparison with the 2009 edition of Webster's Unabridged Dictionary. *The word bank was then filtered with a [list](http://www.wordfrequency.info) of 5000 common words in order to increase relevance and speedup each rhyme-query. The lyrics used to respond are generated from a compilation of 90,000+ lines of lyrics scraped from [Rap Genius](http://rap.genius.com/). The artists who collectively wrote the lyrics that make up Rap-City's database are: Kanye West, Eminem, The Wu-Tang Clan, J. Cole, Drake, and Kendrick Lamar.  


##### History
Rap City is a continuation of "the-rap-app" -- a hackathon project [*Cal Hacks, October 2015*] created by three UC Berkeley students: [Sam Choi](https://github.com/canibringmycat), [Owen Jow](https://github.com/ohjay), and [Sagang Wee](https://github.com/sagangwee). the-rap-app was able to respond to a user's sentence with a word that rhymed with the last syllable of said sentence. Rap City aims to further develop the-rap-app's functionalities to enable full sentence rhyming-responses to a user's lyrics. Thus, Rap City is an attempt to improve on the-rap-app to create the perfect freestyle-rap partner.  
*the original project can be found at: https://github.com/ohjay/the-rap-app*