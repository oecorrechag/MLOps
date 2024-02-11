# MLOps

![alt text](https://github.com/oecorrechag/MLOps/blob/main/images/logo.PNG)

"MLOps" was created to document all topics and development covered in the MLOps class. Written in Python 3.

## Authors

- Oscar Correa - [@oecorrechag](https://github.com/oecorrechag)
- Daniel Chavarro - [@anielFchavarro](https://github.com/anielFchavarro)
- Cristhian Palencia - [@cpalenc](https://github.com/cpalenc)

## Run app
remember: you must be in the directory where the main.py file is located "level_0/app"

### Run app in local server from docker image
create docker image, builf docker image, replace <docker_image_name> with your docker image name

```bash
docker build -t level_0 .
```
After deploy docker image in local server
```bash
docker run --name nivel_0 -p 8989:8989 nivel_0
```
### Test API
open your browser [predict penüing specie](http://localhost:8989/docs#/default/predict_penguins_predict_post)

-chose model
-if you want you can use body request [examples](http://localhost:8989/examples) to build body rrequest json
