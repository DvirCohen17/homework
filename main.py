def serialize_ascii_art(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        serialized_data = []

        for line in lines:
            char_count = {}
            serialized_line = ""
            temp = line[0]
            for char in line:
                current = char
                if temp != current:
                    count = char_count[temp]
                    serialized_line += f"{count}{temp}"

                    char_count.pop(temp)
                    temp = char

                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            serialized_data.append(serialized_line)

        with open(output_file, 'w') as file:
            for line in serialized_data:
                file.write(line + '\n')
                print(line)

        print(f"Serialized {input_file} to {output_file} successfully.")
    except Exception as e:
        print(f"Serialization failed: {str(e)}")

def deserialize_ascii_art(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        deserialized_data = []

        for line in lines:
            deserialized_line = ""
            i = 0
            while i < len(line):
                count = ""
                while i < len(line) and line[i].isdigit():
                    count += line[i]
                    i += 1
                if count:
                    char = line[i]
                    deserialized_line += char * int(count)
                    i += 1
                else:
                    deserialized_line += line[i]
                    i += 1
            deserialized_data.append(deserialized_line)

        with open(output_file, 'w') as file:
            for line in deserialized_data:
                file.write(line)
                print(line + "\n")

        print(f"Deserialized {input_file} to {output_file} successfully.")
    except Exception as e:
        print(f"Deserialization failed: {str(e)}")

def rotate_ascii_art(source_file, dest_file, rotation_degree):
    try:
        # Read the source file
        with open(source_file, 'r') as source:
            ascii_art = source.read()

            rotated_ascii = ascii_art

            lines = ascii_art.split('\n')

            if rotation_degree == 90:
               rotated_ascii = '\n'.join([''.join(row[i] for row in ascii_art.split('\n')[::-1]) for i in range(len(ascii_art.split('\n')[0]))])
            elif rotation_degree == 180:
                rotated_ascii = ascii_art[::-1]
            elif rotation_degree == 270:
                rotated_ascii = '\n'.join([''.join(row[i] for row in ascii_art.split('\n'))[::-1] for i in range(len(ascii_art.split('\n')[0])-1, -1, -1)])
            elif rotation_degree == 360:
                rotated_ascii = ascii_art

        # Save the rotated ASCII art to the destination file
        with open(dest_file, 'w') as dest:
            dest.write(rotated_ascii)
    except Exception as e:
        print(f"Failed: {str(e)}")

def load_conversion_table():
    conversion_table = {}

    try:
        with open("conversion_file.txt", 'r') as file:
            lines = file.readlines()

        for line in lines:
            if len(line) >= 3:
                source_char = line[0]
                option1 = line[1]
                option2 = line[2]
                conversion_table[source_char] = (option1, option2)

    except Exception as e:
        print(f"Failed to load conversion table: {str(e)}")

    return conversion_table

def apply_conversion_table(text, conversion_table, conversion_choice):
    converted_text = ""
    for char in text:
        if char in conversion_table and conversion_choice == 1:
            converted_text += conversion_table[char][0]
        elif char in conversion_table and conversion_choice == 2:
            converted_text += conversion_table[char][1]
        else:
            #for mission number 4
            #converted_text += char
            converted_text += "X"
    return converted_text

def main():
    print("Rotate ASCII Art")
    choice = input("Do you want to do it? y/n ")

    if choice == 'y':
        input_file = input("Enter the path of the input ASCII art file: ")
        output_file = input("Enter the path for the rotated output file: ")
        rotation_degrees = int(input("Enter rotation degrees (0, 90, 180, 270, or 360): "))
        rotate_ascii_art(input_file, output_file, rotation_degrees)

    print("Apply Conversion Table")
    choice = input("Do you want to do it? y/n ")

    if choice == 'y':
        input_text = input("Enter the text to apply conversion to: ")
        conversion_choice = int(input("Enter conversion choice (0 for no conversion, 1 for option1, 2 for option2): "))
        conversion_table = load_conversion_table()
        converted_text = apply_conversion_table(input_text, conversion_table, conversion_choice)
        print("Converted text:")
        print(converted_text)

    print("ASCII Art Serializer and Deserializer")
    print("1. Serialize ASCII Art")
    print("2. Deserialize ASCII Art")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        input_file = input("Enter the path of the input ASCII art file: ")
        output_file = input("Enter the path for the serialized output file: ")
        serialize_ascii_art(input_file, output_file)
    elif choice == '2':
        input_file = input("Enter the path of the serialized input file: ")
        output_file = input("Enter the path for the deserialized output file: ")
        deserialize_ascii_art(input_file, output_file)

    else:
        print("Invalid choice. Please enter '1' for Serialize or '2' for Deserialize.")


if __name__ == "__main__":
    main()
