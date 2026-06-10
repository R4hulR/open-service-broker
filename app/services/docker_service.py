import docker
#to talk to docker daemon, we not to instantiate a client
client = docker.from_env()


def provision_container(instance_id:str):
    container = client.containers.run("redis:latest",name=instance_id,detach=True,ports={"6379/tcp": None})
    #This is the equivalent of running docker run -d redis:latest in the terminal. A few things to note:
    #name=instance_id — we name the container after the instance ID so we can find it later during bind or deprovision
    # detach=True — runs the container in the background, otherwise our code would block waiting for it
    # ports={"6379/tcp": None} — exposes Redis's default port. None tells Docker to assign a random available port — important because multiple Redis instances can't share the same port
    container.reload()
    container_id = container.id
    port = container.ports["6379/tcp"][0]["HostPort"]
    #Docker assigns the port dynamically, so we need to reload the container info to find out which port it got. We'll need this port later when the platform calls /bind to get credentials
    return (container_id,port)

