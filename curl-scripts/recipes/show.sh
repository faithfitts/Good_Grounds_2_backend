#!/bin/bash

curl "http://localhost:8000/recipe/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
