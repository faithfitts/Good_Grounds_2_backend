#!/bin/bash

curl "http://localhost:8000/recipes/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
