from amazon_response import reviews
import requests
import json
from colorama import Fore
from ESConn import connect_to_elasticsearch

def my_reviews(name):
    resp = reviews(name)
    data = json.loads(resp.content)
    
    query = {
        "Reviews Details:":[]
    }
    
    print(" ")
    all_Reviews = data.get("contributions")
    for all in all_Reviews:
        rating = all["rating"]
        visibility = all["visibility"]
        votes = all["helpfulVotes"]
        title = all["title"]
        text = all["text"]
        
        dict1 = {
            "Rating:": rating,
            "Visibility:" : visibility,
            "Votes:": votes ,
            "Title:":title,
            "Description of review:":text
        }
        
        query["Reviews Details:"].append(dict1)
        
        print(Fore.LIGHTCYAN_EX+"Rating : "+Fore.LIGHTGREEN_EX+str(rating))
        print(Fore.LIGHTCYAN_EX+"Total votes on The Reiew : "+Fore.LIGHTGREEN_EX+str(votes))
        print(Fore.LIGHTCYAN_EX+"Visibility of the Review : "+Fore.LIGHTGREEN_EX+str(visibility))
        print(Fore.LIGHTCYAN_EX+"Title of The Reviews : "+Fore.LIGHTGREEN_EX+str(title))
        print(Fore.LIGHTCYAN_EX+"Description Of The Review : "+Fore.LIGHTGREEN_EX+str(text))
        print(" ")
    
    conn = connect_to_elasticsearch()
    conn.index(index='amazon',doc_type='doc',body=query)

if(__name__=='__main__'):
    my_reviews('AFV2KSFLWI3OUOVJMMA5Y3XOEFKA')