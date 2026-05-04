from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNTER = Counter(
    "coal_requests_total",
    "Total API requests"
)

REQUEST_LATENCY = Histogram(
    "coal_request_latency_seconds",
    "Request latency"
)

ACTIVE_ALERTS = Gauge(
    "coal_active_alerts",
    "Number of active alerts"
)
