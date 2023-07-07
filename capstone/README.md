# Capstone project: light curve classifier on AWS
Serving a trained lightGBM classifier as a webservice on AWS [flask](http://flask.pocoo.org/) and [docker](https://www.docker.com/).

## Steps
1. Use Light_curve_classifier_experiment_with_different_models.ipynb to train random forest and grandient boosting classifiers on the [ALERCE ZTF datasets](https://zenodo.org/record/4279623) and generate pickled model files for different layers (hierarchical_level_lgbm_model.pkl, periodic_level_lgbm_model.pkl, stochastic_level_lgbm_model.pkl, transient_level_lgbm_model.pkl)
2. After comparison and for simplicity, chose the lightGBM classifier for each layer.
3. Use app.py to wrap the lightGBM models and serve the model as a REST webservice via flask. Ran it locally by:
    * Execute the command `python app.py` to start the flask app.
    * Go to the browser and hit the url `0.0.0.0:80` to get a message `Welcome to LC classifier` displayed. **NOTE**: A permission error may be received at this point. In this case, change the port number to 5000 in `app.run()` command in `app.py`. 
    (Port 80 is a privileged port, so change it to some port that isn't)
    * To test the app, run the curl_periodic.sh, curl_stochastic.sh, and curl_transient.sh in terminal to query the flask server. Make sure to change the url to `0.0.0.0:80` in the scripts. It should give results of 'RRL', 'YSO', and 'CV/Nova' respectively.
4. Run ```docker build -t app-lcclassifier .``` to  build the docker image using ```Dockerfile```.
5. Run ```docker run -p 80:80 app-lcclassifier``` to run the docker container that got generated using the `app-lcclassifier` docker image.
6. Select a cloud service provider (in this project we use AWS ec2) to run API on the cloud. Follow the steps of [blog](https://medium.com/@tanuj.jain.10/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf) to set up the cloud machine, especially:
    * Generate SSH key pairs and store the permission key locally.
    * log in to the remote machine and install docker with `sudo yum install docker`, `sudo service docker start`, `sudo usermod -a -G docker ec2-user`
    * scp app.py, pickle files, Dockerfile, requirements.txt to the remote machine.
    * Repeat the `docker build` and `docker run` commands in the previous steps.
    * To test the app, run the curl_periodic.sh, curl_stochastic.sh, and curl_transient.sh in terminal to query the flask server. It should give results of 'RRL', 'YSO', and 'CV/Nova' respectively.
