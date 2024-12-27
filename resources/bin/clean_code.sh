#!/bin/sh
# This script is used to clean the code by running autoflake, black and flake8 on the codebase
# It will remove unused imports and variables, format the code and check for linting errors
# It will run on the following directories:
# - main.py
# - src
# - tests
# - utils
# It will check if the directories exist before running the commands
# You can add more directories to the directories array if needed or update the existing ones
# It will also check if autoflake, black and flake8 are installed before running the commands
# If any of the commands are not installed, it will exit the script
# To run the script, use the following command:
# sh clean_code.sh

# Define the main root directory
PROJECT_DIR=$(dirname $(dirname $(dirname $(realpath $0))))

# Check if autoflake is installed
if ! command -v autoflake &> /dev/null
then
    echo "autoflake could not be found, please install it using 'pip install autoflake'"
    exit
fi

# Check if black is installed
if ! command -v black &> /dev/null
then
    echo "black could not be found, please install it using 'pip install black'"
    exit
fi

# Check if flake8 is installed
if ! command -v flake8 &> /dev/null
then
    echo "flake8 could not be found, please install it using 'pip install flake8'"
    exit
fi

# Define the directories and files to lint
targets=(
    "$PROJECT_DIR/main.py"
    "$PROJECT_DIR/src"
    "$PROJECT_DIR/tests"
    "$PROJECT_DIR/utils"
)

printf " *** Starting cleaning code *** \n"

# Run autoflake
printf "Running autoflake...\n"
for target in "${targets[@]}"; do
    if [ -d "$target" ] || [ -f "$target" ]; then
        printf "Running autoflake on %s\n" "$target"
        autoflake --remove-all-unused-imports --remove-unused-variables --in-place --recursive "$target"
    else
        printf "Directory or file %s does not exist\n" "$target"
    fi
done

# Run black
printf "Running black...\n"
for target in "${targets[@]}"; do
    if [ -d "$target" ] || [ -f "$target" ]; then
        printf "Running black on %s\n" "$target"
        black --verbose "$target"
    else
        printf "Directory or file %s does not exist\n" "$target"
    fi
done

# Run flake8
printf "Running flake8...\n"
for target in "${targets[@]}"; do
    if [ -d "$target" ] || [ -f "$target" ]; then
        printf "Running flake8 on %s\n" "$target"
        flake8 --verbose "$target"
    else
        printf "Directory or file %s does not exist\n" "$target"
    fi
done

printf " *** Cleaning code completed *** \n"