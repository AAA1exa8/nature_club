import struct

def flip_endianness(data, fmt):
    """
    Flip the endianness of the given binary data.
    
    :param data: Input binary data (bytes)
    :param fmt: Format string compatible with struct module
    :return: Binary data with flipped endianness
    """
    # Unpack the data using native endianness
    native_data = struct.unpack(fmt, data)
    
    # Flip endianness and pack it back
    if '<' in fmt:  # If it's little-endian
        flipped_fmt = fmt.replace('<', '>')
    elif '>' in fmt:  # If it's big-endian
        flipped_fmt = fmt.replace('>', '<')
    else:
        raise ValueError("Format must specify endianness using '<' or '>'")
    
    flipped_data = struct.pack(flipped_fmt, *native_data)
    return flipped_data

def flip_file_endianness(input_file_path, output_file_path, fmt):
    """
    Flip the endianness of a binary file and write the result to a new file.
    
    :param input_file_path: Path to the input binary file
    :param output_file_path: Path to the output binary file
    :param fmt: Format string compatible with struct module
    """
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        while True:
            # Read a chunk of data from the file
            data = infile.read(4)
            if not data:  # End of file
                break
            
            # Ensure the data is the correct size
            if len(data) != 4:
                raise ValueError("Unexpected end of file or incomplete data.")

            # Flip the endianness of the chunk
            flipped_data = flip_endianness(data, fmt)
            
            # Write the flipped data to the output file
            outfile.write(flipped_data)

# Example usage
# Specify the input and output file paths and data format
input_file = 'output.bin'  # Input binary file
output_file = 'output_be.bin'  # Output binary file after flipping endianness
data_format = '<I'  # Example: 32-bit integer (modify as needed)

flip_file_endianness(input_file, output_file, data_format)

print(f"The endianness of {input_file} has been flipped and written to {output_file}.")

def flip_bytes(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            # Read 8 bytes from the input file
            chunk = infile.read(8)
            if not chunk:
                break  # End of file reached

            # Ensure that we have exactly 8 bytes to process
            if len(chunk) < 8:
                # If fewer than 8 bytes are left, we may handle it or just break
                # For simplicity, we can ignore the last incomplete chunk.
                # Alternatively, you'd want to handle this case according to your specific requirements
                print("Incomplete chunk found, ending process.")
                break

            # Split the chunk into two parts
            first_4_bytes = chunk[:4]
            second_4_bytes = chunk[4:]

            # Flip the two parts
            flipped_chunk = second_4_bytes + first_4_bytes

            # Write the flipped chunk to the output file
            outfile.write(flipped_chunk)

# Usage
input_file = 'output_be.bin'   # Specify the input file name
output_file = 'output_be_f.bin' # Specify the output file name
flip_bytes(input_file, output_file)

