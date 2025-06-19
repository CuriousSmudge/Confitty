def drive_csi_sequence():
    # Test data
    test_final_bytes = ['K', 'J', 'c']
    
    # The CSI handling logic (copied from handle_csi_sequence)
    def handle_csi_sequence_logic(final_byte):
        print(f"Handling CSI Sequence with final byte: {final_byte}")
        
        if final_byte == "K":  # Erase in Line
            print("Erase in Line (K)")
            return "Erase in Line"
        
        elif final_byte == "J":  # Erase in Display
            print("Erase in Display (J)")
            return "Erase in Display"
        
        elif final_byte in ["H", "f"]:  # Cursor Position
            print(f"Cursor Position ({final_byte})")
            return "Cursor Position"
        
        else:  # Unknown / Unhandled Sequence
            print(f"Unhandled CSI Sequence: {final_byte}")
            return "Unhandled"
    
    # Drive the function with test data
    print("CSI Sequence Handler Driver")

    for i in test_final_bytes:
        print(f"Final Byte: {i}, Action: {handle_csi_sequence_logic(i)}")

if __name__ == "__main__":
    drive_csi_sequence()