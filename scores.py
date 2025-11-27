import sys


if len(sys.argv) > 1:
    script_name = sys.argv[0]
    scores = sys.argv[1:]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    scores = ["50", "70", "90", "85", "40"]   
    print("No input given — using default values:")

scores = [int(s) for s in scores]


total = sum(scores)
average = total / len(scores)




print("\n--- Array Score Processing ---")
print("Script Name:", script_name)
print("Scores:", scores)
print("Total:", total)
print("Average:", average)

