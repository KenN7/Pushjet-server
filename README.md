# Pushjet-server
complete collection of tools for pushjet, including api, broker and connectors

## Run
### Configuration

```bash
echo MYSQL_ROOT_PASSWORD=$(openssl rand -base64 32) >> .env
echo MYSQL_DATABASE=$CHOSEN_DBNAME >> .env
echo MYSQL_USER=$CHOSEN_MYSQL_USERNAME >> .env
echo MYSQL_PASSWORD=$(openssl rand -base64 32) >> .env
echo GOOGLE_API_KEY=$YOUR_GCM_API_KEY >> .env
echo GOOGLE_GCM_SENDER_ID=$YOUR_GCM_SENDERID >> .env
```

### Launch

```bash
docker-compose pull
docker-compose build
docker-compose up -d
docker exec -it pushjetserver_pushjetapi_1 ./create-db.sh
```

### Use

Go to [http://localhost:8000](http://localhost:8000)
