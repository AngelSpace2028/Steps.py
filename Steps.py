import itertools

MAX_TABLES = 4300  # Maximum number of tables to print

def main():
    try:
        n = int(input("Enter the number of steps (e.g., 12): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Number of steps must be positive.")
        return

    # All inverse sequences: +1 and *2
    inverse_ops = ['+1', '*2']
    total_possible = 2 ** n
    # Limit the total to show (cap at MAX_TABLES)
    total_to_show = min(total_possible, MAX_TABLES)
    print(f"\nGenerating {total_to_show} table(s) out of {total_possible} total sequences...\n")

    count = 0
    for inv_seq in itertools.product(inverse_ops, repeat=n):
        # Stop if we have reached the limit
        if count >= MAX_TABLES:
            break

        # 1. Compute the starting number by applying inverse ops from 0
        start = 0
        for op in inv_seq:
            if op == '+1':
                start += 1
            else:  # '*2'
                start *= 2

        # 2. Reverse the inverse sequence and swap operations
        #    +1  -> -1
        #    *2  -> /2
        forward_ops = []
        for op in reversed(inv_seq):
            if op == '+1':
                forward_ops.append('-1')
            else:
                forward_ops.append('/2')

        # 3. Apply forward_ops to get all intermediate values
        values = [start]
        cur = start
        for op in forward_ops:
            if op == '-1':
                cur -= 1
            else:  # '/2'
                cur //= 2
            values.append(cur)

        # 4. Print the table
        count += 1
        print(f"{'='*55}")
        print(f"Table {count} of {total_to_show}")
        for i, (fop, val_after) in enumerate(zip(forward_ops, values[1:]), start=1):
            prev = values[i-1]
            if fop == '-1':
                print(f"{i}. {prev} - 1 = {val_after}")
            else:
                print(f"{i}. {prev} : 2 = {val_after}")
        print(f"\nTotal steps: {n}\n")

if __name__ == "__main__":
    main()
