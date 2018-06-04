#!/bin/bash

telnet localhost 5554 << EOF
sms send 1234 "hello"
gsm call 12345678
geo fix 34.0167 71.5833
EOF

echo "Putting delay before call Ending call"

sleep 10

telnet localhost 5554 << EOF
gsm cancel 12345678
EOF

echo "Call Ended"
