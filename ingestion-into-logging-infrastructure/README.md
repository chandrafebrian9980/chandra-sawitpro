# Introduction for my assigment SAWIT PRO

flow for using this scripts command :

1. docker-compose -f docker-compose.setup.yml run --rm keystore
2. docker-compose -f docker-compose.setup.yml run --rm certs
3. docker-compose up -d
4. Go to https://localhost:5601 to access Kibana dashboard.
- Username: elastic
- Password: chandra
5. make tools
6. make collect-docker-logs
7. make all



Stack Version: [8.8.0]

### Main Features 📜

- Configured a Single Node Cluster
- Security Enabled By Default.
- Configured to Enable:
  - Logging & Metrics Ingestion
  - APM
  - Alerting
  - Machine Learning
  - SIEM
  - Use Docker-Compose and `.env` to configure your entire stack parameters.
- Persist Elasticsearch's Keystore and SSL Certifications.
- Self-Monitoring Metrics Enabled.
- Prometheus Exporters for Stack Metrics.
- Collect Docker Host Logs to ELK via `make collect-docker-logs`.
- Embedded Container Healthchecks for Stack Images.

#### More points

<details><summary>Expand...</summary>
<p>

- Parameterize credentials in .env instead of hardcoding `elastic:chandra` in every component config.


</p>
</details>

-----

# Requirements
- 4GB RAM

# Setup

1. Initialize Elasticsearch Keystore and TLS Self-Signed Certificates
    ```bash
    $ make setup
    ```
3. Start Elastic Stack
    ```bash
    $ make elk           <OR>         $ docker-compose up -d		<OR>		$ docker compose up -d
    ```
4. Visit Kibana at [https://localhost:5601](https://localhost:5601) or `https://<your_public_ip>:5601`

    Default Username: `elastic`, Password: `chandra`

> 🏃🏻‍♂️ To start ingesting logs, you can start by running `make collect-docker-logs` which will collect your host's container logs.

## Additional Commands

<details><summary>Expand</summary>
<p>

#### To Start Monitoring and Prometheus Exporters
```shell
$ make monitoring
```
#### To Start Tools
```shell
$ make tools
```
#### To Ship Docker Container Logs to ELK 
```shell
$ make collect-docker-logs
```
#### To Start **Elastic Stack, Tools and Monitoring**
```
$ make all
```
#### To Start 2 Extra Elasticsearch nodes (recommended for experimenting only)
```shell
$ make nodes
```
#### To Rebuild Images
```shell
$ make build
```
#### Bring down the stack.
```shell
$ make down
```

#### Reset everything, Remove all containers, and delete **DATA**!
```shell
$ make prune
```

</p>
</details>

# Configuration

* Some Configuration are parameterized in the `.env` file.
  * `ELASTIC_PASSWORD`, user `elastic`'s password (default: `chandra` _pls_).
  * `ELK_VERSION` Elastic Stack Version (default: `8.8.0`)
  * `ELASTICSEARCH_HEAP`, how much Elasticsearch allocate from memory (default: 1GB -good for development only-)
  * `LOGSTASH_HEAP`, how much Logstash allocate from memory.
  * Other configurations which their such as cluster name, and node name, etc.
* Elasticsearch Configuration in `elasticsearch.yml` at `./elasticsearch/config`.
* Logstash Configuration in `logstash.yml` at `./logstash/config/logstash.yml`.
* Logstash Pipeline in `main.conf` at `./logstash/pipeline/main.conf`.
* Kibana Configuration in `kibana.yml` at `./kibana/config`.
* Rubban Configuration using Docker-Compose passed Environment Variables.

### Setting Up Keystore

You can extend the Keystore generation script by adding keys to `./setup/keystore.sh` script. (e.g Add S3 Snapshot Repository Credentials)

To Re-generate Keystore:
```
make keystore
```

### Notes

- Elasticsearch will save its data to a volume named `elasticsearch-data`

- Make sure to run `make setup` if you changed `ELASTIC_PASSWORD` and to restart the stack afterwards.

- For Linux Users it's recommended to set the following configuration (run as `root`)
    ```
    sysctl -w vm.max_map_count=262144
    ```
   

