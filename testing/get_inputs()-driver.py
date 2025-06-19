def drive_function():
    # Test Data
    keys = [72, 69, 76, 76, 79]
    
    # The function logic (copied from get_inputs)
    def get_inputs_logic(key_code, shift, ctrl, alt):
        con_keys = {72: 'h', 69: 'e', 76: 'l', 79: 'o'}
        con_shift = {72: 'H', 69: 'E', 76: 'L', 79: 'O'}
        
        if not ctrl and not shift and not alt and key_code in con_keys:
            return con_keys[key_code]
        if shift and key_code in con_shift:
            return con_shift[key_code]
        return None
    
    # Drive the function with test data
    print("Test 1:", [get_inputs_logic(k, False, False, False) for k in keys])
    print("Test 2:", [get_inputs_logic(k, True, False, False) for k in keys])
    print("Test 3:", [get_inputs_logic(k, True, True, False) for k in keys])

drive_function()