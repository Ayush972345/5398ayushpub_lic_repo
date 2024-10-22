from elasticsearch import Elasticsearch

# Step 3: Connect to Elasticsearch
# Make sure you have the correct Elasticsearch host and port
es = Elasticsearch([{'host': 'localhost', 'port': 5601}])

# Step 4: Define the Elasticsearch Query
# For example, searching for documents where 'field1' matches 'value1'
query = {
    "query": {
        "match": {
            "field1": "value1"
        }
    }
}

# Step 5: Execute the Query
response = es.search(index="your-index-name", body=query)

# Step 6: Process the Response
# Displaying the results
print("Total Hits:", response['hits']['total']['value'])
for hit in response['hits']['hits']:
    print(hit["_source"])

# Optionally, you can add pagination or filter further as needed

