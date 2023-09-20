from reviews import my_reviews
from hearts import likes
from index import get_following_data

def my_main(user):
    
    print(" ")
    my_reviews(user)
    print(" ")
    likes(user)
    print(" ")
    get_following_data(user)
    print("Relevent Data Dumped Into Elasticsearch...")
    
if(__name__=='__main__'):
    my_main('AFV2KSFLWI3OUOVJMMA5Y3XOEFKA')