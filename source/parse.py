import json

## Open the file:
with open("output.txt", "r") as f:
    lines = f.readlines()

## JSON setup
data = {}

# Look for compilation errors first
for index,line in enumerate(lines):
    if line[0:22] == "attempting to assemble":
        ## Check for EOF or no assembly successful message
        if index+1 == len(lines) or lines[index+1] != "assembly successful\n":
            data["score"] = 0
            data["output"] = "Your code didn't compile :'(\nMake sure you have no syntax errors!"
            with open("results/results.json", "w") as file:
                json.dump(data, file)
            exit()

# No compilation errors, so let's start grading!
with open("output.txt", "r") as f2:
    text = f2.readlines()

# Parse to get testcase scores:
all_tests = []
test_name = ""
in_test = False
for line in text:
    test = {}
    if line[0:5] == "Test:":
        test_name = line.strip()
        in_test = True
    elif line[0:19] == "Test points earned:":
        in_test = False
    elif in_test:
        test["name"] = test_name
        test["output"] = line.strip()
        test["score"] = (float(line.strip().split("(+")[1].split(" pts)")[0]))
        ## Passed or failed
        status = (line.strip().split("=> ")[1].split(" ")[0].lower())
        test["status"] = status + "ed"
        all_tests.append(test)
data["tests"] = all_tests

## Write to JSON
with open("results/results.json", "w") as file:
    json.dump(data, file)
