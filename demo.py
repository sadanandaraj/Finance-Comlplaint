from pymongo import MongoClient

mongodb_url = "mongodb+srv://sadanandaraj52:sadanandaraj@cluster0.af4n9i3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_url)
db = client["finance_artifact263"]
collection_name = "evaluation"

print("------------------------------------------------------------------------------------------------")

class ModelEvaluationArtifact:
    def __init__(self, model_name, evaluation_result):
        self.model_name = model_name
        self.evaluation_result = evaluation_result

    def to_dict(self):
        return {
            "model_name": self.model_name,
            "evaluation_result": self.evaluation_result
        }

class ModelEvaluationArtifactData:
    def __init__(self):
        try:
            self.client = client
            self.db = db
            self.collection = self.db[collection_name]
        except Exception as e:
            print(e)

    def save_eval_artifact(self, model_eval_artifact):
        self.collection.insert_one(model_eval_artifact.to_dict())
        print("Artifact saved successfully.")

    def get_eval_artifact(self, query):
        artifact = self.collection.find_one(query)
        if artifact:
            print("Artifact found:")
            print(artifact)
        else:
            print("Artifact not found.")

# Create the collection if it does not exist
if collection_name not in db.list_collection_names():
    db.create_collection(collection_name)
    print(f"Collection '{collection_name}' created.")

# Usage example:
data = ModelEvaluationArtifactData()
artifact = ModelEvaluationArtifact("Model1", 0.85)
data.save_eval_artifact(artifact)
data.get_eval_artifact({"model_name": "Model1"})

