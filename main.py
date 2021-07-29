import praw
import downloader,detect
import os,time

reddit = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='',username="",password="p")

reddit.validate_on_submit = True


subreddit = reddit.subreddit("")






while True:
    print("download image...",end="\n")
    time.sleep(2)
    image=downloader.validate()
    print(f"download done for {image}",end="\n")
    time.sleep(2)
    check_face=detect.face(image)

    print("checking..... for nsfw tag "+ str(check_face))
    test=subreddit.submit_image(image,image,nsfw=check_face)
    print("post have tag "+str(test.id))
    os.remove(image)
    print("removing")
    print("waiting")
    try:
        time.sleep(1800)
    except KeyboardInterrupt:
        ex=input("do u want exit y/any if you choose any the timeout will end:")
        if ex=="y":exit()
        else:
            print("restarting")
