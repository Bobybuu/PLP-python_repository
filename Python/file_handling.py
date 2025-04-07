def read_modify_and_write_file():
    # Ask the user for the filename to read from
    input_filename = input("Enter the filename to read from: ")
    
    try:
        # Step 1: Open the input file and read its content
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Step 2: Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # Modify the content as desired (e.g., to uppercase)
        
        # Ask the user for a new filename to write to
        output_filename = input("Enter the filename to write the modified content to: ")
        
        # Step 3: Write the modified content to the new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read/write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_modify_and_write_file()
