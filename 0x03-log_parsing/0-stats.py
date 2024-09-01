#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_counts.keys())
line_count = 0

def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def run():
    try:
        for line in sys.stdin:
            # Strip whitespace and split the line into components
            parts = line.strip().split()

            # Check if the line matches the expected format
            if len(parts) < 7:
                continue

            ip, dash, datetime_part, method, path, protocol, status, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]

            try:
                # Convert status and file size to integers
                status = int(status)
                file_size = int(file_size)

                # Update total file size and status code count if status is valid
                total_size += file_size
                if status in valid_status_codes:
                    status_counts[status] += 1
            except ValueError:
                continue  # Skip the line if conversion fails

            # Increment the line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL + C)
        print_statistics()
        sys.exit(0)

    # Print final statistics if the end of the input is reached
    print_statistics()

if __name__ == '__main__':
    run()