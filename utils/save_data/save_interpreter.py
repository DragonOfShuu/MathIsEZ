import json

class Data:
    file_name = "utils/save_data/save_file.json"
    def __init__(self):
        self._update()
        self.unsaved = self.data_raw
    
    @property 
    def data_raw(self):
        self._update()
        return self._data_raw;
    
    @data_raw.setter
    def data_raw(self, value):
        self._data_raw = value
        self._update
        return self.data_raw;
    
    @property 
    def unsaved(self):
        return self._unsaved;
    
    @unsaved.setter 
    def unsaved(self, value):
        self._unsaved = value 
        return self.unsaved;
    
    def save(self):
        with open(self.file_name, 'w', encoding="utf-8") as x:
            x.write(json.dumps(self.unsaved));
        self._update;
        return self.data_raw;
    
    def discard(self):
        self.unsaved = self.data_raw
        return self.unsaved;

    def _update(self):
        '''
        You do not need to use
        this function; simply
        get and set data.
        '''
        with open(self.file_name, 'r', encoding="utf-8") as x:
            self._data_raw = json.loads(x.read())