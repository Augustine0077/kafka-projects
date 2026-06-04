# Apache Kafka Projects

## Author

**Augustine Shaji**

---

# Project Overview

This repository contains two Apache Kafka projects developed using Python and Docker.

The projects demonstrate:

- Kafka Producers
- Kafka Consumers
- Kafka Topics
- Kafka Partitions
- Consumer Groups
- Partition Rebalancing
- Poison Message Handling
- Event-Driven Architecture
- Real-Time Analytics

---

# Technologies Used

- Apache Kafka
- Python
- kafka-python
- Docker
- Git
- GitHub

---

# Project 1: E-Commerce Event Processing

A Kafka-based order processing system demonstrating Kafka fundamentals.

## Features

- Producer and Consumer
- CSV Data Publishing
- Consumer Groups
- Offset Management
- Partition Rebalancing
- Poison Message Handling
- Dead Letter Topic Design

---

## Kafka Topic

```text
ecommerce.orders
```

---

## Workflow

```text
orders.csv
      |
      v
Producer
      |
      v
ecommerce.orders
      |
      v
Consumer Group (order-analytics)
      |
      v
Order Analytics
```

---

# Task 1.2 - Kafka Setup

## Kafka Broker Started

![Kafka Broker](kafka-ecommerce-project/1.png)

## Docker Verification

![Docker Verification](kafka-ecommerce-project/2.png)

## Topic Creation

![Topic Creation](kafka-ecommerce-project/3.png)

## Message Production

![Message Production](kafka-ecommerce-project/4.png)

## Message Consumption

![Message Consumption](kafka-ecommerce-project/5.png)

---

# Task 1.3 - Topic Creation and Partition Consumption

## Topic Description

![Topic Description](kafka-ecommerce-project/1.3-A.png)

## Producing Messages with Keys

![Producing Messages](kafka-ecommerce-project/1.3-B.png)

## Consuming Messages from Partition 0

![Partition Consumption](kafka-ecommerce-project/1.3-C.png)

---

# Task 2.1 - CSV Producer

Producer reads e-commerce order records from CSV and publishes them to Kafka.

## Producer Execution

![Producer Execution](kafka-ecommerce-project/2.1.png)

## Published Records

![Published Records](kafka-ecommerce-project/2.1-1.png)

---

# Task 2.2 - Consumer Analytics

Consumer reads messages and maintains a running order count per user.

## Consumer Output

![Consumer Output](kafka-ecommerce-project/2.2-A.png)

## Running Count Per User

![Running Count](kafka-ecommerce-project/2.2-B.png)

---

# Task 2.3 - Consumer Group Rebalancing

Two consumer instances were started in the same group to demonstrate partition assignment and rebalancing.

## Consumer Instance 1

![Consumer Rebalance 1](kafka-ecommerce-project/2.3-A.png)

## Consumer Instance 2

![Consumer Rebalance 2](kafka-ecommerce-project/2.3-B.png)

---

# Task 2.4 - Poison Message Handling

An invalid JSON message was intentionally sent to Kafka.

## Poison Message Published

![Poison Message Published](kafka-ecommerce-project/2.4-A.png)

## Consumer Error Handling

![Poison Message Handling](kafka-ecommerce-project/2.4-B.png)

---

## Dead Letter Topic (DLT) Design

```text
ecommerce.orders.dlt
```

Invalid messages can be redirected to the Dead Letter Topic instead of crashing consumers.

Benefits:

- Fault tolerance
- Easier debugging
- Message recovery
- Improved reliability

---

# Project 2: Ride Sharing Event Pipeline

A Kafka-based ride sharing analytics system that processes ride events and generates driver statistics.

---

## Kafka Topics

```text
ride.events
ride.completed
driver.earnings
```

---

# Architecture Diagram

![Architecture Diagram](ride_sharing_pipeline_page-0001.jpg)

---

## Workflow

```text
Ride Producer
      |
      v
ride.events
      |
      v
Completed Ride Processor
      |
      v
ride.completed
      |
      v
Driver Earnings Consumer
      |
      v
driver.earnings
      |
      v
Top 5 Drivers Report
```

---

# Ride Event Producer

The producer simulates ride events.

Event Structure:

```json
{
  "ride_id": "R1001",
  "driver_id": "D101",
  "rider_id": "U501",
  "status": "COMPLETED",
  "lat": "10.015",
  "lon": "76.321",
  "timestamp": "2025-06-01 10:00:00"
}
```

## Ride Producer Output

![Ride Producer](kafka-ride-sharing-project/3A.png)

---

# Completed Ride Processor

Reads from:

```text
ride.events
```

Filters:

```text
COMPLETED
```

Writes to:

```text
ride.completed
```

## Processor Output

![Completed Ride Processor](kafka-ride-sharing-project/3B.png)

---

# Driver Earnings Consumer

Consumes completed rides and calculates:

- Total Completed Rides
- Total Driver Earnings

Formula:

```text
1 Completed Ride = $5
```

## Driver Earnings Output

![Driver Earnings](kafka-ride-sharing-project/3C.png)

---

# Top Drivers Report

Example Output:

```text
1. D101 | Completed Rides: 4 | Earnings: $20
2. D102 | Completed Rides: 2 | Earnings: $10
3. D104 | Completed Rides: 2 | Earnings: $10
4. D103 | Completed Rides: 1 | Earnings: $5
5. D105 | Completed Rides: 1 | Earnings: $5
```

---

# Project Structure

```text
kafka-projects
│
├── kafka-ecommerce-project
│   ├── producer.py
│   ├── consumer.py
│   ├── consumer_with_error_handling.py
│   ├── orders.csv
│   ├── docker-compose.yml
│   └── screenshots
│
├── kafka-ride-sharing-project
│   ├── ride_producer.py
│   ├── completed_ride_processor.py
│   ├── driver_earnings_consumer.py
│   ├── top5_drivers.py
│   ├── ride_events.csv
│   └── screenshots
│
└── README.md
```

---

# Learning Outcomes

This project demonstrates:

- Kafka Broker Management
- Topic Creation
- Message Publishing
- Message Consumption
- Consumer Groups
- Offset Management
- Partition Rebalancing
- Poison Message Handling
- Dead Letter Topic Design
- Event Filtering
- Stream Processing
- Real-Time Analytics
- Event-Driven Architecture

---

# Design Decisions

## Why Kafka?

Kafka provides:

- High Throughput
- Reliability
- Scalability
- Fault Tolerance

## Why Python?

Python provides:

- Rapid Development
- Easy Kafka Integration
- Simple Maintenance

## Why Separate Topics?

Separate topics improve:

- Scalability
- Maintainability
- Loose Coupling

## Why Dead Letter Topic?

A Dead Letter Topic allows failed messages to be stored separately without affecting normal processing.

---

# Conclusion

This repository successfully demonstrates Apache Kafka fundamentals and event-driven application development using Python.

Projects Included:

1. E-Commerce Event Processing System
2. Ride Sharing Event Analytics Pipeline

The implementation covers:

- Kafka Producers
- Kafka Consumers
- Consumer Groups
- Partition Rebalancing
- Poison Message Handling
- Event Filtering
- Real-Time Driver Analytics

---

## License

This project is for educational and learning purposes.