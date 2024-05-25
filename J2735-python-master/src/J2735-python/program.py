from J2735Decoders import decodeSPAT

# Configuration
PACKETS_FILE = 'path_to_your_packets_file.txt'  # Replace with the path to your file

# Function to read and decode UDP packets from a file
def read_and_decode_packets(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Remove spaces and newline characters, and decode hex string
            hex_string = line.replace(' ', '').strip()
            packet = bytes.fromhex(hex_string)
            # Decode the packet
            decoded_msg = decodeSPAT(packet)
            print(decoded_msg)

if __name__ == "__main__":
    read_and_decode_packets(PACKETS_FILE)

