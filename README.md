# **Distributed Key-Value Storage System Implementation**

This project implements a lightweight distributed key-value storage architecture utilizing Python and Flask frameworks.

The architecture comprises multiple autonomous storage servers alongside a client application. Each server maintains local data persistence, while the client ensures data replication across all operational servers.


## **Technology Stack**
- Programming Language: Python
- Web Framework: Flask
- Communication Protocol: HTTP/REST
- Data Interchange Format: JSON

## **Installation Instructions**

Install required Python packages:

```bash
pip install flask requests
```

## **Execution Procedure**
1. **Initialize Storage Nodes:**
   Open three separate terminal sessions and execute:

   ```bash
   python node.py 5000
   python node.py 5001  
   python node.py 5002
   ```
2. **Launch Client Application:**
   Open an additional terminal session and run:

   ```bash
   python client.py
   ```

## **Operational Commands**

Within the client interface, the following commands are available:
- `put` → Store a key-value pair across all active nodes
- `get` → Retrieve a value using its associated key
- `exit` → Terminate the client session

## **System Capabilities**

- **Data Replication Mechanism:** Automatic duplication across multiple storage nodes
- **Independent Server Architecture:** Each node operates autonomously
- **Fault Tolerance:** System remains operational despite individual node failures
- **Simplified Communication Protocol:** HTTP-based client-server interaction

**Academic Context:** CSS 439 - Distributed Data Systems
