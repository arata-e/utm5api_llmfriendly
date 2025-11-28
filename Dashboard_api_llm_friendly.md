# UTM5 API Section: Dashboard

This document describes the endpoints for the 'Dashboard' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Dashboard - Get admin tech support chat messages
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/ts_chat/admin_msgs`
### Parameters:
  - **Name:** `admin_id`
    - **Type:** `Number`
    - **Description:** system user identifier
### Example Response:

HTTP/1.1 200 OK
[
 {
   "admin_id": -1,
   "client_id": 494,
   "is_admin_origin": false,
   "last_update": 1601468912,
   "msg": "test22222"
 },
 {
   "admin_id": -1,
   "client_id": 494,
   "is_admin_origin": false,
   "last_update": 1601474202,
   "msg": "{\"message\": \"mySUpper client message\"}"
 }...
]
```

---

## Endpoint: Dashboard - Get core build info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/core_build_info`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[]
```

---

## Endpoint: Dashboard - Get core connections
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/core_connections`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "host": "127.0.0.1",
    "id": 2,
    "port": 54052,
    "staff_id": -1,
    "type": 0
  },
  {
    "host": "127.0.0.1",
    "id": 3,
    "port": 54054,
    "staff_id": -1,
    "type": 0
  },
  {
    "host": "127.0.0.1",
    "id": 4,
    "port": 54056,
    "staff_id": -1,
    "type": 0
  }
]
```

---

## Endpoint: Dashboard - Get customer portal module connections
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/cp_connections`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "127.0.0.1:59004": {
    "Object": {
      "client_ip": "127.0.0.1:59004",
      "connection_status": "closed",
      "change_status_time": "1604417710"
    },
    "Expiration": 1599814068137384146
  },
  "127.0.0.1:59064": {
    "Object": {
      "client_ip": "127.0.0.1:59064",
      "connection_status": "active",
      "change_status_time": "1604417710"
    },
    "Expiration": 1599814068137720604
  }
}
```

---

## Endpoint: Dashboard - Get database Stat
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/db_stats`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
 "queries": 6063,
 "questions": 2,
 "slow_queries": 0,
 "threads_connected": 19,
 "threads_created": 101,
 "threads_running": 1,
 "uptime": 22647
}
```

---

## Endpoint: Dashboard - Get database processes
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/db_processes`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "command": "Sleep",
    "db": "UTM5",
    "host": "localhost",
    "id": 66,
    "info": "",
    "state": "",
    "time": 20,
    "user": "root"
  },
  {
    "command": "Sleep",
    "db": "UTM5",
    "host": "localhost",
    "id": 67,
    "info": "",
    "state": "",
    "time": 20,
    "user": "root"
  },
  ...
]
```

---

## Endpoint: Dashboard - Get hotspot sessions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/hotspot_sessions`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
{
   "nas_sid" : "test",
   "core_session_id" : 123456789,
   "slink_id" : 123456789,
   "user_id" : 123456789,
   "account_id" : 123456789,
   "ip" : "1.2.3.4",
   "login" : "test",
   "start" : 123456789,
   "last_update" : 123456789,
   "end" : 123456789,
   "balance" : 123456789,
   "web_session_id": "someID"
 }..
]
```

---

## Endpoint: Dashboard - Get radius sessions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/radius_sessions`
### Parameters:
  - **Name:** `page`
    - **Type:** `Number`
    - **Description:** page number
  - **Name:** `per_page`
    - **Type:** `Number`
    - **Description:** elements per page
  - **Name:** `filter`
    - **Type:** `String`
    - **Description:** search pattern
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 0,
    "acct_delay_time": 0,
    "acct_inp_giga": 123,
    "acct_inp_oct": 123,
    "acct_inp_pack": 123,
    "acct_out_giga": 123,
    "acct_out_oct": 123,
    "acct_out_pack": 123,
    "acct_sess_time": 0,
    "acct_session_id": "",
    "acct_status_type": 0,
    "acct_term_cause": 0,
    "called_station_id": "",
    "calling_station_id": "",
    "flags": 0,
    "framed_ip": "0.0.0.0",
    "framed_ip6": "0.0.0.0",
    "framed_protocol": 0,
    "id": 0,
    "last_update_date": 0,
    "nas_id": "",
    "nas_ip": "0.0.0.0",
    "nas_port": 0,
    "nas_port_type": 0,
    "radius_attrs": [],
    "recv_date": 0,
    "service_type": 0,
    "slink_id": 0,
    "uname": ""
  }
]
```

---

## Endpoint: Dashboard - Get ram memory stat in KBytes
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/ram_stat`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
 "MemTotal" : 16000,
 "MemFree" : 6000,
 "MemAvailable" : 2000,
 "Buffers" : 1000,
 "Cached" : 1000,
 "SwapCached" : 0,
}
```

---

## Endpoint: Dashboard - Get rest connections
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/rest_connections`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "connection_status": "ESTAB",
    "local_ip_port": "127.0.0.1:9080",
    "peer_ip_port": "127.0.0.1:34862"
  }
]
```

---

## Endpoint: Dashboard - Get server stat
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/server_stat`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "avr_load_last_15min": "1,21",
  "avr_load_last_5min": "1,60",
  "avr_load_last_min": "2,22",
  "logged_users": "1",
  "uptime": " 2:44"
}
```

---

## Endpoint: Dashboard - Get stat created users
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/stat_created_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "data": 1589384568,
    "login": "{x}",
    "user_id": 5
  },
  {
    "data": 1589384844,
    "login": "0",
    "user_id": 6
  }
  ...
]
```

