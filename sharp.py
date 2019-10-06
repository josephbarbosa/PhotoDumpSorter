from sightengine.client import SightengineClient
import os
from shutil import copy



# IMPORTANT NOTES
# 1. Change root_dir to the full path of file you want to analyze
# 2. Change threshold based on preference.

# ---- Change all the values that are marked with the comment CHANGE ----


# CHANGE root directory where photos are
root_dir = '/Users/josephbarbosa/Desktop/Wedding'

# CHANGE THIS IF YOU WANT TO CHANGE THRESHOLD
threshold = 0.95

# CHANGE your SightEngine API Key (Upon Making Account)
api_user_id = '1609359767'
api_key = '6HKCsvjxvKDa6c4uk8md'





#################################################################################

# Connecting to the Sight Engine API
client = SightengineClient(api_user_id, api_key)

# Holding the file_name and the associated sharpness value.
result = {}

results = open("analyzed.txt", "w+")
results_analyzed = open("algorithm_results.txt", "w+")
exception_stop = open("exception_stop.txt", "w+")

results.write("ALL files and their sharpness values\n\n")
results_analyzed.write(
    "Files and Sharpness values BASED ON GIVEN 0.95 THRESHOLD\n\n")

# For each file/picture in the directory
for directory, subdirectories, files in os.walk(root_dir):

      for file in sorted(files):

          # Handling exception in case of a non-supported file name as well as any associated API errors
          try:
            output = client.check('properties').set_file(
                os.path.join(directory, file))
            print("PRE ANALYZED " + file + " | " +
                  "Sharpness: " + str(output['sharpness']))
            results.write(file + " | " + "Sharpness Value: " +
                          str(output['sharpness']) + '\n')

            if output['sharpness'] > threshold:
                result[file] = output['sharpness']
                copy(os.path.join(directory, file),
                     os.getcwd() + '/Analyzed_Images')

            else:
                copy(os.path.join(directory, file),


                     os.getcwd() + '/Under_Threshold')

          except Exception as e:
            exception_stop.write('Exception last occured at file ' + str(file) + '\n')
            print('Exception ' + str(e) + ' has occured.')


# Write out to a file
for item, val in result.items():
    results_analyzed.write(
        item + " | " + "Sharpness Value: " + str(val) + '\n')


print("\nPROGRAM HAS FINISHED RUNNING :)\n")

##################################################################################