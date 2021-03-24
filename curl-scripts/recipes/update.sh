#!/bin/bash

curl "http://localhost:8000/recipe/${ID}/" \
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
