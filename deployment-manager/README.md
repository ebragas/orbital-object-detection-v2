## How to run deployment using Deployment Manager and gcloud 

### Create a new deployment
Create a new deployment using the configuration file:

```
gcloud deployment-manager deployments create quickstart-deployment --config ./deployment-manager/vm.yaml
```

If the deployment is successful, you'll receive the following message:

```
Create operation operation-1547849829426-57fc2df3fa350-deaa04de-307babf4 completed successfully.
NAME                      TYPE                 STATE      ERRORS  INTENT
quickstart-deployment-vm  compute.v1.instance  COMPLETED  []
```

### Check the deployment
Check the deployment status with:

```
gcloud deployment-manager deployments describe quickstart-deployment
```

You should receive a description like this one:

```
fingerprint: TkumSYH7RUqE39SmKYpmqA==
id: '5738092776557375114'
insertTime: '2019-01-18T14:17:09.521-08:00'
manifest: manifest-1547849829532
name: quickstart-deployment
operation:
  endTime: '2019-01-18T14:17:52.848-08:00'
  name: operation-1547849829426-57fc2df3fa350-deaa04de-307babf4
  operationType: insert
  progress: 100
  startTime: '2019-01-18T14:17:09.847-08:00'
  status: DONE
  user: ericbragas.4128615@gmail.com
NAME                      TYPE                 STATE      INTENT
quickstart-deployment-vm  compute.v1.instance  COMPLETED
```

### Review your resources
You should be able to see the deployed resources in the Google Cloud Console.

1. Open the Deployment Manager page
2. Click `quickstart-deployment`
3. To see resource info, click the resource name e.g. `quickstart-deployment-vm`

### Clean up
Delete resources associated with a deployment:

```
gcloud deployment-manager deployments delete quickstart-deployment
```

Confirm you want to delete the list of resources when prompted, then confirm in the console that all resources have been terminated.

### Sources
* [Google Cloud Deployment Manager Quickstart](https://cloud.google.com/deployment-manager/docs/quickstart)
