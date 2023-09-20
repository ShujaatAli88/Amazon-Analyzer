import requests
from bs4 import BeautifulSoup
from amazon_response import followings
import json
from colorama import Fore
from ESConn import connect_to_elasticsearch

def get_following_data(user_identifier):
    resp = followings(user_identifier)
    
    con_ob = connect_to_elasticsearch()
    
    if resp.status_code == 200:
        data = json.loads(resp.text)
        
        following_data = data.get("followingData")
        
        if following_data is not None:  # Check if following_data is not None
            total_followers = following_data.get("count", 0)  # Provide a default value of 0 if "count" is not present
            followers_list = following_data.get("follows", [])  # Provide an empty list as a default
        
            query = {
                "Followings": []
            }
            print(Fore.LIGHTGREEN_EX+f"Following: {total_followers}")
            
            if followers_list:
                print(Fore.LIGHTCYAN_EX+"Followed Entities:")
                for follower in followers_list:
                    title = follower.get("title", "N/A")
                    imageUrl = follower.get("imageUrl", "N/A")
                    
                    myQuery ={
                        "Name": title,
                        "Image Url": imageUrl
                    }
                    
                    query["Followings"].append(myQuery)
                    
                    print(f"Title: {title}")
                    print(Fore.LIGHTYELLOW_EX+f"Image URL: {imageUrl}")
                
                # Convert the query to JSON before indexing
                json_query = json.dumps(query)
                
                # Index the JSON data in Elasticsearch
                con_ob.index(index='amazon',doc_type='doc',body=json_query)
             
            else:
                print("No followers found.")
        else:
            print("No following data found in the response.")
    else:
        print(f"Error: HTTP status code {resp.status_code}")

if __name__ == '__main__':
    get_following_data('AFV2KSFLWI3OUOVJMMA5Y3XOEFKA')
