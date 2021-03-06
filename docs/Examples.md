
# Examples

## models

### upload_model

How to upload a model file on notebook. 

**Code**

```
from afs import models

# Write a file as model file.
with open('model.h5', 'w') as f:
    f.write('dummy model')

# User-define evaluation result. Type:dict
extra_evaluation = {
    'confusion_matrix_TP': 0.9,
    'confusion_matrix_FP': 0.8,
    'confusion_matrix_TN': 0.7,
    'confusion_matrix_FN': 0.6,
    'AUC': 1.0
}

# User-define Tags. Type:dict
tags = {'machine': 'machine01'}

# User-define Feature Importance Type:list(dict)
feature_importance = [
	{'feature': 'petal_length', 'importance': 0.9473576807512394}, 
	{'feature': 'petal_width',  'importance': 0.038191635936882906}, 
	{'feature': 'sepal_length', 'importance': 0.011053241240641932}, 
	{'feature': 'sepal_width',  'importance': 0.0033974420712357825}
]

coefficient = [
	{'feature': 'B-0070-0068-1-FN66F_strength', 'coefficient': -4.730741400252476}, 
	{'feature': 'B-0070-0068-1-FN66F_vendor', 'coefficient': -0.9335123601234512}, 
	{'feature': 'B-0070-0068-1-FN66F_tensile','coefficient': 0.16411707246054036}, 
	{'feature': 'B-0070-0068-1-FN66F_lot','coefficient': -0.08745686004816221}, 
	{'feature': 'Machine','coefficient': 0.015048547152059243}, 
	{'feature': 'Lot','coefficient': -0.010971975766858174}, 
	{'feature': 'RPM','coefficient': 0.0003730247816832932}, 
	{'feature': 'record_purpose','coefficient': 0.0}
]


# Model object
afs_models = models()

# Upload the model to repository and the repository name is the same as file name, the the following is optional parameters:
#   1. (optional) accuracy is a evaluation of the model by the result of testing.
#   2. (optional) loss is a evaluation of the model by the result of testing.
#   3. (optional) extra_evaluation is for other evaluations for the model, you can put them to this parameter.
#   4. (optional) tags is the label for the model, like the time of data or the type of the algorithm.
#   5. (optional) feature_importance is the record how the features important in the model.
#	6. (optional) coefficient indicates the direction of the relationship between a predictor variable and the response variable.
afs_models.upload_model(
    model_path='model.h5',
	model_repository_name='model.h5',
	accuracy=0.4,
	loss=0.3, 
	extra_evaluation=extra_evaluation, 
	tags=tags,
	feature_importance=feature_importance,
	coefficient=coefficient,
)

# Get the latest model info 
model_info = afs_models.get_latest_model_info(model_repository_name='model.h5')

# See the model info
print(model_info)
```

**results**
```
{
	'uuid': '3369315c-d652-4c4d-b481-405be2ad5b33',
	'name': '3369315c-d652-4c4d-b481-405be2ad5b33',
	'model_repository': 'ef388859-64fb-4718-b90f-34defc8a3aae',
	'owner': '12345338-62b6-11ea-b1de-d20dfb084846',
	'evaluation_result': {
		'accuracy': 0.4,
		'loss': 0.3,
		'confusion_matrix_TP': 0.9,
		'confusion_matrix_FP': 0.8,
		'confusion_matrix_TN': 0.7,
		'confusion_matrix_FN': 0.6,
		'AUC': 1.0
	},
	'tags': {
		'machine': 'machine01'
	},
	'feature_importance': [{
		'feature': 'petal_length',
		'importance': 0.9473576808
	}, {
		'feature': 'petal_width',
		'importance': 0.0381916359
	}, {
		'feature': 'sepal_length',
		'importance': 0.0110532412
	}, {
		'feature': 'sepal_width',
		'importance': 0.0033974421
	}],
	'coefficient': [
		{'feature': 'B-0070-0068-1-FN66F_strength', 'coefficient': -4.730741400252476}, 
		{'feature': 'B-0070-0068-1-FN66F_vendor', 'coefficient': -0.9335123601234512}, 
		{'feature': 'B-0070-0068-1-FN66F_tensile','coefficient': 0.16411707246054036}, 
		{'feature': 'B-0070-0068-1-FN66F_lot','coefficient': -0.08745686004816221}, 
		{'feature': 'Machine','coefficient': 0.015048547152059243}, 
		{'feature': 'Lot','coefficient': -0.010971975766858174}, 
		{'feature': 'RPM','coefficient': 0.0003730247816832932}, 
		{'feature': 'record_purpose','coefficient': 0.0}
	],
	'size': 11,
	'created_at': '2020-04-06T10:23:56.228000+00:00'
}
```


### get_latest_model_info

