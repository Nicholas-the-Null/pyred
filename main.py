import praw
import downloader,detect
import os,time
import datetime,requests
import GoldenFace
import cv2
from nudenet import NudeClassifier
classifier = NudeClassifier()

color_a = (255,255,0)
color_b = (0,0,255)


timer=int(input("Enter time in seconds: "))


try:
	request = requests.get("https://www.google.com")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("no internet")
    input()
    exit()


reddit = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='',username="",password="")

reddit.validate_on_submit = True


subreddit = reddit.subreddit("")






while True:
    print("download image...",end="\r")
    time.sleep(2)
    image=downloader.validate()
    print(f"download done for {image[0]}",end="\r")
    time.sleep(2)
    check_face=detect.face(image[0])
    text=""
    check_nsfw=False
    print("checking..... for nsfw tag "+ str(check_face),end="\r")
    safe_value=0
    unsafe_value=0
    x=classifier.classify(image[0])
    valori=list(x.values())
    valori=list(valori)
    valorii=valori[0]
    for x in valorii.keys():
        if x=="safe":
            safe_value=valorii.get(x)
        else:
            unsafe_value=valorii.get(x)

    if safe_value>unsafe_value:
        text=" safe with "+str(safe_value*100)+"% confidence"
    else:
        text=" unsafe with "+str(unsafe_value*100)+"% confidence"
        check_nsfw=True


    if check_face:
        try:
            analysis = GoldenFace.goldenFace(image[0])
            goldenRatio = analysis.geometricRatio()
            text+=" this person's vote is "+str(int(goldenRatio)+"/100")
        except Exception:
            check_face=False
    os.system("cls")
    post=subreddit.submit_image(image[0]+text,image[0],nsfw=check_nsfw)
    post.mod.approve()
    post.reply("log of this post: "+
    
    "download post at "+datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
    +"\n\nafter " + str(image[1])+" attemp " 
    + "\n\nfile name "+ image[0] + "\n\nwith sha " + str(image[2]) + "\n\nreddit id " + str(post.id) +"\n\nnsfw " + str(check_nsfw) + text+"\n")
    
    
    
    
    print("saving log",end="\r")
    time.sleep(1)
    with open("log.txt","a") as file:
        file.write("download post at "+datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")+" after " + str(image[1])+" attemp " + "file name "+ image[0] + " with sha " + str(image[2]) + " reddit id " + str(post.id) +" nsfw " + str(check_nsfw) + text+"\n")
    os.remove(image[0])
    print("removing",end="\r")
    print("waiting",end="\r")
    os.system("cls")
    #delete_post=reddit.submission("oukhpm")
    #delete_post.delete()
    try:
        for i in reversed(range(timer)):
            print(i,end="\r")
            if i==1000 or i==10 or i==100:
                os.system("cls")
            time.sleep(1)

    except KeyboardInterrupt:
        ex=input("do u want exit y/any if you choose any the timeout will end:")
        if ex=="y":exit()
        else:
            print("restarting",end="\r")

#['STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_chunk', '_comments_by_id', '_fetch', '_fetch_data', '_fetch_info', '_fetched', '_kind', '_reddit', '_reset_attributes', '_safely_add_arguments', '_url_parts', '_vote', 'award', 'clear_vote', 'comment_limit', 'comment_sort', 'comments', 'crosspost', 'delete', 'disable_inbox_replies', 'downvote', 'duplicates', 'edit', 'enable_inbox_replies', 'flair', 'fullname', 'gild', 'hide', 'id', 'id_from_url', 'mark_visited', 'mod', 'parse', 'reply', 'report', 'save', 'shortlink', 'unhide', 'unsave', 'upvote']
#dir(reddit)
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_authorized_core', '_check_for_async', '_check_for_update', '_core', '_handle_rate_limit', '_next_unique', '_objectify_request', '_objector', '_prepare_common_authorizer', '_prepare_objector', '_prepare_prawcore', '_prepare_trusted_prawcore', '_prepare_untrusted_prawcore', '_ratelimit_regex', '_read_only_core', '_token_manager', '_unique_counter', '_validate_on_submit', 'auth', 'comment', 'config', 'delete', 'domain', 'front', 'get', 'inbox', 'info', 'live', 'multireddit', 'patch', 'post', 'put', 'random_subreddit', 'read_only', 'redditor', 'redditors', 'request', 'submission', 'subreddit', 'subreddits', 'update_checked', 'user', 'username_available', 'validate_on_submit']
