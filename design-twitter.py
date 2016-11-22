'''
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followships = {}
        self.user_tweets = {}
        self.tweets = {}
        self.tweet_time_tick = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweet_time_tick += 1
        self.tweets[tweetId] = self.tweet_time_tick
        if userId in self.user_tweets:
            self.user_tweets[userId].append(tweetId)
        else:
            self.user_tweets[userId] = [tweetId]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        source = []
        for uid in self.followships.get(userId, {}).keys() + [userId]:
            tweets = self.user_tweets.get(uid)
            if tweets:
                source.append(tweets)

        n = len(source)
        left = n
        p = [len(t) - 1 for t in source]
        feed = []
        while len(feed) < 10 and left > 0:
            max_t = k = tid = -1
            for i in xrange(n):
                if p[i] >= 0 and self.tweets[source[i][p[i]]] > max_t:
                    max_t = self.tweets[source[i][p[i]]]
                    k = i
                    tid = source[i][p[i]]
            p[k] -= 1
            if p[k] < 0:
                left -= 1
            feed.append(tid)
        return feed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId in self.followships:
            self.followships[followerId][followeeId] = True
        else:
            self.followships[followerId] = {followeeId: True}

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followships:
            self.followships[followerId].pop(followeeId, None)


if __name__ == '__main__':
    t = Twitter()
    t.postTweet(1, 5)
    t.postTweet(1, 3)
    assert t.getNewsFeed(1) == [3, 5]
    t.follow(1, 2)
    t.postTweet(2, 1)
    assert t.getNewsFeed(1) == [1, 3, 5]
    t.unfollow(1, 3)
