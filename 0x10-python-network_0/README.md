# Python - Network #0 — Alx System Engineering DevOps
0x10. Python - Network #0

```Bash```
```Python```
```Scripting```
```Back-end```
```API```

URLs and HTTP are fundamental concepts for navigating the web and understanding how data is transmitted between clients and servers.

## URL Components
A URL (Uniform Resource Locator) is composed of several components:

- **Scheme**: Indicates the protocol being used, such as "*http://*" or "*https://*".
- **Domain Name**: The human-readable name of the server hosting the resource.
- **Sub-Domain**: Optionally, a subdivision of the domain.
- **Port Number**: If specified, it indicates the port on the server to connect to.
- **Path**: The specific location of the resource on the server.
- **Query String**: Additional parameters passed to the server.
- **Fragment Identifier**: Specifies a specific section within the resource.

```http
https://www.example.com:8080/path/to/resource?param1=value1&param2=value2#section3
```

## Domain Name vs Sub-Domain

- **Domain Name:** A human-readable label that corresponds to a specific IP address on the internet, used to identify and locate computers and resources.

- **Sub-Domain:** A subdivision of a larger domain, allowing for further organization of resources under a domain name.

    ```http
    Sub-Domain: blog.example.com
    ```

## HTTP Basics
HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting data over the internet. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

## HTTP Request and Response

- **HTTP Request**: A message sent from a client (such as a web browser) to a server, specifying the action to be performed and any necessary data.

- **HTTP Response**: A message sent from a server to a client in response to an HTTP request. It contains the requested resource or indicates an error.

## HTTP Components

- **HTTP Headers:** Additional information sent with an HTTP request or response, providing metadata about the message.

- **HTTP Message Body**: Contains the data being sent in an HTTP request or response, such as HTML content or file data.

- **HTTP Request Method**: Specifies the action to be performed on the server, such as GET, POST, PUT, DELETE, etc.

- **HTTP Response Status Code**: Indicates the success or failure of an HTTP request, such as 200 for a successful request or 404 for "not found".
    ```http
    GET /path/to/resource HTTP/1.1
    Host: www.example.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
    ```

## Additional Concepts

**HTTP Cookies**: Small pieces of data sent from a website and stored on the user's computer by the web browser, commonly used for session management and tracking user activity.
```http
Set-Cookie: session_id=abc123; Expires=Wed, 09 Jun 2021 10:18:14 GMT;
```

Cookies are mainly used for three purposes:

- **Session management:**
    
    Logins, shopping carts, game scores, or anything else the server should remember

- **Personalization:**
    
    User preferences, themes, and other settings

- **Tracking:**
    
    Recording and analyzing user behavior

## Making Requests with cURL
``cURL`` is a command-line tool for transferring data using various protocols, including HTTP. To make a request, use the "curl" command followed by the URL.
```bash
curl https://example.com
```

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
