# Empty class for bypassing improper codegen for cases that have
# both multipart/form-data and application/json requests
class EmptyJsonBody:
    def to_dict(self):
        return {}
