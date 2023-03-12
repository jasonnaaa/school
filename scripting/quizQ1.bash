#!/bin/bash

read -p "Enter the Name of the state: " state
read -p "Enter the name of the city: " city

echo ${city^} ${state^} >> locationinfo