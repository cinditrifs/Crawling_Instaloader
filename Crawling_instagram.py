import instaloader
import pandas as pd
from typing import List
import re
import time

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
        if count > 100 :
                break
        print(username + " post ke " + str(count) + " dari " + str(akun_pertama.mediacount)) #cindihouw_ post ke 1 dari 61
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
count = 1
count_follower = 1
for follower in akun_pertama.get_followers():
    if count_follower > 500 : #batasan untuk crawling akun
            break
    username_follower = follower.username
    akun_follower = instaloader.Profile.from_username(L.context, username_follower)
    if akun_follower.is_private == True:
        print("Username " + username_follower + " tidak bisa diakses karena akun privat") #username candadfs tidak bisa diakses karena akun privat
    count = 1
    for post in akun_follower.get_posts():
        if count > 100 :
                break
        print(username_follower + " post ke " + str(count) + " dari " + str(akun_follower.mediacount) + ", follower " + username +  " ke " + str(count_follower) + " dari " + str(akun_pertama.followers))
        #fitrianisa post ke 1 dari 5 follower cindihouw_ ke 2 dari 20
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
    count_follower = count_follower + 1
    print ("slepp to 1 second")
    time.sleep(1)


#Mengambil data dari salah satu followersnya followers
    followers2 = []
    count1 = 1    
    count_followers2 = 1
    for follower in akun_follower.get_followers() :
        if count_followers2 > 500 :
                break
        username_follower2 = follower.username
        jangkauan2 = instaloader.Profile.from_username(L.context, username_follower2)
        if jangkauan2.is_private == True:
                print("Username " + username_follower2 + " tidak bisa diakses karena akun privat")
        count = 1
        for post in jangkauan2.get_posts():
                if count > 100 :
                        break
                print(username_follower2 + " post ke " + str(count) + " dari " + str(jangkauan2.mediacount) + ", follower " +  username_follower + "ke " + str(count1) + " dari " + str(akun_follower.followers))
                #hanifaahmad post ke 1 dari 12 followers fitriannisa ke 
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
        count_followers2 = count_followers2 + 1
        count1= count1 +1
        print ("slepp to 1 second")
        time.sleep(1)
        
    
#menjadikan data yang diambil menjadi data tabel format csv
data = pd.DataFrame({"Username":usernamelist, "Caption":captionlist, "Hastag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
data.to_csv('Data_Crawling_Instagram.csv')

