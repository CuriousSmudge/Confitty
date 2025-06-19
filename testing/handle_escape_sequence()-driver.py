def drive_escape_classification():
    # Test data
    test_bytes = [0x2F, ord('['), 0x5F]  # 0x2F, "[", 0x5F
    
    # The classification logic (copied from handle_escape_sequence)
    def classify_escape_sequence(byte_val, buffer_length):
        # CSI Sequence (ESC[) - C2 Control
        if buffer_length == 1 and byte_val == ord('['):
            return "C2/CSI"
        
        # C1 Control Codes
        if buffer_length == 1 and 0x40 <= byte_val <= 0x5F:
            return "C1"
        
        # C0 Single Character Escape Sequences  
        if buffer_length == 1 and (0x60 <= byte_val <= 0x7E or 0x20 <= byte_val <= 0x2F):
            return "C0"
        
        return "Unknown"
    
    for byte_val in test_bytes:
        char = chr(byte_val) if 32 <= byte_val <= 126 else 'non-printable'
        classification = classify_escape_sequence(byte_val, 1)  # Assume buffer length = 1
        
        print(f"Byte: 0x{byte_val:02X} ({char}) -> {classification}")

if __name__ == "__main__":
    drive_escape_classification()