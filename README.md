# CORS Proxy

A simple CORS proxy application built with Flask to bypass CORS restrictions while making HTTP requests.

## Features
- Handles all HTTP methods (GET, POST, PUT, DELETE, PATCH, OPTIONS).
- Passes headers and data from the client to the target server.
- Returns the response from the target server, maintaining status codes and headers.
- Lightweight and easy to set up locally.

## Requirements
- Python 3.7+
- Flask
- Flask-CORS
- Requests

## Installation

1. Clone this repository or copy the provided code.

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python cors_proxy.py
   ```

4. The proxy will be available at `http://localhost:8989`.

## Usage

### Making Requests
To use the proxy, pass the target URL as the `url` query parameter. For example:

```bash
GET http://localhost:8989/?url=https://api.example.com/resource
```

### Example with cURL
```bash
curl -X GET "http://localhost:8989/?url=https://api.example.com/resource"
```

### Example with Fetch (JavaScript)
```javascript
fetch('http://localhost:8989/?url=https://api.example.com/resource')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Notes
- Ensure that the `url` parameter is a complete and valid URL.
- Avoid using this proxy in production environments as it does not implement authentication or rate limiting.

## License
This project is licensed under the MIT License.
