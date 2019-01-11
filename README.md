# Final Project Proposal
Today, it’s difficult to imagine the fight against the rise of police brutality against people of color without the Black Lives Matter movement. Yet the movement is only four years old, and it all started with a simple hashtag. The hashtag 'blacklivesmatter' spread over the country quickly after it appeared in early July of 2013. 
With this project, I plan to inquire into how the hashtag spread geographically. In the times before the internet and telephone, the spread of information was geographically trackable as it relied on physical means to be tranferred. The black lives matter hashtag and the information it conveys, on the other hand, can be seen instantly by anyone in the world. I'm wondering whether there's a pseudogeographical spread of information despite this fact.
This project is interesting to me because it provides understanding of how information is spread today. I am fascianted by how knowledge transfer has changed with social media. With this inquiry, I will be able to come to a deeper understanding of the nature of that transfer. 
I hypothesize that a certain twitter user will follow more other users that live close to them than very far away. Thus, as one user tweets using the #blacklivesmatter hashtag, his or her followers who live nearby will see it and potentially use it, which would result in an information spread resembling word-of-mouth. 
To test this hypothesis, I will design a program that plots points representing tweets using the black lives matter hashtag on a map of the US. The earliest occuring hashtag instance will be blue, and the points will become more and more red as more are plotted, creating a chronological gradient. This map will display how, geographically, the hashtag spread. 

## Data Plan
*Summarize data sources, data formats, and how to obtain or generate the data you will be using*
I will be pulling tweet data through an API I found on github called GetOldTweets. Using this API, I’ll be able to call for tweet data by hashtag over a specified range of time. This data will be in csv file form. The user will be able to specify the range of time they want, and the maximum number of tweets. 
	I will then pull latitude/longitude data from this csv file using code I will write in get_tweets.py. The coordinate data will be in csv file format as well. This file will contain the coordinates that will be plotted onto a map of the US, each representing a tweet.   
## Implementation Plan
*Overview of you plan. Are you starting from existing code? What skills from the course will be be using to complete your project? etc.*

### External Libraries
- geopy
- pillow
- pyquery
- requests

### Milestones
- Pulls tweets from twitter matching query '#blacklivesmatter' into csv file
- Pulls locations from tweets in csv file into another csv file
- Determines coordinates from locations in csv file, writes these coordinates into a csv file
- Plots coordinates from csv file onto map of USA, with changing gradient


## Deliverables
- Map of US with gradient plotted points representing hashtag usage instances

# Final Project Report
One of the biggest challenges I faced with this project was in pulling old tweets by hashtag. The official Twitter API only allows pulling tweets that are at most a week old. The GetOldTweets API was the only option I could find for bypassing this restriction. GetOldTweets had numerous errors that I had to correct. After I corrected the errors, I found that I couldn't do a querysearch on my computer. I spent a long time trying to get to the root of the error in lxml. My efforts were fruitless, and I later learned that it was only due to the version of lmxl on my computer and that I could run data pulls from my lab computer instead. The process of getting the GetOldTweets API to work drained a lot of my time on this project as I couldn't really get started on my coding until the API was successfully pulling tweets by querysearch.

After I got the API working, coding went without great challenge. The main challenge was getting a data pull on a range of time in which the hashtag was spreading. As I progressed, I learned that the 'blacklivesmatter' hashtag did not spread to its full audience in a predictable manner over time. It was created in July of 2013, but much of the tweet volume comes from the summer of 2014. Further, the hashtag usage tends to spike around news events and high profile instances of police brutality. This makes it a bit more difficult to capture the range of time in which the hashtag is growing and becoming known to people becuase the process is so long and inconsistent. The output shown in the repository does not appear to support my hypothesis of the hashtag spread being pseudo-geographical. Rather, the absence of a clear gradient indicates that location and distance has virtually no bearing on the transfer of information and ideas around the country. The dynamics of information spread of the days without internet are more different than they are today than I thought.

I achieved what I wanted to with this program in that I was able to determine whether spread of ideas and knowledge on twitter resembles word-of-mouth transfer in its geographical spreading pattern. Based on the data I used, no such resemblence exists. In conclusion, though, I am not completely confident about that result due to the inconsistency of the blacklivesmatter hashtag. I believe that with a more precise data range targeting a known period of hashtag growth or the use of a different hashtag with a faster and more consistent growth period would yield a map that would be more expository of the nature of the spread of ideas in a social media context.

## Instructions to run the code

cd into old_tweets, then into my_GetOldTweets. From there, if you want to run your own data pulls, which take a while and only work on computers with a certain version of lmxl, import the module geopy into your environment and run the following:
    "python Exporter.py --searchquery "#blacklivesmatter" --since 2013-07-13 --until 2013-09-13"

If you don't want to run your own data pulls, I have provided the geo data from the tweets obtained in the data pull outlined above in the file tweet_coords.csv. 
To create your image, import pillow into your environment and run 
    "python3 exec.py tweet_coords.csv US-states.csv output.png 1024"
The arguments follow the form:
    "tweet coordinate data source, boundary data source [for generating the map of the US], desired output filename, width of image"
This will generate an image at the filename specified. 
    
