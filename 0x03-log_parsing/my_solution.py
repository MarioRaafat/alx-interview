#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def run():
    try:
        total_size = 0
        line_count = 0
        status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        valid_status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

        for line in sys.stdin:
            # Strip whitespace and split the line into components
            parts = line.strip().split()
            
            # Check if the line matches the expected format
            if len(parts) < 9:
                continue

            status = parts[7]
            file_size = parts[8]

            try:
                # Convert status and file size to integers
                #status = int(status)
                file_size = int(file_size)

                # Update total file size and status code count if status is valid
                total_size += file_size
                if status in valid_status_codes:
                    status_counts[int(status)] += 1

            except ValueError:

                continue  # Skip the line if conversion fails

            # Increment the line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL + C)
        print_statistics(total_size, status_counts)
        sys.exit(0)

    # Print final statistics if the end of the input is reached
    print_statistics(total_size, status_counts)

if __name__ == '__main__':
    run()