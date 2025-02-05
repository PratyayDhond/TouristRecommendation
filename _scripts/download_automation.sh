#!/bin/bash

# Initialize a counter
counter=0
sleep 3

while true; do
  # Increment the counter
  counter=$((counter + 1))
  
  # Log the current iteration
  echo "Iteration: $counter"
  
  # Simulate pressing Ctrl+S
  echo "Pressing Ctrl+S..."
  xdotool keydown Control_L
  xdotool key s
  xdotool keyup Control_L
  
  # Wait for 3 seconds
  sleep 2
  
  # Simulate pressing Return/Enter
  echo "Pressing Return/Enter..."
  xdotool key Return
  
  # Wait for 1 second
  sleep 1
  
  # Simulate pressing Ctrl+W
  echo "Pressing Ctrl+W..."
  xdotool keydown Control_L
  xdotool key w
  xdotool keyup Control_L
  
  
  sleep 1
  
  # Log the completion of the cycle
  echo "Completed iteration $counter."
  echo "----------------------------------"
done

