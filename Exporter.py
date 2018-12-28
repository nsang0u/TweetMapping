# -*- coding: utf-8 -*-

import sys
import getopt
import got3
import datetime
import codecs


def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return


	if len(argv) == 1 and argv[0] == '-h':
		print("incorrect -nnn")
		return
	outputFile = None
	arg = None

	try:
		opts, args = getopt.getopt(argv, "", ("username=", "since=", "until=", "querysearch=", "toptweets", "maxtweets="))

		tweetCriteria = got3.manager.TweetCriteria()

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg

			elif opt == '--since':
				tweetCriteria.since = arg

			elif opt == '--until':
				tweetCriteria.until = arg

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)


		outputFile = codecs.open("output_got.csv", "w+", "utf-8")

		outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
			outputFile.flush();
			print('More %d saved on file...\n' % len(tweets))

		got3.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except getopt.GetoptError:
		print('Arguments parser error, try -h' + arg)
	finally:
		if outputFile != None:
			outputFile.close()
		print('Done. Output file generated "output_got.csv".')

if __name__ == '__main__':
	main(sys.argv[1:])
