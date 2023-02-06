temp_df = states.copy()

# Add a bit of padding for future values:
extra_space = 5
temp_df.columns = [x.center(len(x) + extra_space) for x in temp_df.columns]

# Get just the header.
header = '\n'.join(temp_df.iloc[:0].to_markdown(tablefmt='psql', index=False).splitlines()[:3])

with open('texttest.txt', 'w') as f:
    # write the header to file:
    f.write(header + '\n')
    # For each row that you want,
    # make a new output with just that row.
    # Then cut the header off.
    for row in range(len(temp_df[:3])):
        lines = '\n'.join(temp_df.iloc[[row]].to_markdown(tablefmt='psql', index=False).splitlines()[3:])
        # Write the row to file.
        f.write(lines + '\n') 