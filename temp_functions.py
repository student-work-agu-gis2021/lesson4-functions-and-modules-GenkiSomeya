def fahr_to_celsius(temp_fahrenheit):
  converted_temp=(temp_fahrenheit-32)/1.8
  return converted_temp

def temp_classifier(temp_celsius):
  """
    Function for classfiying temperature.

    parameters
    ----------
    temp_celsius:<numercal>
      Temperature in Celsius

    Returns
    -------
    <numerical>
      Group number
    """
# Use your newly created function to print the answers to the following questions:
  if(temp_celsius<-2):
    return 0
  elif(-2<=temp_celsius<2):
    return 1
  elif(2<=temp_celsius<15):
    return 2
  elif(temp_celsius>=15):
    return 3

"""
  Sctipt for storing functions.

  Functions
  ---------
  fahr_to_celsius:
    converting temperature in Kelvins to Celsius.\
  temp_classifier:
    classfiying temperature.
"""