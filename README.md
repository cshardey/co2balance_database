
# Database for CO2 Balance

First ETL step for creating data source for data pipeline

## Authors

- [@cshardey](https://github.com/cshardey)


## Deployment
1. Create a .env file in the db folder with the following variables:
```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
```

2. Create a .env file in the api_service folder with the following variables:
Generate a secret key for the JWT token
```
JWT_SECRET_KEY
JWT_REFRESH_SECRET_KEY
```

3. RUN the docker containers in the docker folder. Each docker  service  is located in a separate folder. The docker-compose.yml file is used to run the containers. The docker-compose.yml file is located in the docker folder.

4. To access the various services, the following ports are used:
```
Airflow: 8080
Postgres: 5432
FastAPI: 8000
Monitoring Service: 3000
Resumable Image Upload Service: 1080
```





[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Acknowledgements

 - CO2 Balance Team
 - Dr Elisa Covato
## License

[MIT](https://choosealicense.com/licenses/mit/)
