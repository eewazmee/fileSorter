from pathlib import Path
import shutil


def file_sorter(path: str = str()):
    entries = Path(path)
    if entries.exists():
        # print('this folder exists')
        for file in entries.iterdir():
            file_path = path + '/' + file.name
            if file.name.endswith('.mp3'):
                shutil.move(file_path, '/home/samir/Music/')

            elif file.name.endswith('.jpeg') or file.name.endswith('.jpg') or file.name.endswith('.png'):
                if file.name.startswith('fde'):
                    shutil.move(file_path, '/home/samir/Pictures/fde/')
                elif file.name.startswith('pp'):
                    shutil.move(file_path,'/home/samir/Pictures/pp/')
                else:
                    shutil.move(file_path, '/home/samir/Pictures/')

            elif file.name.endswith('.mp4'):
                shutil.move(file_path, '/home/samir/Videos/')

            elif file.name.endswith('.pdf'):
                shutil.move(file_path, '/home/samir/Documents')

