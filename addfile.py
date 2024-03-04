import argparse
import os
import csv 
import shutil

path = os.path.join(os.getcwd(), 'files')

def get_args():
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and not file.startswith('.')]
    parser = argparse.ArgumentParser()
    parser.add_argument("file" , choices=files, help="filename to move to the appropriate folder (e.g. hello.png)")
    args = parser.parse_args()

    return args.file

def manage_folder():
    type_dict = [
    {'fold':'audio', 'f_ext': 'mp3'},
    {'fold':'doc', 'f_ext': 'txt'},
    {'fold':'doc', 'f_ext': 'odt'},
    {'fold':'images', 'f_ext': 'png'},
    {'fold':'images', 'f_ext': 'jpg'},
    {'fold':'images', 'f_ext': 'jpeg'}]

    file = get_args()
    file_name, file_ext = file.rsplit('.', 1)
    file_path = file_path = os.path.join(path, file)
    folder = next(item for item in type_dict if item['f_ext'] == file_ext)['fold']

    #check if the folder exists, otherwise create it
    if not os.path.isdir(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

    #print the information
    print(file_name + " type:" + folder + " size: " + str(os.path.getsize(file_path)) + "B")   
    file_detail = file.rsplit(".", 1)[0] + "," + folder + "," + str(os.path.getsize(file_path))

    #check if there is a file with the same name and if so, change the destination name
    destination_folder = os.path.join(path, folder)
    count = 1
    while os.path.exists(os.path.join(destination_folder, file)):
        file = f"{file_name}({count}).{file_ext}"
        count += 1
    
    #move file
    source = os.path.join(path, get_args())
    destination = os.path.join(destination_folder, file)

    shutil.move(source, destination)

    manage_recap_csv(file_detail)

def manage_recap_csv(detail):
    insert_header = False

    if not os.path.exists(os.path.join(os.getcwd(), 'recap.csv')):
        insert_header = True    

    with open('recap.csv', 'a') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        if insert_header:
            csv_columns = ['name', 'type', 'size (B)']
            csvwriter.writerow(csv_columns)
        csvwriter.writerow(detail)

manage_folder()