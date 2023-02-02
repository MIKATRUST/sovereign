
class Model:
    def __init__(self, data):
        self.data = data
        print("constructor Model")
        print(f"constructor Model:{data}")

    
    def get_data(self):
        """Get the data stored in the model object"""
        return self.data + 10
