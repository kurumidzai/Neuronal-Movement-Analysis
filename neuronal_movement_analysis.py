def analyze_neuronal_movements(movement_data):
  # Initialize variables
  avg_movement = 0
  num_movements = len(movement_data)
  
  # Calculate average movement
  for movement in movement_data:
    avg_movement += movement
  avg_movement /= num_movements
  
  # Calculate standard deviation of movements
  std_dev = 0
  for movement in movement_data:
    std_dev += (movement - avg_movement) ** 2
  std_dev = (std_dev / num_movements) ** 0.5
  
  # Return results
  return avg_movement, std_dev

# Test function
movement_data = [1, 2, 3, 4, 5]
avg, std_dev = analyze_neuronal_movements(movement_data)
print(avg) # should print 3.0
print(std_dev) # should print 1.5811388300841898
