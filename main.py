import os
import subprocess

def get_template_number():
    template_number = int(input("Enter the template number: "))
    return template_number

# Get the template number from user input
template_number = get_template_number()

# Set the template number in a file
with open('./plots/template_number.txt', 'w') as file:
    file.write(str(template_number))  # Write the template number to the file

# Print the selected template number
print("Template number selected:", template_number)

# Run the analysis scripts

# ? Run the scripts for the resolution bias with mle metric
subprocess.run(["python", "resolution_bias/captioning_run/run_captioning.py", "--do_mle_based_logits","True"])
subprocess.run(["python", "analysis/resolution_bias/run_preliminary_analysis.py", "--do_mle_based_logits","True"])
subprocess.run(["python", "analysis/resolution_bias/return_benchmark.py", "--do_mle_based_logits","True"])