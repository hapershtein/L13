## Agent Function Examples

Here are examples of how to call the agent functions and their possible outputs:

### `get_geolocation()`

**Description:** Retrieves the current geolocation information.

**User Prompt Example:**
```
What's my current location?
```

**Example Call:**
```python
agent.get_geolocation()
```

**Example Output:**
```json
{
  "latitude": 34.0522,
  "longitude": -118.2437,
  "city": "Los Angeles",
  "country": "United States"
}
```

### `get_local_time()`

**Description:** Retrieves the current local time.

**User Prompt Example:**
```
What time is it?
```

**Example Call:**
```python
agent.get_local_time()
```

**Example Output:**
```json
{
  "time": "2025-10-23 10:30:00 PST",
  "timezone": "America/Los_Angeles"
}
```

### `get_upgradable_packages()`

**Description:** Lists packages that have available upgrades on the system.

**User Prompt Example:**
```
Are there any packages that need upgrading?
```

**Example Call:**
```python
agent.get_upgradable_packages()
```

**Example Output:**
```json
{
  "upgradable_packages": [
    "python3-pip",
    "apt",
    "snapd"
  ]
}
```