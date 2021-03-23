#!/bin/bash

curl "http://localhost:8000/recipes/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "recipes": {
      "title": "'"${TITLE}"'",
      "description": "'"${DESCRIPTION}"'",
      "method": "'"${METHOD}"'",
      "ingredients": "'"${INGREDIENTS}"'"
    }
  }'

echo
