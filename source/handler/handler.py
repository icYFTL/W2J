from io import BytesIO
from os import path, mkdir, system, remove
from core import dwebp
import uuid
from base64 import encodebytes


class Handler:
    def __init__(self, image: BytesIO):
        self.image = image

    def __save(self) -> str:
        if not path.exists('tmp'):
            mkdir('tmp')
        uniq = uuid.uuid4().hex
        _path = path.join('tmp', f'temp_file{uniq}.webp')
        open(_path, 'wb').write(self.image.read())
        return _path

    def __clear(self, paths: list) -> None:
        for _path in paths:
            try:
                remove(_path)
            except:
                pass

    def run(self) -> str:
        file = self.__save()

        system('{dwebp} {input_img} -o {output_img}'.format(
            dwebp=dwebp,
            input_img=file,
            output_img=file.replace('webp', 'jpeg')
        ))

        if path.exists(file.replace('webp', 'jpeg')):
            result = encodebytes(open(file.replace('webp', 'jpeg'), 'rb').read()).decode('UTF-8')
            self.__clear([file, file.replace('webp', 'jpeg')])
            return result
        else:
            self.__clear([file])
            raise Exception('Smth went wrong')