---

## Endpoint: Dashboard - Get stat deleted users
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/stat_deleted_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "data": 1589384568,
    "login": "{x}",
    "user_id": 5
  },
  {
    "data": 1589384844,
    "login": "0",
    "user_id": 6
  }
  ...
]
```

---

## Endpoint: Dashboard - Get tariffs history for visualisation
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/tariffs_history_graphic`
### Parameters:
  - **Name:** `data_from`
    - **Type:** `Number`
    - **Description:** Unix data from what link date return result
  - **Name:** `data_to`
    - **Type:** `Number`
    - **Description:** Unix data to what link date return result
### Example Response:

HTTP/1.1 200 OK
[
  {
    "graph_data": {
      "1.8": {
        "count_acc": 6
      },
      "2.8": {
        "count_acc": 6
      },
      "27.7": {
        "count_acc": 6
      },
      "28.7": {
        "count_acc": 8
      },
      "3.8": {
        "count_acc": 1
      },
      "31.7": {
        "count_acc": 2
      }
    },
    "tariff_id": 2,
    "tariff_name": "HS"
  },
  {
    "graph_data": {
      "10.8": {
        "count_acc": 1
      },
      "19.7": {
        "count_acc": 1
      }
    },
    "tariff_id": 1,
    "tariff_name": "iptra"
  }
]
```

---

## Endpoint: Dashboard - Get tariffs history
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/tariffs_history`
### Parameters:
  - **Name:** `data_from`
    - **Type:** `Number`
    - **Description:** Unix data from what link date return result
  - **Name:** `data_to`
    - **Type:** `Number`
    - **Description:** Unix data to what link date return result
### Example Response:

HTTP/1.1 200 OK
[
  {
    "link_date": 1597830323,
    "tariff_id": 1,
    "tariff_name": "iptra",
    "unlink_date": 1598443080,
     "account_id": 1
  },
  {
    "link_date": 1598539868,
    "tariff_id": 2,
    "tariff_name": "HS",
    "unlink_date": 1598540235,
     "account_id": 1
  }
  ...
]
```

---

## Endpoint: Dashboard - Get tech support chat customer messages
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/ts_chat/new_customer_msgs`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
   "admin_id": 0,
   "client_id": 494,
   "is_admin_origin": false,
   "last_update": 0,
   "msg": "someMessages"
 },
 {
   "admin_id": 0,
   "client_id": 494,
   "is_admin_origin": true,
   "last_update": 0,
   "msg": "someMessages"
 }
]
```

---

## Endpoint: Dashboard - Get top of process statistics
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/dashboard/top_processes`
### Parameters:
  - **Name:** `sort_type`
    - **Type:** `String`
    - **Description:** mem or cpu for sorting
### Example Response:

HTTP/1.1 200 OK
[
  {
    "%CPU": "2.4",
    "%MEM": "3.7",
    "PID": "16800",
    "PPID": "16795",
    "Process_name": "qtcreator"
  },
  {
    "%CPU": "1.3",
    "%MEM": "2.7",
    "PID": "16811",
    "PPID": "16800",
    "Process_name": "clangbackend"
  }
  ...
]
```

---

## Endpoint: Dashboard - Notify all avaliable admin about new msg
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/dashboard/tech_support_chat`
### Parameters: None
### Example Response: Not available

---

## Endpoint: Dashboard - Update own password
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/dashboard/change_own_password`
### Parameters: None
### Example Response: Not available

---

