#!/bin/bash

curl "http://localhost:8000/allrecipes/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
