from elasticsearch import Elasticsearch

def connect_to_elasticsearch():
     conn =  Elasticsearch([{'host':'localhost' , 'port':9200}])
     return conn

if __name__ == "__main__":
    ok = connect_to_elasticsearch()
    print(ok)