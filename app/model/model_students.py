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
            # split unused string data
            tmpp = input_data.split('\r\n\r\n', 1)[1]
            # split nim, nama, and angkatan
            tmp = tmpp.split('&')
            tmp1 = {}
            # open json data
            with open('db/data.json') as f:
                data_raw = json.load(f)
                data = data_raw
            # add new data from splitted POST string
            for d in tmp:
                tmp1[d.split('=')[0]] = d.split('=')[1]
            data['mahasiswa'].append(tmp1)
            # write to json
            with open('db/data.json', 'w') as wf:
                json.dump(data, wf)
            print('data successfully added!')
        except Exception as e:
            print(e)

    def update(self, data):
        pass

    def delete(self, data):
        pass
