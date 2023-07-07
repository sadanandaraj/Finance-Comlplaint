# from finance_complaint.config import mongo_client 

# from finance_complaint.entity.artifact_entity import ModelEvaluationArtifact


# class ModelEvaluationArtifactData:

#     def __init__(self):
#         self.client = mongo_client
#         self.database_name = "finance_artifact"
#         self.collection_name = "evaluation"
#         self.collection = self.client[self.database_name][self.collection_name]

#     def save_eval_artifact(self, model_eval_artifact: ModelEvaluationArtifact):
#         self.collection.insert_one(model_eval_artifact.to_dict())

#     def get_eval_artifact(self, query):
#         self.collection.find_one(query)

from finance_complaint.entity.artifact_entity import ModelEvaluationArtifact
from pymongo import MongoClient

mongodb_url = "mongodb+srv://sadanandaraj52:sadanandaraj@cluster0.af4n9i3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_url)
# db = client["finance_artifact3"]
db = client["finance_artifact666"]  # Corrected line
print("------------------------------------------------------------------------------------------------")
class ModelEvaluationArtifactData:
    def __init__(self):
        try:
            self.client = client
            self.db = db  # Corrected line
            self.collection = self.db["evaluation222"]
        except Exception as e:
            print(e)

    def save_eval_artifact(self, model_eval_artifact: ModelEvaluationArtifact):
        self.collection.insert_one(model_eval_artifact.to_dict())

    def get_eval_artifact(self, query):
        return self.collection.find_one(query)  # Corrected line