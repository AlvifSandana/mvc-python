import json


class ModelStudents:
    def read_all(self):
        try:
            with open('db/data.json') as f:
                data_raw = json.load(f)
                data = data_raw['mahasiswa']
        except FileNotFoundError as FNF:
            data = {'message': f'File not found. ({FNF})'}
        except Exception as e:
            data = {'message': f'{e}'}
        return data

    def read_by_nim(self, nim):
        pass

    def create(self, input_data):
        try:
            with open('db/data.json') as f:
                data_raw = json.load(f)
                data = data_raw['mahasiswa']
            data.append({
                'nim': input_data['nim'],
                'nama': input_data['nama'],
                'angkatan': input_data['angkatan'],
            })
            print('data successfully added!')
        except Exception as e:
            print(e)


    def update(self, data):
        pass

    def delete(self, data):
        pass
