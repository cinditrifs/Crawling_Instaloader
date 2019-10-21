import instaloader
import pandas as pd
from typing import List
import re

captionlist = []
hashtaglist = []
likeslist = []
commentlist = []
followerlist = []
usernamelist = []

#Login dengan cara input oleh user 
Akunpribadi = input("Nama Pengguna Anda=\n")
Password = input("Kata Sandi= \n" )
username = input("Akun siapa yang ingin anda crawl?[tanpa '@']\n")

L = instaloader.Instaloader(max_connection_attempts=0)
L.login(Akunpribadi, Password)

#akun yang ingin di crawling
akun_pertama = instaloader.Profile.from_username(L.context, username)
count = 1
for post in akun_pertama.get_posts():
        print("mengambil data dari akun " + username + " post ke " + str(count) + " dari " + str(akun_pertama.mediacount))
        caption = post.caption
        if caption is None:
            caption = ""
        if caption is not None:
            caption = caption.encode('ascii', 'ignore').decode('ascii')
        hashtag = post.caption_hashtags
        likes = post.likes
        
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(username)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1
        
#mengambil data akun followers dari akun yang dituju    
followers = []
count_account = 1
for follower in akun_pertama.get_followers():
    username_follower = follower.username
    akun_follower = instaloader.Profile.from_username(L.context, username_follower)
    if akun_follower.is_private == True:
        print("Profile Instagram dengan username " + username_follower + " tidak bisa diakses karena akun privat")
    count = 1
    for post in akun_follower.get_posts():
        print("mengambil data dari " + username_follower + " post ke " + str(count) + " dari " + str(akun_follower.mediacount) + ", follower " + username +  " ke " + str(count_account) + " dari " + str(akun_pertama.followers))
        caption = post.caption
        if caption is None:
            caption = ""
        if caption is not None:
            caption = caption.encode('ascii', 'ignore').decode('ascii')
        
        hashtag = post.caption_hashtags
        likes = post.likes
        
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(username_follower)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1
    count_account = count_account + 1


#Mengambil data dari salah satu followersnya followers
followers2 = []
count_account = 1
for follower in akun_follower.get_followers() :
        username_follower2 = follower.username
        jangkauan2 = instaloader.Profile.from_username(L.context, username_follower2)
        if jangkauan2.is_private == True:
                print("Profile Instagram dengan username " + username_follower2 + " tidak bisa diakses karena akun privat")
        count = 1
        for post in jangkauan2.get_posts():
                print("mengambil data dari " + username_follower2 + " post ke " + str(count) + " dari " + str(jangkauan2.mediacount) + ", follower " +  username_follower + "ke " + str(count_account) + " dari " + str(akun_follower.followers))
                caption = post.caption
                if caption is None:
                        captionion = ""
                if caption is not None:
                    caption = caption.encode('ascii', 'ignore').decode('ascii')
        
        hashtag = post.caption_hashtags
        likes = post.likes
        
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(username_follower2)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1
        count_account = count_account + 1
    
#menjadikan data yang diambil menjadi data tabel format csv
data = pd.DataFrame({"Username":usernamelist, "Caption":captionlist, "Hastag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
data.to_csv('Data_Crawling_Instagram.csv')
