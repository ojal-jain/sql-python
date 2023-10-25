import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://ojal-cosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'MVuK3hp9Jw45W29SFkPOLBACpv6nk5yONVsl2mGgKYLd1snpPNg35yks29izonZklHdN2g2ecJJEACDbipAGGA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}