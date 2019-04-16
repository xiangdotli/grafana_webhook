GET http://127.0.0.1:5001/

POST http://127.0.0.1:5001/notify
{
  "evalMatches": [
    {
      "value": 40.66,
      "metric": "metric",
      "tags": {
        "__name__": "go_goroutines",
        "instance": "prometheus:9090",
        "job": "prometheus"
      }
    }
  ],
  "message": "high numbers of goroutines found",
  "ruleId": 1,
  "ruleName": "Urgent Issue: high numbers of goroutines",
  "ruleUrl": "http://localhost:3000/d/w2u6SYgWk/monitor?fullscreen&edit&tab=alert&panelId=2&orgId=1",
  "state": "alerting",
  "title": "[Alerting] Urgent Issue: high numbers of goroutines"
}