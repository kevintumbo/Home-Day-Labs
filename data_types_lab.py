def data_type(data):
    if isinstance(data, str):
        return len(data)
        
    if data is None:
      return "no value"
      
    if isinstance(data, bool):
        if data is True:
            return True
        else:
            return False
    if isinstance(data, int):
        if data < 100:
            return "less than 100"
        elif data == 100:
            return "equal to 100"
        else:
            return "more than 100"
    if isinstance(data, list):
        if len(data) >= 3:
            return data[2]
        else:
            return None