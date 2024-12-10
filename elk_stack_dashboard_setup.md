# Setting Up a Real-Time SOC Dashboard with ELK Stack

## Prerequisites
- Elasticsearch, Logstash, Kibana installed.
- Log sources from AWS, Azure, GCP, and on-premise systems.

## Steps
1. **Elasticsearch Configuration:**
   - Create indices for log storage: `aws-logs-*`, `azure-logs-*`.

2. **Logstash Pipeline:**
   - Parse logs from S3, Event Hub, and Pub/Sub:
     ```logstash
     input {
       s3 { bucket => "cloudtrail-logs" }
       azure_event_hubs { connection => "eventhub-connection-string" }
     }
     output {
       elasticsearch { hosts => ["localhost:9200"] index => "cloud-logs-%{+YYYY.MM.dd}" }
     }
     ```

3. **Kibana Visualization:**
   - Build visualizations for:
     - Unauthorized login attempts.
     - High-risk IAM policy changes.
     - Insecure network rules.

## Real-Time Alerts
- Use Elasticsearch Watcher or Alerting plugins to send Slack/Email alerts.
