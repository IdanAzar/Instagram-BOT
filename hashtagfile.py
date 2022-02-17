from random import randint
import random

hash_list = ["animals", "technology", "puppys", "gaming",
             "motivation", "classiccars", "nature", "celebrities",
             "tesla", "stocks", "movies", "gym"]


def create_hashtag_file():
    hashtag_file = open("hashtags.txt", "w")
    for element in hash_list:
        hashtag_file.write(element + "\n")
    hashtag_file.close()


def create_comment_file():
    comment_list = ["damn, loved the post! keep sharing", "fire", "amazing post, love your content!",
                    "well done, keep up with this content", "loved it!, amazing post",
                    "what an amazing photo, keep up with the quality content!", "great photo!",
                    "thats awsome! keep up!"]
    with open("comments.txt", "w") as comment_file:
        for element in comment_list:
            comment_file.write(element + "\n")
        comment_file.close()


def get_hashtag():
    hashtag_file = open("hashtags.txt", "r")
    buffer = hashtag_file.readlines()
    index = random.randint(0, 12)
    return buffer[index]


def get_comment():
    comment_file = open("comments.txt", "r")
    com_temp = comment_file.readlines()
    i = random.randint(0, 7)
    return com_temp[i]
