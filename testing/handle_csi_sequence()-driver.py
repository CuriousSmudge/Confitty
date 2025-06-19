def drive_csi_sequence():
    # Test data
    test_final_bytes = ['K', 'J', 'c']
    
    # Mock canvas and cursor (simplified)
    class MockCell:
        def __init__(self):
            self.text = "X"  # Put some text to see erase effects
    
    class MockCursor:
        def __init__(self):
            self.x = 5
            self.y = 3
    
    # The CSI handling logic (copied from handle_csi_sequence)
    def handle_csi_sequence_logic(final_byte, cursor, canvas, width, height):
        print(f"Handling CSI Sequence with final byte: {final_byte}")
        
        if final_byte == "K":  # Erase in Line
            print("Erase in Line (K)")
            for x in range(cursor.x, width):
                canvas[x][cursor.y].text = ""
            return "Erase in Line"
        
        elif final_byte == "J":  # Erase in Display
            print("Erase in Display (J)")
            for x in range(width):
                for y in range(height):
                    canvas[x][y].text = ""
            return "Erase in Display"
        
        elif final_byte in ["H", "f"]:  # Cursor Position
            print(f"Cursor Position ({final_byte})")
            cursor.x = 0
            cursor.y = 0
            return "Cursor Position"
        
        else:  # Unknown / Unhandled Sequence
            print(f"Unhandled CSI Sequence: {final_byte}")
            return "Unhandled"
    
    # Drive the function with test data
    print("CSI Sequence Handler Driver")
    print("=" * 30)
    
    # Set up mock environment
    width, height = 10, 5
    
    for final_byte in test_final_bytes:
        print(f"\n--- Testing final byte: '{final_byte}' ---")
        
        # Reset environment for each test
        canvas = [[MockCell() for _ in range(height)] for _ in range(width)]
        cursor = MockCursor()
        
        print(f"Before: Cursor at ({cursor.x}, {cursor.y})")
        print(f"Before: Canvas has text: {canvas[5][3].text}")
        
        # Call the logic
        result = handle_csi_sequence_logic(final_byte, cursor, canvas, width, height)
        
        print(f"After: Cursor at ({cursor.x}, {cursor.y})")
        print(f"After: Canvas[5][3] text: '{canvas[5][3].text}'")
        print(f"Result: {result}")

if __name__ == "__main__":
    drive_csi_sequence()