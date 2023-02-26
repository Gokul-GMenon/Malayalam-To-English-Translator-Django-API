import requests


class XLS_R:

    def __init__(self):

        self.API_URL = "https://api-inference.huggingface.co/models/5p33ch3xpr/XLS-R_Finetuned"
        self.headers = {"Authorization": "Bearer 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"}


    # def return_dic(self, filename):
       

    #     item = {'path': filename}

    #     # Resampling
    #     speech_array, sampling_rate = torchaudio.load(str(item["path"]))
        
    #     if sampling_rate != 16000:
    #         item["speech"] = np.asarray(librosa.resample(np.asarray(speech_array[0]), sampling_rate, 16000))  
    #     else:
    #         item["speech"] = np.array(speech_array[0])
        
    #     item["sampling_rate"] = 16_000


    #     temp = {}

    #     # assert (
    #     #     len(set(item["sampling_rate"])) == 1
    #     # ), f"Make sure all inputs have the same sampling rate of {processor.feature_extractor.sampling_rate}."

    #     temp["input_values"] = self.processor(item["speech"], sampling_rate=item["sampling_rate"]).input_values
        
    #     # with processor.as_target_processor():
    #     #     temp["labels"] = processor(item["sentence"]).input_ids
    #     # temp['sentence'] = item["sentence"]

    #     return temp


    # def evaluate(self, batch):
        
    #     inputs = self.processor(batch["input_values"], sampling_rate=16_000, return_tensors="pt", padding=True)
        
    #     with torch.no_grad():
    #         logits =self.model(inputs.input_values.to("cpu"), attention_mask=inputs.attention_mask.to("cpu")).logits

    #     pred_ids = torch.argmax(logits, dim=-1)
    #     batch["pred_strings"] = self.processor.batch_decode(pred_ids)
        # return batch

    def predict(self, file_name):
     
        with open(file_name, "rb") as f:
            data = f.read()
        response = requests.post(self.API_URL, headers=self.headers, data=data)
        return response.json()

        return self.evaluate(self.return_dic(file_name))['pred_strings']

# file_name = 'Rc1.wav'

# obj = XLS_R()

# print()
# print(obj.predict(file_name))
