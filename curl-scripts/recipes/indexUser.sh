#!/bin/bash

curl "http://localhost:8000/userRecipes" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
