import requests
import json

def dl_video(link):
    url = link
    
    mediaInfo = dict()

    if url.find("nstagram") == -1:
        mediaInfo["response"] = "failed"  
        return mediaInfo        

    try:
        if url[-1] != "/":
            url = url + "/"

        head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        req_link = url + '?__a=1'
        print(req_link)
        r = requests.get(req_link, headers = head)
        json_data = json.loads(r.text)

        mediaType = json_data["graphql"]["shortcode_media"]["__typename"]
        mediaUrl = json_data["graphql"]["shortcode_media"]["video_url"]
        uzanti = json_data["graphql"]["shortcode_media"]["shortcode"]
        user_id = json_data["graphql"]["shortcode_media"]["owner"]["id"]
        ppurl = json_data["graphql"]["shortcode_media"]["owner"]["profile_pic_url"]
        username = json_data["graphql"]["shortcode_media"]["owner"]["username"]
        mediacount = json_data["graphql"]["shortcode_media"]["owner"]["edge_owner_to_timeline_media"]["count"]
        followercount = json_data["graphql"]["shortcode_media"]["owner"]["edge_followed_by"]["count"]
        fullname = json_data["graphql"]["shortcode_media"]["owner"]["full_name"]
    except:
        mediaInfo["response"] = "failed"  
        return mediaInfo

    if mediaType != "GraphVideo":
        mediaInfo["response"] = "failed"  
        return mediaInfo
    elif mediaType == "GraphVideo":   
        if int(followercount) >= 1000000:
            followercount = f"{round(followercount/1000000)}M"
        elif int(followercount) >= 100000 & int(followercount) <= 999999:
            followercount = f"{round(followercount/1000,1)}K"
        elif int(followercount) >= 10000 & int(followercount) <= 100000:
            followercount = f"{round(followercount/1000,1)}K"

        mediaInfo["username"] = username
        mediaInfo["fullname"] = fullname
        mediaInfo["mediaUrl"] = mediaUrl
        mediaInfo["ppurl"] = ppurl
        mediaInfo["mediacount"] = mediacount
        mediaInfo["followercount"] = followercount
        mediaInfo["uzanti"] = uzanti
        mediaInfo["type"] = mediaType
        mediaInfo["response"] = "success"

        return mediaInfo


def dl_photo(link):
    url = link
    mediaInfo = dict()

    if url.find("nstagram") == -1:
        mediaInfo["response"] = "failed"  
        return mediaInfo           

    try:
        if url[-1] != "/":
            url = url + "/"

        head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        req_link = url + '?__a=1'
        print(req_link)
        r = requests.get(req_link, headers = head)
        json_data = json.loads(r.text)

        mediaType = json_data["graphql"]["shortcode_media"]["__typename"]
    except:
        mediaInfo["response"] = "failed"  
        return mediaInfo

    if mediaType == "GraphImage":
        mediaUrl = json_data["graphql"]["shortcode_media"]["display_resources"][-1]["src"]
        uzanti = json_data["graphql"]["shortcode_media"]["shortcode"]
        user_id = json_data["graphql"]["shortcode_media"]["owner"]["id"]
        ppurl = json_data["graphql"]["shortcode_media"]["owner"]["profile_pic_url"]
        username = json_data["graphql"]["shortcode_media"]["owner"]["username"]
        mediacount = json_data["graphql"]["shortcode_media"]["owner"]["edge_owner_to_timeline_media"]["count"]
        followercount = json_data["graphql"]["shortcode_media"]["owner"]["edge_followed_by"]["count"]
        mediaType = json_data["graphql"]["shortcode_media"]["__typename"]
        fullname = json_data["graphql"]["shortcode_media"]["owner"]["full_name"]

        if int(followercount) >= 1000000:
            followercount = f"{round(followercount/1000000)}M"
        elif int(followercount) >= 100000 & int(followercount) <= 999999:
            followercount = f"{round(followercount/1000,1)}K"
        elif int(followercount) >= 10000 & int(followercount) <= 100000:
            followercount = f"{round(followercount/1000,1)}K"

        mediaInfo["username"] = username
        mediaInfo["fullname"] = fullname
        mediaInfo["mediaUrl"] = mediaUrl
        mediaInfo["ppurl"] = ppurl
        mediaInfo["mediacount"] = mediacount
        mediaInfo["followercount"] = followercount
        mediaInfo["uzanti"] = uzanti
        mediaInfo["type"] = mediaType
        mediaInfo["response"] = "success"
        return mediaInfo
    
    elif mediaType == "GraphSidecar":
        uzanti = json_data["graphql"]["shortcode_media"]["shortcode"]
        user_id = json_data["graphql"]["shortcode_media"]["owner"]["id"]
        ppurl = json_data["graphql"]["shortcode_media"]["owner"]["profile_pic_url"]
        username = json_data["graphql"]["shortcode_media"]["owner"]["username"]
        mediacount = json_data["graphql"]["shortcode_media"]["owner"]["edge_owner_to_timeline_media"]["count"]
        followercount = json_data["graphql"]["shortcode_media"]["owner"]["edge_followed_by"]["count"]
        mediaType = json_data["graphql"]["shortcode_media"]["__typename"]
        fullname = json_data["graphql"]["shortcode_media"]["owner"]["full_name"]

        base_links = json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]
        photo_links = []
        for i in base_links:
            photo_links.append(i["node"]["display_resources"][-1]["src"])

        if int(followercount) >= 1000000:
            followercount = f"{round(followercount/1000000)}M"
        elif int(followercount) >= 100000 & int(followercount) <= 999999:
            followercount = f"{round(followercount/1000,1)}K"
        elif int(followercount) >= 10000 & int(followercount) <= 100000:
            followercount = f"{round(followercount/1000,1)}K"

        mediaInfo["username"] = username
        mediaInfo["fullname"] = fullname
        mediaInfo["mediaUrl"] = photo_links
        mediaInfo["ppurl"] = ppurl
        mediaInfo["mediacount"] = mediacount
        mediaInfo["followercount"] = followercount
        mediaInfo["uzanti"] = uzanti
        mediaInfo["type"] = mediaType
        mediaInfo["response"] = "success"
        return mediaInfo

    else:
        mediaInfo["response"] = "failed"
        return mediaInfo

