#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
lines_processed = 0


def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 6:
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_file_size += file_size
                status_code_counts[status_code] += 1
                lines_processed += 1

                # Check if 10 lines have been processed
                if lines_processed == 10:
                    print_statistics()
                    lines_processed = 0
            except ValueError:
                pass  # Ignore lines with invalid data
except KeyboardInterrupt:
    pass  # Handle CTRL+C gracefully

# Print the final statistics
print_statistics()
