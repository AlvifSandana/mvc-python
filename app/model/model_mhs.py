import json


class ModelMahasiswa:
    def read(self):
        try:
            with open('db/data.json') as f:
                data_raw = json.load(f)
                data = data_raw['mahasiswa']
        except FileNotFoundError as FNF:
            data = {'message': f'File not found. ({FNF})'}
        except Exception as e:
            data = {'message' : f'{e}'}
        return data

    def create(self):
        pass

    def update(self, data):
        pass

    def delete(self, data):
        pass