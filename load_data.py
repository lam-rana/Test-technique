import os
import yaml

path_to_data = os.path.join(os.path.dirname(
    __file__), 'fake_liste_users_revo_130122.yaml')
print("loading data file, wait...")
with open(path_to_data, 'r') as data_file_content:
    users_list = yaml.load(data_file_content, Loader=yaml.FullLoader)
print("data load complete!")

print("Total number of users : ", len(users_list))
