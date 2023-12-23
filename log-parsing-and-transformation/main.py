import re
import json

def parse_log(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    error_count = 0
    total_response_time = 0
    total_transactions = len(logs)

    for log in logs:
        match = re.match(r'\[(.*?)\] (\d+) (\d+)', log)
        if match:
            timestamp, status_code, response_time = match.groups()
            if int(status_code) >= 400:
                error_count += 1
            total_response_time += int(response_time)

    avg_response_time = total_response_time / total_transactions

    metrics = {
        "error_count": error_count,
        "avg_response_time": avg_response_time,
        "total_transactions": total_transactions
    }

    return metrics

def transform_to_json(metrics):
    return json.dumps(metrics, indent=2)

if __name__ == "__main__":
    log_file = "sample.log"
    extracted_metrics = parse_log(log_file)
    json_metrics = transform_to_json(extracted_metrics)

    with open("transformed_metrics.json", 'w') as output_file:
        output_file.write(json_metrics)
