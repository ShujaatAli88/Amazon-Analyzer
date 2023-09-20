from amazon_response import hearts
import json
from colorama import Fore
from ESConn import connect_to_elasticsearch

def likes(user):
    con = connect_to_elasticsearch()
    resp = hearts(user)
    data = json.loads(resp.content)
    total_likes = data.get("helpfulVotes")
    dic1 = total_likes["helpfulVotesData"]
    hearted_Count = dic1["count"]
    print(Fore.LIGHTGREEN_EX+"Total likes on Account : "+Fore.LIGHTCYAN_EX+str(hearted_Count))
    
    query = {
        "Total Likes on Account:":hearted_Count
    }
    con.index(index='amazon',doc_type='doc', body=query)

if(__name__=='__main__'):
    likes('AFV2KSFLWI3OUOVJMMA5Y3XOEFKA')