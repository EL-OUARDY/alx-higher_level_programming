#!/bin/bash
# sends a GET request to a URL (with a header variable), and displays the size of the body of the response
curl -sH "X-School-User-Id: 98" "$1"