**Code**
```
from afs import models
afs_models = models()
afs_models.get_latest_model_info(model_repository_name='model.h5')
```

**Output**
```
{
	'evaluation_result': {
		'accuracy': 0.123,
		'loss': 0.123
	},
	'tags': {},
	'created_at': '2018-09-11 10:15:54'
}
```


###  download_model

**Code**
```
from afs import models

# Model object
afs_models = models()

# Download model from model repository, and get the last one model.
afs_models.download_model(
	save_path='dl_model.h5', 
	model_repository_name='model.h5', 
	last_one=True)

# Or get the specific model name in the model repository.
afs_models.download_model(
	save_path='dl_model.h5', 
	model_repository_name='model.h5', 
	model_name='2019-07-10 02:59:11.610828')

# List the directory
!ls
```

**Output**
```
dl_model.h5 
```



### upload_model (big model)

How to upload a big model (300MB-1GB) file on notebook. 

Both `encode_blob_accessKey` and `encode_blob_secretKey` can be gotten from encoded blob credential `accessKey` and `blob_secretKey` by `base64`. Developer can use `python` to encode or use web tool like [utilities-online](http://www.utilities-online.info/base64/#.XRG3H9MzbOQ).


**Code**

```
from afs import models

# Write a big file as 301 MB model file.
f = open('big_model.h5', "wb")
f.seek((301 * 1024 * 1024 + 1) - 1)
f.write(b"\0")
f.close()

# User-define evaluation result
extra_evaluation = {
    'AUC': 1.0
}

# User-define Tags 
tags = {'machine': 'machine01'}

# Model object
afs_models = models()
afs_models.set_blob_credential(
	blob_endpoint="http://x.x.x.x:x",
	encode_blob_accessKey="ENCODE_BLOB_ACCESSKEY", 
	encode_blob_secretKey="ENCODE_BLOB_SECRETKEY"
	)


# Upload the model to repository and the repository name is the same as file name.
# Accuracy and loss is necessary, but extra_evaluation and tags are optional.
afs_models.upload_model(
    model_path='big_model.h5', 
	accuracy=0.4, 
	loss=0.3, 
	extra_evaluation=extra_evaluation, 
	tags=tags, 
	model_repository_name='model.h5', 
	blob_mode=True)

```

(Update 2019-09-18) Using `AFS 2.1.27006` or later, the `set_blob_credential` method can be ignored. Like the following:

```
from afs import models

# Write a big file as 301 MB model file.
f = open('big_model.h5', "wb")
f.seek((301 * 1024 * 1024 + 1) - 1)
f.write(b"\0")
f.close()

# User-define evaluation result
extra_evaluation = {
    'AUC': 1.0
}

# User-define Tags 
tags = {'machine': 'machine01'}

# Model object
afs_models = models()

# Upload the model to repository and the repository name is the same as file name.
# Accuracy and loss is necessary, but extra_evaluation and tags are optional.
afs_models.upload_model(
    model_path='big_model.h5', 
	accuracy=0.4, 
	loss=0.3, 
	extra_evaluation=extra_evaluation, 
	tags=tags, model_repository_name='model.h5', 
	blob_mode=True)

```


**Output**
```
{
	'uuid': '433184a2-e930-465d-8b03-ecf0d649a7f9',
	'name': '2019-06-25 01:42:44.810366',
	'model_repository': 'bff9ea46-8856-4eef-b8dc-a4879a6ed9f9',
	'owner': 'dd9fcd3b-cfe7-47ec-9452-5157efcf1e50',
	'evaluation_result': {
		'accuracy': 0.4,
		'loss': 0.3,
		'AUC': 1.0
	},
	'parameters': {},
	'tags': {
		'machine': 'machine01'
	},
	'size': 315621377,
	'created_at': '2019-06-25T01:42:44.821000+00:00'
}
```


### Upload Model Metafile
To upload model metafile to AFS. In order to maintain performance upload the file, developer has to input blob credential.

Both `encode_blob_accessKey` and `encode_blob_secretKey` can be gotten from encoded blob credential `accessKey` and `blob_secretKey` by `base64`. Developer can use `python` to encode or use web tool like [utilities-online](http://www.utilities-online.info/base64/#.XRG3H9MzbOQ).


**Code**
```
from afs import models

# Write a file as model metafile.
with open('model_meta_data.txt', 'w') as f:
    f.write('dummy model')


# SDK Model object
afs_models = models()
afs_models.set_blob_credential(
	blob_endpoint="http://x.x.x.x:x",
	encode_blob_accessKey="ENCODE_BLOB_ACCESSKEY", 
	encode_blob_secretKey="ENCODE_BLOB_SECRETKEY"
	)

# Create a model_repository
afs_models.create_model_repo("test_model_repository")

# Upload a model metafile under model_repository. If the name of metafile is existed, this upload will overwrite.
afs_models.upload_model_metafile(
        file_path='model_meta_data.txt',
        name="test_metafile",
        model_repository_name="test_model_repository",
    )
```

**Output**
```
{
	"uuid": "4dde12a1-c035-4b6d-ae1e-96baf28fb42e",
	"name": "test_metafile",
	"model_repository": "7ae7667a-273b-47be-a538-79b0e6531775",
	"owner": "c5442dba-7c12-4955-b161-4a7578e314b9",
	"size": 11,
	"blob_key": "model_metafile\/c5442dba-7c12-4955-b161-4a7578e314b9\/7ae7667a-273b-47be-a538-79b0e6531775\/4dde12a1-c035-4b6d-ae1e-96baf28fb42e",
	"created_at": "2019-08-05T05:37:28.762000+00:00",
	"update_time": "2019-08-05T05:51:34.180000+00:00",
	"deploy_time": [],
	"status": "done"
}
```


### [Advanced] Token download_model


**Code**
```
from afs import models

# AFS connect info. 
# Example format, CANNOT COPY AND PASTE.
# AFS API target endpoint
target_endpoint="https://api.afs.wise-paas.com"

# AFS service instance id
instance_id="123e4567-e89b-12d3-a456-426655440000"

# WISE-PaaS SSO token be gotten from SSO authentication
token="bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vdWFhLmFyZmEud2lzZS1wYWFzLmNvbS90b2tlbl9rZXlzIiwia2lkIjoia2V5LTEiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJjZWExYTMwMGNjMmY0YzczYmMyNmY3Y2FiNTIwYjI4YSIsInN1YiI6IjhiNTJjODk0LTkyNmEtNDA4Mi1iNTdlLTc4ZDYwNjQ5MzI2OSIsInNjb3BlIjpbImNsb3VkX2NvbnRyb2xsZXIucmVhZCIsInBhc3N3b3JkLndyaXRlIiwiY2xvdWRfY29udHJvbGxlci53cml0ZSIsIm9wZW5pZCIsInVhYS51c2VyIl0sImNsaWVudF9pZCI6ImNmIiwiY2lkIjoiY2YiLCJhenAiOiJjZiIsImdyYW50X3R5cGUiOiJwYXNzd29yZCIsInVzZXJfaWQiOiI4YjUyYzg5NC05MjZhLTQwODItYjU3ZS03OGQ2MDY0OTMyNjkiLCJvcmlnaW4iOiJ1YWEiLCJ1c2VyX25hbWUiOiJCZW4yMDE5LkNodWFuZ0BhZHZhbnRlY2guY29tLnR3IiwiZW1haWwiOiJCZW4yMDE5LkNodWFuZ0BhZHZhbnRlY2guY29tLnR3IiwiYXV0aF90aW1lIjoxNTYyODM2ODA0LCJyZXZfc2lnIjoiNGU4NGIyOTQiLCJpYXQiOjE1NjM0NDQwOTksImV4cCI6MTU2MzQ0NDY5OSwiaXNzIjoiaHR0cHM6Ly91YWEuYXJmYS53aXNlLXBhYXMuY29tL29hdXRoL3Rva2VuIiwiemlkIjoidWFhIiwiYXVkIjpbImNsb3VkX2NvbnRyb2xsZXIiLCJwYXNzd29yZCIsImNmIiwidWFhIiwib3BlbmlkIl19.R1SHUv8CIIoEN1pL5aGjxTn3OMB1rgjumD0hFFFrqNVIwcctN4QvNH1kK6G6SZyrlXvjU_TXNDAbsAXiWLUkG7L60GZR2ZpJyPGNemZITjffuCKi0paQOrmAW5S0Nvn505G955DbuGDMGxQPOaorAcOkJYzFfAujSoZk3KMZmId9ACXr_Z96Fx5yhYnfXjT9aZDsASsx9I5UHYpunHRbzINJFx2PIxrYwCzfX2vFJqgeqeyeE1rjRsoS6GRj7eM3ud4YKQaC-MK0TFttkTeRtPwggUJV51QhDmH03EYQ5qVFqsixE_zPGKFQb4wnTkdWGUOyBjoYSTuzk_dUZNbHGG"

# Model object
my_models = models(
    target_endpoint=target_endpoint,
    instance_id=instance_id,
    token=token,
)

# Download model from model repository, and get the last one model.
my_models.download_model(save_path='dl_model.h5', model_repository_name='model.h5', last_one=True)

# Or get the specific model name in the model repository.
my_models.download_model(save_path='dl_model.h5', model_repository_name='model.h5', model_name='2019-07-10 02:59:11.610828')

# List the directory
!ls
```

**Output**
```
dl_model.h5 
```