#!/usr/bin/env python
from typing import List
from collections import deque

import heapq

class User:
    def __init__(self, uid: int):
        self.uid = uid
        self.follows = set()
        self.posts = deque()

    def addFollow(self, uid: int) -> None:
        self.follows.add(uid)

    def rmFollow(self, uid: int) -> None:
        self.follows.remove(uid)

    def addPost(self, postId: int, postTime: int) -> None:
        if len(self.posts) == 10:    # 因为最多就10个posts，所以超过10时，老的那些直接扔掉
            self.posts.popleft()
        self.posts.append((-postTime, postId))    # 为了方便后面能通过堆选出Top10，这里维护负时间

class Twitter:

    def __init__(self):
        self.globalTime = 0
        self.users = {}

    def _getUser(self, userId: int) -> User:
        # 为了避免测试数据中的一些沙比case，这个类中获取某个user统一通过这个方法
        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._getUser(userId)
        user.addPost(tweetId, self.globalTime)
        self.globalTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        这个方法逻辑并不复杂，就是把本人以及本人关注的所有人的posts都拿出来合并
        然后建立堆序，从中pop出10个来就好了
        '''
        if userId not in self.users: return []
        posts = []
        user = self._getUser(userId)
        posts.extend(list(user.posts))
        for f in user.follows:
            posts.extend(list(self.users[f].posts))

        heapq.heapify(posts)

        ans = []
        while len(posts) > 0 and len(ans) < 10:
            _, post_id = heapq.heappop(posts)
            ans.append(post_id)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        a, b = followerId, followeeId
        user_a = self._getUser(a)
        user_b = self._getUser(b)    # 这句其实可以没有
        user_a.addFollow(b)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        a, b = followerId, followeeId
        user_a = self.users[a]
        if b in user_a.follows:
            user_a.rmFollow(b)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)