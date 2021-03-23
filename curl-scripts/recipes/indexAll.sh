#!/bin/bash

curl "http://localhost:8000/recipes" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
