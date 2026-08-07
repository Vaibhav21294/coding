ls -1 | wc -l

# If you're on macOS/Linux, use:

find . -type f -name "*.py" | wc -l
# What it does
# find . → starts from the current directory
# -type f → only files
# -name "*.py" → only Python files
# | wc -l → counts them

# If you want to see the files as well as count them:

# find . -type f -name "*.py"

# For example, if there are 127 Python files, the first command outputs:

# 127