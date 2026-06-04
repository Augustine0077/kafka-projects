<<<<<<< HEAD
# Apache Kafka Projects

## Author

**Augustine Shaji**

---

# Project Overview

This repository contains two Apache Kafka projects developed using Python and Docker to demonstrate real-time event streaming, consumer groups, partition rebalancing, event-driven processing, and real-time analytics.

## Technologies Used

- Apache Kafka
- Python
- kafka-python
- Docker
- GitHub

---

# Project 1: E-Commerce Event Processing

A Kafka-based order processing system demonstrating core Kafka concepts.

## Features

- Producer & Consumer
- Consumer Groups
- Partition Rebalancing
- Poison Message Handling
- Offset Management
- CSV-Based Event Publishing

## Kafka Topic

```text
ecommerce.orders
```

## Workflow

```text
orders.csv
    ↓
Producer
    ↓
ecommerce.orders
    ↓
Consumers
```

---

## Task 1.2 - Kafka Cluster Setup

### Kafka Broker Started

![Kafka Broker](D:\kafka  -assignment\.venv\Lib\site-packages\kafka-ecommerce-project\1.3 -A.png)

### Docker Verification

![Docker Verification](kafka-ecommerce-project/screenshots/2.png)

### Topic Creation

![Topic Creation](kafka-ecommerce-project/screenshots/3.png)

### Message Production

![Producer](kafka-ecommerce-project/screenshots/4.png)

### Message Consumption

![Consumer](kafka-ecommerce-project/screenshots/5.png)

---

## Task 1.3 - Topic Creation and Partition Consumption

### Topic Creation

![Topic Creation](kafka-ecommerce-project/screenshots/1.3-A.png)

### Producing Messages With Keys

![Producing Messages](kafka-ecommerce-project/screenshots/1.3-B.png)

### Consuming Messages From Partition 0

![Partition Consumption](kafka-ecommerce-project/screenshots/1.3-C.png)

---

## Task 2.1 - CSV Producer

### Producer Execution

![Producer Execution](kafka-ecommerce-project/screenshots/2.1.png)

### Published Records

![Published Records](kafka-ecommerce-project/screenshots/2.1-1.png)

---

## Task 2.2 - Consumer Analytics

### Consumer Output

![Consumer Output](kafka-ecommerce-project/screenshots/2.2-A.png)

### Running Order Count

![Running Count](kafka-ecommerce-project/screenshots/2.2-B.png)

---

## Task 2.3 - Consumer Group Rebalancing

### Consumer Instance 1

![Consumer Rebalance 1](kafka-ecommerce-project/screenshots/2.3-A.png)

### Consumer Instance 2

![Consumer Rebalance 2](kafka-ecommerce-project/screenshots/2.3-B.png)

---

## Task 2.4 - Poison Message Handling

### Poison Message Sent

![Poison Message](kafka-ecommerce-project/screenshots/2.4-A.png)

### Consumer Error Handling

![Poison Message Detection](kafka-ecommerce-project/screenshots/2.4-B.png)

### Dead Letter Topic (DLT)

```text
ecommerce.orders.dlt
```

The DLT is proposed to store invalid messages that cannot be processed successfully.

---

# Project 2: Ride Sharing Event Pipeline

A Kafka-based ride-sharing analytics system that processes ride events and generates driver statistics.

## Features

- Ride Event Producer
- Completed Ride Filtering
- Driver Earnings Calculation
- Top Drivers Reporting
- Event-Driven Architecture

## Kafka Topics

```text
ride.events
ride.completed
driver.earnings
```

---

## Architecture Diagram

![Architecture Diagram](kafka-ride-sharing-project/screenshots/architecture.png)

---

## Workflow

```text
ride_events.csv
        ↓
Ride Producer
        ↓
ride.events
        ↓
Completed Ride Processor
        ↓
ride.completed
        ↓
Driver Earnings Consumer
        ↓
driver.earnings
        ↓
Top 5 Drivers CLI
```

---

## Ride Producer

Publishes ride events into Kafka.

### Screenshot

![Ride Producer](kafka-ride-sharing-project/screenshots/3A.png)

---

## Completed Ride Processor

Filters only completed rides and forwards them to the `ride.completed` topic.

### Screenshot

![Completed Ride Processor](kafka-ride-sharing-project/screenshots/3B.png)

---

## Driver Earnings Consumer

Calculates:

- Completed Rides
- Driver Earnings

Formula:

```text
1 Completed Ride = $5
```

### Screenshot

![Driver Earnings](kafka-ride-sharing-project/screenshots/3C.png)

---

## Top Drivers Report

Example:

```text
1. D101 | Rides: 4 | Earnings: $20
2. D102 | Rides: 2 | Earnings: $10
3. D104 | Rides: 2 | Earnings: $10
4. D103 | Rides: 1 | Earnings: $5
5. D105 | Rides: 1 | Earnings: $5
```

---

# Learning Outcomes

This assignment demonstrates:

- Kafka Brokers
- Kafka Topics
- Kafka Partitions
- Kafka Producers
- Kafka Consumers
- Consumer Groups
- Offset Management
- Partition Rebalancing
- Poison Message Handling
- Dead Letter Topic Design
- Event Filtering
- Event-Driven Architecture
- Real-Time Analytics
- Stream Processing

---

# Design Decisions

## Why Kafka?

Kafka provides:

- High Throughput
- Reliability
- Fault Tolerance
- Scalability

## Why Python?

Python provides:

- Fast Development
- Easy Kafka Integration
- Readable Code

## Why Separate Topics?

Separate topics improve:

- Maintainability
- Scalability
- Loose Coupling

## Why Dead Letter Topic?

A Dead Letter Topic allows invalid messages to be stored separately for future investigation without crashing consumers.

---

# Conclusion

This project successfully demonstrates Apache Kafka fundamentals and event-driven application development through:

1. E-Commerce Event Processing System
2. Ride Sharing Event Analytics Pipeline

The implementation covers producer-consumer communication, consumer groups, partition rebalancing, poison message handling, event filtering, and real-time analytics using Apache Kafka and Python.
=======
# kafka-projects
>>>>>>> a3e8d65ab3dd29811db8e990ea9b9bda55e46884
