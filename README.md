# Coal DevOps Monitoring Platform

DevOps-ориентированная тестовая платформа для мониторинга производственных показателей предприятия угольной промышленности.  
Проект демонстрирует разработку и оптимизацию контейнерной среды с использованием Kubernetes, Prometheus и инструментов DevOps.


# Назначение проекта

Платформа реализует:

- контейнеризированный микросервис мониторинга датчиков оборудования
- оркестрацию в Kubernetes
- сбор метрик Prometheus
- автоскейлинг нагрузки
- DevOps pipeline
- нагрузочное тестирование
- health-checks и readiness probes

Имитация производственных датчиков:

- температура оборудования
- вибрация узлов
- газовая концентрация
- уровень тревожных событий

# Архитектура решения

Client → API Service → Kubernetes → Prometheus → Grafana

Компоненты:

- FastAPI сервис мониторинга
- Docker контейнер
- Kubernetes Deployment
- Horizontal Pod Autoscaler
- Prometheus metrics endpoint
- ServiceMonitor (Prometheus Operator)
- Load testing (Locust)

# Технологический стек

- Python 3.11
- FastAPI
- Prometheus client
- Docker
- Kubernetes
- Prometheus Operator
- Grafana
- GitHub Actions CI
- Locust (нагрузочное тестирование)

# Структура проекта

```
coal-devops-platform/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── metrics.py
│   ├── models.py
│   ├── services/
│   │    └── sensor_service.py
│   └── api/
│        └── routes.py
│
├── docker/
│   └── Dockerfile
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   └── servicemonitor.yaml
│
├── loadtest/
│   └── locustfile.py
│
├── .github/workflows/
│   └── ci.yml
│
├── requirements.txt
├── .env.example
└── README.md
```

# Переменные окружения
Создать файл `.env`:
```
SERVICE_NAME=coal-monitoring-service
ENVIRONMENT=dev
SENSOR_DELAY_MIN=0.05
SENSOR_DELAY_MAX=0.25
```

# Локальный запуск (без Kubernetes)

## 1. Установка зависимостей
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

pip install -r requirements.txt
```

## 2. Запуск сервиса
```bash
uvicorn app.main:app --reload
```

## 3. Проверка
Перейти на адреса:
```
http://localhost:8000/
http://localhost:8000/sensor
http://localhost:8000/health
http://localhost:8000/metrics
```

# Запуск через Docker

## Сборка образа
```bash
docker build -t coal-monitor:1.0 -f docker/Dockerfile .
```

## Запуск контейнера
```bash
docker run -p 8000:8000 coal-monitor:1.0
```

# Развёртывание в Kubernetes
## Требования

- установлен kubectl
- доступ к кластеру
- установлен Prometheus Operator (или kube-prometheus-stack)
- metrics-server (для HPA)

## 1. Создание namespace
```bash
kubectl apply -f k8s/namespace.yaml
```

## 2. Deployment
```bash
kubectl apply -f k8s/deployment.yaml
```

## 3. Service
```bash
kubectl apply -f k8s/service.yaml
```

## 4. Autoscaling
```bash
kubectl apply -f k8s/hpa.yaml
```

## 5. Prometheus мониторинг
```bash
kubectl apply -f k8s/servicemonitor.yaml
```

## Проверка ресурсов
```bash
kubectl get pods -n coal-devops
kubectl get svc -n coal-devops
kubectl get hpa -n coal-devops
```
# Метрики Prometheus

Сервис экспортирует:

- coal_requests_total
- coal_request_latency_seconds
- coal_active_alerts

Endpoint: /metrics


Prometheus автоматически собирает данные через ServiceMonitor.

# Grafana

Рекомендуемые панели:

- RPS
- latency histogram
- error/critical alerts
- pod scaling
- CPU utilization
- request duration


# Нагрузочное тестирование

## Установка Locust

```bash
pip install locust
```

## Запуск
```bash
cd loadtest
locust
```


Открыть: http://localhost:8089
Указать: Target host: http://SERVICE_IP
Реализованы endpoints: 
* /health
* /sensor
* /metrics

Используются Kubernetes probes:

- readinessProbe
- livenessProbe
